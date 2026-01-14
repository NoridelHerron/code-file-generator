
// ============================================================
// Project Name: 
// Description :
//
// File Name   : ipc.c
// Dependencies:
// Author      : Noridel Herron
// Date        : 2026-01-13 23:47:23
// ============================================================

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <semaphore.h>
#include <pthread.h>

#include "ipc_pkg.h"

#define SHM_NAME "/herron_shm"
#define SEM_NAME "/herron_sem"

static noris_packet_t *shared_packet = NULL;
static sem_t *data_ready = NULL;

int ipc_init(void)
{
    int fd;

    fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
    if (fd < 0) {
        perror("shm_open");
        return -1;
    }

    if (ftruncate(fd, sizeof(noris_packet_t)) < 0) {
        perror("ftruncate");
        close(fd);
        return -1;
    }

    shared_packet = mmap(NULL,
                         sizeof(noris_packet_t),
                         PROT_READ | PROT_WRITE,
                         MAP_SHARED,
                         fd,
                         0);
    close(fd);

    if (shared_packet == MAP_FAILED) {
        perror("mmap");
        shared_packet = NULL;
        return -1;
    }

    data_ready = sem_open(SEM_NAME, O_CREAT, 0666, 0);
    if (data_ready == SEM_FAILED) {
        perror("sem_open");
        return -1;
    }

    if (shared_packet->shm_magic != AWESOME) {
        memset(shared_packet, 0, sizeof(noris_packet_t));

        pthread_mutexattr_t attr;
        pthread_mutexattr_init(&attr);
        pthread_mutexattr_setpshared(&attr, PTHREAD_PROCESS_SHARED);
        pthread_mutex_init(&shared_packet->lock, &attr);
        pthread_mutexattr_destroy(&attr);

        shared_packet->shm_magic = AWESOME;
    }

    return 0;
}

// ****************************************

void ipc_send_packet(const noris_packet_t *pkt)
{
    if (!shared_packet || !data_ready) return;

    pthread_mutex_lock(&shared_packet->lock);
    memcpy(shared_packet, pkt, sizeof(noris_packet_t));
    pthread_mutex_unlock(&shared_packet->lock);

    sem_post(data_ready);
}

// ****************************************

int ipc_receive_packet(noris_packet_t *pkt)
{
    if (!shared_packet || !data_ready) return -1;

    if (sem_wait(data_ready) != 0) {
        perror("sem_wait");
        return -1;
    }

    pthread_mutex_lock(&shared_packet->lock);
    memcpy(pkt, shared_packet, sizeof(noris_packet_t));
    pthread_mutex_unlock(&shared_packet->lock);

    return 0;
}

// ****************************************

void ipc_cleanup(void)
{
    if (shared_packet) {
        munmap(shared_packet, sizeof(noris_packet_t));
        shared_packet = NULL;
    }

    if (data_ready) {
        sem_close(data_ready);
        data_ready = NULL;
    }

    shm_unlink(SHM_NAME);
    sem_unlink(SEM_NAME);
}

// ============================================================
// END OF FILE
// ============================================================
