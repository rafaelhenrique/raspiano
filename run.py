# -*- coding: utf-8 -*-
import time
import sys
import math

import pingo

try:
    print("Loading board...")
    board = pingo.detect.get_board()
    print("Its ok...")
except Exception as e:
    print("Error on get_board: {}".format(e))
    sys.exit(1)

buzzer = board.pins[12]
buzzer.mode = pingo.OUT


def play_tone(tone, duration):
    index = 0
    while(index < duration * 1000):
        print(duration * 1000)
        print(index)
        print("")
        buzzer.hi()
        time.sleep(tone / 1000000.)
        buzzer.low()
        time.sleep(tone / 1000000.)
        index += tone * 2

def play_note(note, duration):
    tones = {'c': 1915, 'd': 1700, 'e': 1519, 'f': 1432, 'g': 1275,
             'a': 1136, 'b': 1014, 'C': 956}
    play_tone(tones[note], duration)


if __name__ == "__main__":
    notes = "ccggaagffeeddc "
    beats = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4]
    tempo = 250

    for index in range(len(notes)):
        note = notes[index]
        beat = beats[index]
        if note == ' ':
            time.sleep(beat * tempo)
        else:
            play_note(note, beat * tempo)

        time.sleep((tempo/1000.) / 2.)
        print("--------------Nota {}".format(note))

