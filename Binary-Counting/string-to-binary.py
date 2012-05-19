#!/usr/bin/env python

import pymcu
from time import sleep

mb = pymcu.mcuModule()

# which pins will be used for which bit, least significant first.
pins = [1, 2, 3, 4, 5, 6, 7, 8]

# a message.
message = 'Hello world.'
delay = 1.0 

try:
       [[mb.pinHigh(on), mb.pinLow(list(set(pins) - set(on))), sleep(delay)] for on in [[pins[n + 1] for n in range(8) if ord(c) & (1 << n) > 0] for c in message]]
finally:
        mb.pinLow(pins)
        mb.close()
