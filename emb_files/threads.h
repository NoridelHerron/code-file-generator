
// ============================================================
// Project Name: 
// Description :
//
// File Name   : threads.h
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-12 10:52:45
// ============================================================

#ifndef THREADS_H
#define THREADS_H

	void* led_thread(void *arg);
	void* lcd_thread(void *arg);
	void* logic_thread(void *arg);
	void* function_thread(void *arg);
	void* save_thread(void *arg);

#endif /* THREADS_H */

// ============================================================
//  End of File
// ============================================================
