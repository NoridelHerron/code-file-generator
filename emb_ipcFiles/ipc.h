
// ============================================================
// Project Name: 
// Description :
//
// File Name   : ipc.h
// Dependencies:
// Author      : Noridel Herron
// Date        : 2026-01-13 23:47:23
// ============================================================

#ifndef IPC_INTERFACE_H
#define IPC_INTERFACE_H

#include "ipc_pkg.h"

/* Initialize shared memory and synchronization primitives */
int  ipc_init(void);

/* Release IPC resources */
void ipc_cleanup(void);

/* Write latest packet into shared memory */
void ipc_send_packet(const noris_packet_t *pkt);

/* Read latest packet from shared memory */
int  ipc_receive_packet(noris_packet_t *pkt);

#endif /* IPC_INTERFACE_H */

// ============================================================
// End of File
// ============================================================
