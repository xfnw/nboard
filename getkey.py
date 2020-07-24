#!/usr/bin/env python3
import curses

def main(stdscr):
    while True:
        k = stdscr.getkey()

        if k == '\x1b':
            k=""
            for i in range(5):
                k += stdscr.getkey()


        print(repr(k))



curses.wrapper(main)


