__author__ = 'Taylor'

class Utility:

    def substring(self, string, i1, i2):
        substring = ""

        if len(string) <= 1:
            return string
        if i1 < 0 or i1 > len(string)-1:
            return string
        if i2 < 0 or i2 > len(string)-1:
            return string
        if i2 < i1:
            return string

        for index in range(i1, i2+1, 1):
            substring += string[index]
        return substring

    def reverseString(self, string):
        reverse = ""

        for num in range(len(string)-1, -1, -1):
            reverse += string[num]

        return reverse

    def pigLatin(self, string):
        pig = Utility.substring(self, string, 1, len(string)-1) + string[0] + "ay"
        return pig

