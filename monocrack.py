#!/usr/ibn/python

import string
import collections

transalpha = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

scoretextfile = open('score.txt', 'r') #score.txt is the file the program will score and find cribs
scoreciphertext = scoretextfile.read()
alphabet = list(string.ascii_uppercase)
score = collections.Counter(scoreciphertext)
scoresum = sum(score.values())
sortedscore= sorted(score, key=score.get, reverse=True)

for char in sortedscore:
    print(char, score[char],'\t{0:.0%}'.format(score[char]/scoresum))


