// ============================================================
// Project Name: 
// Description :
//
// File Name   : lcd_thread.c
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-12 14:54:53
// ============================================================

#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <pthread.h>

void* lcd_thread(void *arg)
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
    

    