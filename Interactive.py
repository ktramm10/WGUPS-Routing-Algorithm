from Hash import HashTable
from datetime import datetime

class InteractiveUI:
    def __init__(self, hashTable : HashTable):
        self.hashTable : HashTable = hashTable
        self.userInput : str = ""
        self.stopListening : bool = False

    def isInputValid(self, userInput):
        try:
            datetime.strptime(userInput, "%H:%M")
            return True
        except ValueError:
            return False

    def listen(self):
        while not self.stopListening:

            self.userInput = input("Input the time you would like to view your"
                                   " packages (format: xx:xx),\n"
                                   " if you don't wish to view the packages"
                                   " type \"x\".")
            if self.userInput == "x":
                self.stopListening = True
            elif self.isInputValid(self.userInput):
                print("The valid time is " + self.userInput)
            else:
                print("Invalid input! Please try again.")
        print("Thank you for using WGUPS!")

    def convertTimeToMinutes(self, time : str):
        pass