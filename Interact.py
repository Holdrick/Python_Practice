__author__ = 'Taylor'

from Utility import Utility

class Interact:
    utility = Utility()

    def displayMenu(self):
        print("1: Reverse a string")
        print("2: Convert a word to pig latin")
        print("q: Quit")
        self.option = input("\nEnter an option: ")

    def doReverse(self):
        string = input("Enter word to reverse: ")
        reverse = Interact.utility.reverseString(string)
        print(string, "reversed:", reverse, "\n")

    def doPigLatin(self):
        string = input("Enter word to convert: ")
        pig = Interact.utility.pigLatin(string)
        print(string, "converted to pig latin:", pig, "\n")

interact = Interact()
done = False

while done != True:
    interact.displayMenu()
    if interact.option == '1':
        interact.doReverse()
    elif interact.option == '2':
        interact.doPigLatin()
    elif interact.option == 'q':
        done = True



