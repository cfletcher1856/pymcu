#!/usr/bin/env python

import pymcu
from time import sleep

mb = pymcu.mcuModule()

pins = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0

try:
    while True:
        for (pin, value) in zip(pins, [int(count & (1 << n) > 0) for n in range(8)]):
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
    mb.close()
