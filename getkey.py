#!/usr/bin/env python3
import curses

def main(stdscr):
    while True:
        k = stdscr.getkey()
        print(repr(k))



curses.wrapper(main)


