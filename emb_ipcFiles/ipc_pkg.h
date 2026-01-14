
// ============================================================
// Project Name: 
// Description :
//
// File Name   : ipc_pkg.h
// Dependencies:
// Author      : Noridel Herron
// Date        : 2026-01-13 23:47:23
// ============================================================

#ifndef IPC_PKG_H
#define IPC_PKG_H

#include <stdint.h>
#include <pthread.h>

/* Magic constant used to validate shared memory */
#define AWESOME 0x192938fa

/* Example shared packet */
struct  noris_packet {
    uint32_t        shm_magic;   /* Shared memory validity check */
    pthread_mutex_t lock;        /* Process-shared mutex */
};

/* Typedef used by IPC */
typedef struct noris_packet noris_packet_t;

#endif /* IPC_PKG_H */

// ============================================================
// END OF FILE
// ============================================================
