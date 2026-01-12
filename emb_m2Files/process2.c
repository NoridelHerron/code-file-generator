
// ============================================================
// Project Name: 
// Description :
//
// File Name   : process2.c
// Dependencies:
// Author      : Nori
// Date        : 2026-01-12 14:59:35
// ============================================================

#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <pthread.h>

int main(void)
{
    pthread_t t0_t;
	pthread_t t1_t;
	pthread_t t2_t;
	pthread_t t3_t;
	pthread_t t4_t;
	pthread_t t5_t;
	pthread_t t6_t;
	pthread_t t7_t;
	pthread_t t8_t;
	pthread_t t9_t;

    if (ipc_init() < 0) {
        fprintf(stderr, "IPC init failed\n");
        return 1;
    }

    /* Start the Threads */
    pthread_create(&t0_t, NULL, t0_thread, NULL);
	pthread_create(&t1_t, NULL, t1_thread, NULL);
	pthread_create(&t2_t, NULL, t2_thread, NULL);
	pthread_create(&t3_t, NULL, t3_thread, NULL);
	pthread_create(&t4_t, NULL, t4_thread, NULL);
	pthread_create(&t5_t, NULL, t5_thread, NULL);
	pthread_create(&t6_t, NULL, t6_thread, NULL);
	pthread_create(&t7_t, NULL, t7_thread, NULL);
	pthread_create(&t8_t, NULL, t8_thread, NULL);
	pthread_create(&t9_t, NULL, t9_thread, NULL);

    /* Wait for Threads */
    pthread_join(t0_t, NULL);
	pthread_join(t1_t, NULL);
	pthread_join(t2_t, NULL);
	pthread_join(t3_t, NULL);
	pthread_join(t4_t, NULL);
	pthread_join(t5_t, NULL);
	pthread_join(t6_t, NULL);
	pthread_join(t7_t, NULL);
	pthread_join(t8_t, NULL);
	pthread_join(t9_t, NULL);

    /* Clean up */
    ipc_cleanup();

    return 0;
}

// ============================================================
// END OF FILE
// ============================================================
    