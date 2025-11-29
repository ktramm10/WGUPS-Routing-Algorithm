import math
from logging import exception
class NotAtHubException(Exception):
    pass

class PackageNotOnTruck(Exception):
    pass




class Package:
    def __init__(self, delLocationName : str , delAddress: str, delDeadline: str, delCity: str, delZip: str, weight: float,
                 delStatus: str, packageID : int, priorityRating = 0, timeDelivered : str = "",
                 timeDelMinutes : float = 0, timeLoadedMinutes : float = 0):
        self.delLocationName = delLocationName
        self.delAddress = delAddress
        self.delDeadline = delDeadline
        self.delCity = delCity
        self.delZip = delZip
        self.weight = weight
        self.delStatus = delStatus
        self.packageID = packageID
        self.timeDelivered = timeDelivered
        # Packages are assigned a priority Rating based on the urgency of their delivery based on deadline to improve algorithm decision-making.
        self.priorityRating = priorityRating
        self.timeDelMinutes = timeDelMinutes
        self.timeLoadedMinutes = timeLoadedMinutes

    def __str__(self):
        return  ("Address: " + self.delAddress + " Deadline: " +
                 self.delDeadline) + " City: " +  self.delCity + (" Zip Code: " +
                 self.delZip + " Weight: " + self.weight.__str__() +  " Status: " +
                                                                  self.delStatus)

    def getData(self):
        return [self.delAddress, self.delDeadline, self.delCity, self.delZip,
                self.weight, self.delStatus]

class Truck:
    def __init__(self, distanceTraveledMiles : float, packages : list, truckID : int, isAtHub : bool = True,
                 startTimeMinutes : float = 480, hub : str = "Western Governors University"): # minutes to 8AM is 480
        self.distanceTraveledMiles = distanceTraveledMiles
        self.packages = packages
        self.isAtHub = isAtHub
        self.startTimeMinutes = startTimeMinutes
        self.currentTime = startTimeMinutes
        self.hub = hub
        self.currentLocation = hub
        self.truckID = truckID
        self.packagesDelivered : int = 0



    def loadPackage(self, package : Package):
        if self.isAtHub:
            if package.delStatus != "En Route":
                if self.packages.__len__() < 16:
                    package.delStatus = "En Route"
                    print("Package Loaded - Package ID: " + package.packageID.__str__() + " | Package Status: " + package.delStatus + " | Time Loaded: " +
                          self.get24HourClockTime() + " Onto : Truck #" + self.truckID.__str__())
                    self.packages.append(package)
                    package.timeLoadedMinutes = self.currentTime

                else:
                    raise Exception("Truck is at max capacity, packages must be delivered before more can be loaded")
            else:
                raise Exception("Package is already on a truck and cannot be loaded")
        else:
            raise NotAtHubException("Truck is not currently at the hub and cannot load packages.")

    def deliverPackage(self, package : Package):
        if self.packages.__contains__(package):
            self.packagesDelivered += 1
            self.packages.remove(package)
            package.timeDelivered = self.get24HourClockTime()
            package.timeDelMinutes = self.currentTime
            package.delStatus = "Delivered" + " | " + package.timeDelivered + " | Delivered By Truck #" + self.truckID.__str__()
            print("ID: " + package.packageID.__str__() + " | Time Delivered: " + package.timeDelivered +
                  " Location Delivered: " + package.delLocationName + " | Truck Distance Traveled: " +
                  round(self.distanceTraveledMiles, 2).__str__())
        else:
            raise PackageNotOnTruck("The package that is attempting to be delivered in not currently on the truck.")

    def travelTo(self, location : str, distance : float):
        self.currentLocation = location
        self.distanceTraveledMiles += distance
        self.distanceToTime()

    def distanceToTime(self):
        timePassed = round(self.distanceTraveledMiles / .3, 2) # 18 miles / 60 minutes  = .3 miles per minute.
        self.currentTime = self.startTimeMinutes + timePassed

    def get24HourClockTime(self):
        hours = math.floor(self.currentTime / 60)
        minutes = self.currentTime % 60
        if int(minutes).__str__().__len__() < 2:
            return "" + int(hours).__str__() + ":0" + int(minutes).__str__()
        else:
            return "" + int(hours).__str__() + ":" + int(minutes).__str__()