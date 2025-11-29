import math

from Hash import HashTable
from datetime import datetime

class InteractiveUI:
    def __init__(self, hashTable : HashTable):
        self.hashTable : HashTable = hashTable
        self.isPM: bool = False
        self.stopListening : bool = False
        self.minutes : float = 0.0

    def isInputValid(self, userInput):
        try:
            datetime.strptime(userInput, "%H:%M")
            return True
        except ValueError:
            return False

    def listen(self):
        while not self.stopListening:

            userInputTime = input("Input the time you would like to view your"
                                   " packages (format: xx:xx),\n"
                                   " if you don't wish to view the packages"
                                   " type \"x\".\n")
            if userInputTime == "x":
                self.stopListening = True
            elif self.isInputValid(userInputTime):
                userInputMeridiem = input("Input whether the time is \"AM\" or \"PM\".")
                if userInputMeridiem.lower() == "am" or userInputMeridiem.lower() == "pm":
                    if userInputMeridiem.lower() == "pm":
                        self.isPM = True
                    print("The valid time is " + userInputTime)
                    self.minutes = self.convertTimeToMinutes(userInputTime)
                    print("converted time to minutes: " + self.minutes.__str__())
                    print("24hr clock time: " + self.get24HourClockTime())
                else:
                    print("Invalid input! Please try again.")
        print("Thank you for using WGUPS!")

    def convertTimeToMinutes(self, time : str):
        timeMinutes : float = 0
        # is hours 1 or 2 digits?
        if time.__len__() == 4 :
            timeMinutes += int(time[0]) * 60
            timeMinutes += int(time[2]) * 10 + int(time[3])
        else:
            timeMinutes += (int(time[0]) * 10) * 60 + int(time[1]) * 60
            timeMinutes += (int(time[3]) * 10) + int(time[4])
            # TODO: Fix 12 AM/PM edge case
        if self.isPM:
            if not (779 >= timeMinutes >= 720):
                print("passed 12:00 check")
                timeMinutes += 720
        # if 12 AM
        elif 779 >= timeMinutes >= 720:
            print("is am & 12 time frame")
            timeMinutes += 720

        return timeMinutes

    def get24HourClockTime(self):
        hours = math.floor(self.minutes / 60)
        minutes = self.minutes % 60
        if int(minutes).__str__().__len__() < 2:
            return "" + int(hours).__str__() + ":0" + int(minutes).__str__()
        else:
            return "" + int(hours).__str__() + ":" + int(minutes).__str__()

    def displayPackages(self):
        pass