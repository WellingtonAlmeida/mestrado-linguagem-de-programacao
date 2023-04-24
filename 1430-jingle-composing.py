# -*- coding: utf-8 -*-
line = input()
notes = {'W': 1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}
while line != '*':
    measures_ok = 0
    for measure in line.split(sep='/'):
        duration=0.0
        for note in measure:
            duration += notes[note]
        if (duration == 1):
            measures_ok += 1
    print(measures_ok)
    line = input()