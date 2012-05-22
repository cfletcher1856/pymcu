import pymcu
import time

mb = pymcu.mcuModule()

while 1:
    lux = mb.readAnalog(1)
    print "lux: {0}"
    time.sleep(1)
