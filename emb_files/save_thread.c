// ============================================================
// Project Name: 
// Description :
//
// File Name   : save.c
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-12 10:52:45
// ============================================================

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>

void* save_thread(void *arg)
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
    

    