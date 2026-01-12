// ============================================================
// Project Name: 
// Description :
//
// File Name   : lcd.c
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-12 10:52:45
// ============================================================

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>

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
    

    