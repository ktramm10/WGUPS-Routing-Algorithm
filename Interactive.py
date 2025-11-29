import math

from Hash import HashTable
from datetime import datetime


class InteractiveUI:
    def __init__(self, hashTable: HashTable):
        self.hashTable: HashTable = hashTable
        self.isPM: bool = False
        self.stopListening: bool = False
        self.minutes: float = 0.0

    def isInputValid(self, userInput):
        # check if user input is valid time
        try:
            datetime.strptime(userInput, "%H:%M")
            return True
        except ValueError:
            return False

    def listen(self):
        # repeat program while flag variable is false
        while not self.stopListening:
            # reset member variables for subsequent time lookups
            self.minutes = 0.0
            self.isPM = False
            # take user input
            userInputTime = input("\nInput the time you would like to view your"
                                  " packages (format: xx:xx),\n"
                                  "if you don't wish to view the packages"
                                  " type \"x\".\n")
            # set flag to cancel
            if userInputTime == "x":
                self.stopListening = True
            # validate user input
            elif self.isInputValid(userInputTime):
                # request meridiem ie. AM or PM
                userInputMeridiem = input("Input whether the time is \"AM\" or \"PM\".\n")
                # Validate meridiem
                if userInputMeridiem.lower() == "am" or userInputMeridiem.lower() == "pm":
                    # set flag for meridiem
                    if userInputMeridiem.lower() == "pm":
                        self.isPM = True
                    # calculate minutes value for comparison and display results
                    self.minutes = self.convertTimeToMinutes(userInputTime)
                    self.displayPackages()
                # Invalid input given, try again
                else:
                    print("Invalid input! Please try again.")
        # end program
        print("Thank you for using WGUPS!")

    def convertTimeToMinutes(self, time: str):
        timeMinutes: float = 0
        # is hours 1 or 2 digits?
        if time.__len__() == 4:
            # multiple hours by 60 and add to total
            timeMinutes += int(time[0]) * 60
            # add minutes to total
            timeMinutes += int(time[2]) * 10 + int(time[3])
        else:
            # multiply 2 digit hour by 60
            timeMinutes += (int(time[0]) * 10) * 60 + int(time[1]) * 60
            # add minutes to total
            timeMinutes += (int(time[3]) * 10) + int(time[4])
        # if meridiem is set to PM add 720 minutes
        if self.isPM:
            if not (779 >= timeMinutes >= 720):
                timeMinutes += 720
        # handle 12 AM/PM edge-case
        elif 779 >= timeMinutes >= 720:
            timeMinutes += 720

        return timeMinutes

    # convert minute value into military time
    def get24HourClockTime(self, totalMinutes):
        hours = math.floor(totalMinutes / 60)
        minutes = totalMinutes % 60
        if int(minutes).__str__().__len__() < 2:
            return "" + int(hours).__str__() + ":0" + int(minutes).__str__()
        else:
            return "" + int(hours).__str__() + ":" + int(minutes).__str__()

    # display all packages at the time that was input by the user
    def displayPackages(self):
        # print header
        header = ("\nPackages Status @ " + self.get24HourClockTime(self.minutes))
        if self.isPM:
            header += " PM:"
        else:
            header += " AM:"
        print(header)

        # iterate through packages
        for i in range(1, 41):
            package = self.hashTable.search(i)
            tempStatus = "HUB"
            # compare minute values for loading time and delivery to determine the temporary status of the package
            if 0 < package.timeLoadedMinutes <= self.minutes:
                tempStatus = "En Route"
                if self.minutes >= package.timeDelMinutes:
                    tempStatus = "Delivered"

            # format output based on package status
            output = ("ID: " + package.packageID.__str__() + " | Status: " + tempStatus + " | Address: " + package.delAddress + " | Deadline: " +
                      package.delDeadline)
            if tempStatus == "En Route" or tempStatus == "Delivered":
                output += " | Truck No.: " + package.truckNumber
            else:
                output += " | Truck No.: Null"
            if tempStatus == "Delivered":
                output += " | Time Delivered: " + package.timeDelivered
            else:
                output += " | Time Delivered: Null"
            print(output)