from Graph import RouteGraph
from Hash import HashTable
from Object import Truck, Package


class TruckController:
    def __init__(self, truck1 : Truck, truck2 : Truck, hashtable : HashTable, graph : RouteGraph):
        self.truck1 = truck1
        self.truck2 = truck2
        self.hashTable = hashtable
        self.graph = graph
        self.allPackagesDispatched = False

    def optimizeRoute(self):
        trucks = [self.truck1, self.truck2]
        print("Day Started! \n")
        # Load trucks with packages
        self.t1FirstLoad()
        self.t2FirstLoad()
        for truck in trucks:
            print("\nTruck #" + truck.truckID.__str__() + " Runtime:")
            while truck.packages.__len__() > 7: # Deliver the first 7 packages before returning to hub
                # use algorithm to determine the optimal next package to deliver
                packageSelected = self.findNextLocation(truck)

                # send truck to location and deliver the package
                truck.travelTo(packageSelected.delLocationName, self.graph.get_weight(truck.currentLocation, packageSelected.delLocationName))
                truck.deliverPackage(packageSelected)
            # return truck to hub for second load of packages
            print("\nTruck Returning To Hub For More Packages!!")
            truck.travelTo(truck.hub, self.graph.get_weight(truck.currentLocation, truck.hub))
            print("Arrives and Loads at: " + truck.get24HourClockTime())
            self.secondaryLoad1(truck)
            print("\n")

            # redeploy algorithm and continue deliveries
            while truck.packages.__len__() > 0:
                if truck.currentTime > 620 and not self.allPackagesDispatched: # once final package has arrived at hub have truck #1 collect it
                    print("\n Truck Returning to Hub for more packages!!\n")
                    truck.travelTo(truck.hub, self.graph.get_weight(truck.currentLocation, truck.hub))
                    self.finalPackage(truck)

                packageSelected = self.findNextLocation(truck)
                truck.travelTo(packageSelected.delLocationName, self.graph.get_weight(truck.currentLocation, packageSelected.delLocationName))
                truck.deliverPackage(packageSelected)
            # display distance traveled for this truck and notify that its work is complete
            print("Truck Distance Traveled",round(truck.distanceTraveledMiles), "Miles!")
            print("Truck Complete!\n")
            # final display
        print("Day Complete!")
        print("Total Distance Traveled by Both Trucks: " + round(self.truck1.distanceTraveledMiles + self.truck2.distanceTraveledMiles).__str__() + " Miles")
        print("Packages Delivered by Truck #1: " + self.truck1.packagesDelivered.__str__())
        print("Packages Delivered by Truck #2: " + self.truck2.packagesDelivered.__str__())
        print("\n")


    def findNextLocation(self, truck):
        bestChoice : Package # local variable that holds best package to deliver next
        nearestNeighborDistance : float = -1 # float value that holds the closest distance to the trucks current location
        for package in truck.packages: # iterate over packages in truck
            # if first iteration set vars to first package
            if nearestNeighborDistance < 0:
                nearestNeighborDistance = self.graph.get_weight(truck.currentLocation, package.delLocationName)
                bestChoice = package
            # deadline takes priority over proximity so prioritize priority rating during selection
            elif package.priorityRating > bestChoice.priorityRating:
                nearestNeighborDistance = self.graph.get_weight(truck.currentLocation, package.delLocationName)
                bestChoice = package
            # if packages have the same priority rating select based on distance
            elif package.priorityRating == bestChoice.priorityRating and self.graph.get_weight(truck.currentLocation, package.delLocationName) < nearestNeighborDistance:
                nearestNeighborDistance = self.graph.get_weight(truck.currentLocation, package.delLocationName)
                bestChoice = package
        # return the package that should be delivered next
        return bestChoice

    def t1FirstLoad(self):
        self.truck1.loadPackage(self.hashTable.search(15))
        self.truck1.loadPackage(self.hashTable.search(13))
        self.truck1.loadPackage(self.hashTable.search(14))
        self.truck1.loadPackage(self.hashTable.search(1))
        self.truck1.loadPackage(self.hashTable.search(16))
        self.truck1.loadPackage(self.hashTable.search(19))
        self.truck1.loadPackage(self.hashTable.search(20))
        self.truck1.loadPackage(self.hashTable.search(8))
        self.truck1.loadPackage(self.hashTable.search(31))
        self.truck1.loadPackage(self.hashTable.search(34))
        self.truck1.loadPackage(self.hashTable.search(21))
        self.truck1.loadPackage(self.hashTable.search(11))
        self.truck1.loadPackage(self.hashTable.search(10))
        self.truck1.loadPackage(self.hashTable.search(22))
        self.truck1.loadPackage(self.hashTable.search(33))
        self.truck1.loadPackage(self.hashTable.search(26))

    def t2FirstLoad(self):
        self.truck2.loadPackage(self.hashTable.search(3))
        self.truck2.loadPackage(self.hashTable.search(2))
        self.truck2.loadPackage(self.hashTable.search(4))
        self.truck2.loadPackage(self.hashTable.search(5))
        self.truck2.loadPackage(self.hashTable.search(7))
        self.truck2.loadPackage(self.hashTable.search(40))
        self.truck2.loadPackage(self.hashTable.search(18))
        self.truck2.loadPackage(self.hashTable.search(36))
        self.truck2.loadPackage(self.hashTable.search(38))
        self.truck2.loadPackage(self.hashTable.search(29))
        self.truck2.loadPackage(self.hashTable.search(30))
        self.truck2.loadPackage(self.hashTable.search(37))
        self.truck2.loadPackage(self.hashTable.search(12))
        self.truck2.loadPackage(self.hashTable.search(23))
        self.truck2.loadPackage(self.hashTable.search(24))
        self.truck2.loadPackage(self.hashTable.search(39))

    def secondaryLoad1(self, truck):
        if self.hashTable.search(6).delStatus == "HUB":
            truck.loadPackage(self.hashTable.search(6))
            truck.loadPackage(self.hashTable.search(28))
            truck.loadPackage(self.hashTable.search(27))
            truck.loadPackage(self.hashTable.search(35))
        else:
            self.secondaryLoad2(truck)

    def secondaryLoad2(self, truck):
        truck.loadPackage(self.hashTable.search(25))
        truck.loadPackage(self.hashTable.search(32))
        truck.loadPackage(self.hashTable.search(17))

    def finalPackage(self, truck):
        if self.hashTable.search(9).delStatus == "HUB":
            truck.loadPackage(self.hashTable.search(9))
            print("\n")
            self.allPackagesDispatched = True
        else:
            return