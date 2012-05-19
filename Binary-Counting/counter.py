#!/usr/bin/env python

import pymcu
from time import sleep

mb = pymcu.mcuModule()

num_of_pins = 8
pins = range(1, num_of_pins + 1)
count = 0

try:
    while True:
        for (pin, value) in zip(pins, [int(count & (1 << n) > 0) for n in range(num_of_pins)]):
            high = []
            low = []
            if value:
                high.append(pin)
            else:
                low.append(pin)

            mb.pinHigh(high)
            mb.pinLow(low)

        sleep(0.5)
        count = (count + 1) % 256
except KeyboardInterrupt:
    mb.pinLow(pins)
    mb.close()
