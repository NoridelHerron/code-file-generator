// ============================================================
// Project Name: 
// Description :
//
// File Name   : test2.c
// Dependencies:
// Author      : nds
// Date        : 2026-01-11 16:18:29
// ============================================================

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>

void* test2_thread(void *arg)
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
    

    