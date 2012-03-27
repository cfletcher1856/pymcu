import pymcu
from time import sleep


class Morse(object):
    DOT = 1
    DASH = DOT * 3
    SYMBOL_SPACE = DOT
    LETTER_SPACE = DASH
    WORD_SPACE = DOT * 7

    mb = pymcu.mcuModule()

    alphabet = {
        'a': [DOT, DASH],
        'b': [DASH, DOT, DOT],
        'c': [DASH, DOT, DASH, DOT],
        'd': [DASH, DOT, DOT],
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
        '.': [DOT, DASH, DOT, DASH, DOT, DASH],
        ',': [DASH, DASH, DOT, DOT, DASH, DASH],
        '?': [DOT, DOT, DASH, DASH, DOT, DOT],
        "'": [DOT, DASH, DASH, DASH, DASH, DOT],
        '!': [DASH, DOT, DASH, DOT, DASH, DASH],
        '/': [DASH, DOT, DOT, DASH, DOT],
        '(': [DASH, DOT, DASH, DASH, DOT],
        ')': [DASH, DOT, DASH, DASH, DOT, DASH],
        '&': [DOT, DASH, DOT, DOT, DOT],
        ':': [DASH, DASH, DASH, DOT, DOT, DOT],
        ';': [DASH, DOT, DASH, DOT, DASH, DOT],
        '=': [DASH, DOT, DOT, DOT, DASH],
        '+': [DOT, DASH, DOT, DASH, DOT],
        '-': [DASH, DOT, DOT, DOT, DOT, DASH],
        '_': [DOT, DOT, DASH, DASH, DOT, DASH],
        '"': [DOT, DASH, DOT, DOT, DASH, DOT],
        '$': [DOT, DOT, DOT, DASH, DOT, DOT, DASH],
        '@': [DOT, DASH, DASH, DOT, DASH, DOT],
    }

    def __init__(self, word, wpm=13):
        self.speed = (1200 / wpm) / 1000.0
        word_len = len(word)
        for ctr, char in enumerate(word, start=1):
            char = char.lower()
            if char != " ":
                try:
                    if ctr < word_len and word[ctr] != " ":
                        self.light_on(self.alphabet[char], False)
                    else:
                        self.light_on(self.alphabet[char], True)
                except KeyError:
                    print "This char has not been implemented yet {0}".format(char)
                    return

    def light_on(self, code, end_of_word):
        code_len = len(code)
        for ctr, duration in enumerate(code, start=1):
            self.mb.pinHigh(1)
            sleep(duration * self.speed)
            self.mb.pinLow(1)

            if ctr < code_len:
                sleep(self.SYMBOL_SPACE * self.speed)

        if end_of_word:
            sleep(self.WORD_SPACE * self.speed)
        else:
            sleep(self.LETTER_SPACE * self.speed)


m = Morse("Morse Code!!")
