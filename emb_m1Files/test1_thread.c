// ============================================================
// Project Name: 
// Description :
//
// File Name   : test1_thread.c
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-12 14:58:56
// ============================================================

#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <pthread.h>

void* test1_thread(void *arg)
{
    (void)arg;

    // 
    for (;;) {
        sleep(1);
    }
    return NULL;
}

// ============================================================
// END OF FILE
// ============================================================
    

    