import pymcu
import time


class Morse(object):
    DOT = 0.25
    DASH = DOT * 3
    LETTER_SPACE = DOT
    WORD_SPACE = DOT * 7

    #mb = pymcu.mcuModule()

    alphabet = {
        ' ': [WORD_SPACE],
        'a': [DOT, DASH],
        'b': [DASH, DOT, DOT],
        'c': [DASH, DOT, DASH, DOT],
        'e': [DOT],
        'f': [DOT, DOT, DASH, DOT],
        'g': [DASH, DASH, DOT],
        'h': [DOT, DOT, DOT, DOT],
        'i': [DOT, DOT],
        'j': [DOT, DASH, DASH, DASH],
        'k': [DASH, DOT, DASH],
        'l': [DOT, DASH, DOT, DOT],
        'm': [DASH, DASH],
        'n': [DASH, DOT],
        'o': [DASH, DASH, DASH],
        'p': [DOT, DASH, DASH, DOT],
        'q': [DASH, DASH, DOT, DASH],
        'r': [DOT, DASH, DOT],
        's': [DOT, DOT, DOT],
        't': [DASH],
        'u': [DOT, DOT, DASH],
        'v': [DOT, DOT, DOT, DASH],
        'w': [DOT, DASH, DASH],
        'x': [DASH, DOT, DOT, DASH],
        'y': [DASH, DOT, DASH, DASH],
        'z': [DASH, DASH, DOT, DOT],
        '0': [DASH, DASH, DASH, DASH, DASH],
        '1': [DOT, DASH, DASH, DASH, DASH],
        '2': [DOT, DOT, DASH, DASH, DASH],
        '3': [DOT, DOT, DOT, DASH, DASH],
        '4': [DOT, DOT, DOT, DOT, DASH],
        '5': [DOT, DOT, DOT, DOT, DOT],
        '6': [DASH, DOT, DOT, DOT, DOT],
        '7': [DASH, DASH, DOT, DOT, DOT],
        '8': [DASH, DASH, DASH, DOT, DOT],
        '9': [DASH, DASH, DASH, DASH, DOT],
    }

    def __init__(self, word):
        for char in word:
            self.light_on(self.alphabet[char])

    def light_on(self, code):
        for index, duration in enumerate(code):
            #self.mb.pinHigh(1)
            #time.sleep(duration)
            #self.mb.pinLow(1)
            print duration

            try:
                code[index + 1]
                print self.LETTER_SPACE
                #time.sleep(self.LETTER_SPACE)
            except:
                print self.DASH
                #time.sleep(self.DASH)

m = Morse("ab")
