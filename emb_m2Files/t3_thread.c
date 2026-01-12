// ============================================================
// Project Name: 
// Description :
//
// File Name   : t3_thread.c
// Dependencies:
// Author      : Nori
// Date        : 2026-01-12 14:59:35
// ============================================================

#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <pthread.h>

void* t3_thread(void *arg)
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
    

    