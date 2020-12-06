# Design and implement a python program that is based on the following
# requirements.  a) define a class which has at least two methods:
# Method 1 - getString: to get a string from console input, and
# Method 2 - printString: to print the string in upper case
# b) demonstrate code works using three different test input strings

class lyrics:
    def __init__(self):
        self.lyric = ''

    def getString(self):
        self.lyric = input()

    def printString(self):
        print(self.lyric.upper())

rick = lyrics()
rick.getString()
rick.printString()

rick2 = lyrics()
rick2.getString()
rick2.printString()

rick3 = lyrics()
rick3.getString()
rick3.printString()
