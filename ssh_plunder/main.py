#!/usr/bin/python

"""
Lyle Scott, III
lyle@digitalfoo.net
A simple demo that uses curses to scroll the terminal.
"""
import curses
import sys
import random
import time


class MenuDemo:
    DOWN = 1
    UP = -1
    SPACE_KEY = 32
    ESC_KEY = 27

    PREFIX_SELECTED = '_X_'
    PREFIX_DESELECTED = '___'

    outputLines = []
    screen = None
            
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1) 
        self.screen.border(0)
        self.topLineNum = 0
        self.highlightLineNum = 0
        self.markedLineNums = []
        self.getOutputLines()
        self.run()
        
    def run(self):
        while True:
            self.displayScreen()
            time.sleep(0.03)
            self.updown(self.DOWN)

    def markLine(self):
        linenum = self.topLineNum + self.highlightLineNum
        if linenum in self.markedLineNums:
            self.markedLineNums.remove(linenum)
        else:
            self.markedLineNums.append(linenum)

    def getOutputLines(self):
        ### !!!
        ### This is where you would write a function to parse lines into rows 
        ### and columns. For this demo, I'll just create a bunch of random ints
        ### !!!
        self.outputLines = [x.strip() for x in open('/lines.txt').readlines()]
        self.nOutputLines = len(self.outputLines)

    def displayScreen(self):
        # clear screen
	# print "here"
        self.screen.erase()

        # now paint the rows
        top = self.topLineNum
        bottom = self.topLineNum+curses.LINES
        for (index,line,) in enumerate(self.outputLines[top:bottom]):
            linenum = self.topLineNum + index
            if linenum in self.markedLineNums:
                prefix = self.PREFIX_SELECTED
            else:
                prefix = self.PREFIX_DESELECTED

            line = '%s %s' % (prefix, line,)

            # highlight current line            
            if index != self.highlightLineNum:
                self.screen.addstr(index, 0, line)
            else:
                self.screen.addstr(index, 0, line, curses.A_BOLD)
        self.screen.refresh()

    # move highlight up/down one line
    def updown(self, increment):
        nextLineNum = self.highlightLineNum + increment

        # paging
        if increment == self.UP and self.highlightLineNum == 0 and self.topLineNum != 0:
            self.topLineNum += self.UP 
            return
        elif increment == self.DOWN and nextLineNum == curses.LINES and (self.topLineNum+curses.LINES) != self.nOutputLines:
            self.topLineNum += self.DOWN
            return

        # scroll highlight line
        if increment == self.UP and (self.topLineNum != 0 or self.highlightLineNum != 0):
            self.highlightLineNum = nextLineNum
        elif increment == self.DOWN and (self.topLineNum+self.highlightLineNum+1) != self.nOutputLines and self.highlightLineNum != curses.LINES:
            self.highlightLineNum = nextLineNum
 
    def restoreScreen(self):
        curses.initscr()
        curses.nocbreak()
        curses.echo()
        curses.endwin()
    
    # catch any weird termination situations
    def __del__(self):
        self.restoreScreen()

     
if __name__ == '__main__':
    ih = MenuDemo()

