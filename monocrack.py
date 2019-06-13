#!/usr/ibn/python

import string
import collections
import re

def doublelettercrib(text):
    cribs = re.findall(r"(\w)\1+", text)
    print(cribs)

def alphatrans(score, trans, text):
    print("before:\t", score)
    print("after:\t", trans)
    newtext = scoreciphertext.translate(str.maketrans(score, trans))
    return newtext

def charswap(first, secound, string):
    stringlist = list(string)
    stringlist[first], stringlist[secound] = stringlist[secound], stringlist[first]
    return ''.join(stringlist)

if __name__ == '__main__':
    scoretextfile = open('score.txt', 'r') #score.txt is the file the program will score and find cribs
    scoreciphertext = scoretextfile.read()
    alphabet = list(string.ascii_uppercase)
    score = collections.Counter(scoreciphertext)
    scoresum = sum(score.values())
    sortedscore= sorted(score, key=score.get, reverse=True)
    
    for char in sortedscore:
        print(char, '{0:.0%}'.format(score[char]/scoresum))

    transalpha = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    scorealpha = ''.join(sortedscore)

    #print(scoreciphertext.translate(str.maketrans(scorealpha, transalpha)))
    newscoretext = ''
    c = 1
    print(scoreciphertext)
    doublelettercrib(scoreciphertext)

    while c == 1:
        num1 = int(input("Enter position for first charater to swap: "))
        num2 = int(input("Enter secound: "))
        transalpha = charswap(num1-1, num2-1, transalpha)
        newscoretext = alphatrans(scorealpha, transalpha, newscoretext)
