# Keith Tramm WGUID: 012273798
import Object
import Hash
import Graph
import Controller

# Initialize Hashtable with 5 "buckets". Buckets will resize when the load factor exceeds 1.5
ht = Hash.HashTable(5)
# Populates the hashtable with package data from WGUPS Package File
ht.populateHashTableData()


# Creates a graph representation of the SLC Downtown Map using an adjacency matrix, and establishes edges using the WGUPS Distance Table data
gr = Graph.RouteGraph()
gr.populate_graph_data()

# Initialize truck objects
truck1 = Object.Truck(0.0, [], 1)
truck2 = Object.Truck(0.0, [], 2)

# Initialize truck controller component
tc = Controller.TruckController(truck1, truck2, ht, gr)
# Deploy Algorithm
tc.optimizeRoute()
# Display full hashtable to verify deliveries
print("Display Packages: ")
for i in range(1,41):
    print("ID: " + i.__str__() + " - Status: " + ht.search(i).delStatus + " - Delivery Deadline: " + ht.search(i).delDeadline)

# Interactable Interface
# TODO: implement an interactable interface that takes user input of time ( 10:00 am ) and display the status of all 40 packages at that time
# idea: convert user input into total minutes value ie 8:00 am = 480 minutes, store time when packages are loaded and delivered within the package object. Upon called the time
# designated by the user we can compare the time with the two stored times to determine if a package was at "HUB", "En Route", or "Delivered" at the given time.
