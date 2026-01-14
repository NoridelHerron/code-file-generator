
## ============================================================
## Project Name: 
## Description :
##
## File Name   : ipc_content.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-13 21:15:29
## ============================================================

from utilities.shared_helpers import (
    Print_Sep,
    Print_Header
)

from gen_generator.std_lib import (
    Standard_Lib
)

## ============================================================
##  Function/s Only
## ============================================================

def IPC_FileContent(
        file_name,
        author,
        shm_name,
        sem_name,
        packet_type,
        magic_define
    ):

    header = Print_Header (
                file_name,
                author,
                "//",
                ".c" )
    
    lib    = Standard_Lib (file_name)
    sep    = Print_Sep()
    star   = Print_Sep(True)

    result = f"""
{header}
{lib}
#define SHM_NAME "/{shm_name}"
#define SEM_NAME "/{sem_name}"

static {packet_type} *shared_packet = NULL;
static sem_t *data_ready = NULL;

int ipc_init(void)
{{
    int fd;

    fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
    if (fd < 0) {{
        perror("shm_open");
        return -1;
    }}

    if (ftruncate(fd, sizeof({packet_type})) < 0) {{
        perror("ftruncate");
        close(fd);
        return -1;
    }}

    shared_packet = mmap(NULL,
                         sizeof({packet_type}),
                         PROT_READ | PROT_WRITE,
                         MAP_SHARED,
                         fd,
                         0);
    close(fd);

    if (shared_packet == MAP_FAILED) {{
        perror("mmap");
        shared_packet = NULL;
        return -1;
    }}

    data_ready = sem_open(SEM_NAME, O_CREAT, 0666, 0);
    if (data_ready == SEM_FAILED) {{
        perror("sem_open");
        return -1;
    }}

    if (shared_packet->shm_magic != {magic_define}) {{
        memset(shared_packet, 0, sizeof({packet_type}));

        pthread_mutexattr_t attr;
        pthread_mutexattr_init(&attr);
        pthread_mutexattr_setpshared(&attr, PTHREAD_PROCESS_SHARED);
        pthread_mutex_init(&shared_packet->lock, &attr);
        pthread_mutexattr_destroy(&attr);

        shared_packet->shm_magic = {magic_define};
    }}

    return 0;
}}

// {star}

void ipc_send_packet(const {packet_type} *pkt)
{{
    if (!shared_packet || !data_ready) return;

    pthread_mutex_lock(&shared_packet->lock);
    memcpy(shared_packet, pkt, sizeof({packet_type}));
    pthread_mutex_unlock(&shared_packet->lock);

    sem_post(data_ready);
}}

// {star}

int ipc_receive_packet({packet_type} *pkt)
{{
    if (!shared_packet || !data_ready) return -1;

    if (sem_wait(data_ready) != 0) {{
        perror("sem_wait");
        return -1;
    }}

    pthread_mutex_lock(&shared_packet->lock);
    memcpy(pkt, shared_packet, sizeof({packet_type}));
    pthread_mutex_unlock(&shared_packet->lock);

    return 0;
}}

// {star}

void ipc_cleanup(void)
{{
    if (shared_packet) {{
        munmap(shared_packet, sizeof({packet_type}));
        shared_packet = NULL;
    }}

    if (data_ready) {{
        sem_close(data_ready);
        data_ready = NULL;
    }}

    shm_unlink(SHM_NAME);
    sem_unlink(SEM_NAME);
}}

// {sep}
// END OF FILE
// {sep}
"""
    # *************
    return result
    # *************

## ****************************************

def IPC_packageContent( file_name, 
                        author,
                        packet_type, 
                        magic_define,
                        mem_addr ):

    header = Print_Header (
                file_name,
                author,
                "//",
                ".h" )
    
    lib    = Standard_Lib ("ipc_pkg")
    sep    = Print_Sep()

    if packet_type.endswith("_t"):
        packet_name = packet_type[:-2]
    else:
        packet_name = packet_type
        packet_type += "_t"

    result = f"""
{header}

#ifndef IPC_PKG_H
#define IPC_PKG_H
{lib}
/* Magic constant used to validate shared memory */
#define {magic_define} {mem_addr}

/* Example shared packet */
struct  {packet_name} {{
    uint32_t        shm_magic;   /* Shared memory validity check */
    pthread_mutex_t lock;        /* Process-shared mutex */
}};

/* Typedef used by IPC */
typedef struct {packet_name} {packet_type};

#endif /* IPC_PKG_H */

// {sep}
// END OF FILE
// {sep}
"""
    # *************
    return result
    # *************

## ============================================================
##  End of File
## ============================================================

