#!/usr/bin/env python

import pymcu

mb = pymcu.mcuModule()

# There are 8 pins on the input keypad
# The default for the pymcu is digital pins are set to output
# we need to set them to input so we can read from the keypad
for pin in xrange(1, 9):
    mb.digitalState(pin, 'input')
    print pin


# Row 1 (1,2,3,A) pin 8
# Row 2 (4,5,6,B) pin 7
# Row 3 (7,8,9,C) pin 6
# Row 4 (*,0,#,D) pin 5

# Col 1 (1,4,7,*) pin 4
# Col 2 (2,5,8,0) pin 3
# Col 3 (3,6,9,#) pin 2
# Col 4 (A,B,C,D) pin 1

# So if 5 is pressed the pins should be 7, 3

while True:
    for row_pin in xrange(5, 9):
        for col_pin in xrange(1, 5):
            if mb.digitalRead(row_pin) and mb.digitalRead(col_pin):
                print "The pressed row {0} and col {1}".format(row_pin, col_pin)
                print row_pin, col_pin

