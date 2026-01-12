
// ============================================================
// Project Name: 
// Description :
//
// File Name   : process1.c
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-12 14:58:56
// ============================================================

#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <pthread.h>

int main(void)
{
    pthread_t test1_t;
	pthread_t test2_t;
	pthread_t test3_t;

    if (ipc_init() < 0) {
        fprintf(stderr, "IPC init failed\n");
        return 1;
    }

    /* Start the Threads */
    pthread_create(&test1_t, NULL, test1_thread, NULL);
	pthread_create(&test2_t, NULL, test2_thread, NULL);
	pthread_create(&test3_t, NULL, test3_thread, NULL);

    /* Wait for Threads */
    pthread_join(test1_t, NULL);
	pthread_join(test2_t, NULL);
	pthread_join(test3_t, NULL);

    /* Clean up */
    ipc_cleanup();

    return 0;
}

// ============================================================
// END OF FILE
// ============================================================
    