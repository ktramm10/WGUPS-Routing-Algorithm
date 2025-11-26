class NameNotFoundError(Exception):
    pass
class Location:
    def __init__(self, name : str, address : str, zipcode : str):
        self.name = name
        self.address = address
        self.zipcode = zipcode

    def __str__(self):
        return "Name: " + self.name + " | Address: " + self.address + (" | "
                                            + "Zipcode: ") + self.zipcode

class RouteGraph:
    def __init__(self):
        self.locations =  []
        self.locToIndex = {}
        self.adjMatrix  = []

    def addNode(self, name : str, address : str, zipcode : str):
        if name not in self.locToIndex:
            self.locations.append(Location(name, address, zipcode))
            self.locToIndex[name] = len(self.locations) - 1

            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append([0] * len(self.locations))

    def addEdge(self, node1Name : str, node2Name : str, weight : float):
        if node1Name and node2Name in self.locToIndex:
            idx1 = self.locToIndex[node1Name]
            idx2 = self.locToIndex[node2Name]

            self.adjMatrix[idx1][idx2] = weight
            self.adjMatrix[idx2][idx1] = weight
        else:
            raise NameNotFoundError("Node name 1 or 2 was not found in "
                                    "dictionary \"locToIndex\".")

    def get_weight(self, node1Name : str, node2Name : str):
        if node1Name and node2Name not in self.locToIndex:
            raise NameNotFoundError("Node name 1 or 2 was not found in "
                                    "dictionary \"locToIndex\". node 1 : " + node1Name + ", " + node2Name)
        else:
            idx1 =  self.locToIndex[node1Name]
            idx2 = self.locToIndex[node2Name]
            return self.adjMatrix[idx1][idx2]

    def print_graph(self):
        print("Locations: ")
        for value in self.locations:
            print(value)
        print("Adjacency Matrix: ")
        for value in self.adjMatrix:
            print(value)

    def populate_graph_data(gr):
        # insert locations into graph
        gr.addNode("Western Governors University", "4001 South 700 East", "84107")
        gr.addNode("International Peace Gardens", "1060 Dalton Ave S", "84104")
        gr.addNode("Sugar House Park", "1330 2100 S", "84106")
        gr.addNode("Taylorsville-Bennion Heritage City Gov Off", "1488 4800 S", "84123")
        gr.addNode("Salt Lake City Division of Health Services", "177 W Price Ave",
                   "84115")
        gr.addNode("South Salt Lake Public Works", "195 W Oakland Ave", "84115")
        gr.addNode("Salt Lake City Streets and Sanitation", "2010 W 500 S", "84104")
        gr.addNode("Deker Lake", "2300 Parkway Blvd", "84119")
        gr.addNode("Salt Lake City Ottinger Hall", "233 Canyon Rd", "84103")
        gr.addNode("Columbus Library", "2530 S 500 E", "84106")
        gr.addNode("Taylorsville City Hall", "2600 Taylorsville Blvd", "84118")
        gr.addNode("South Salt Lake Police", "2835 Main St", "84115")
        gr.addNode("Council Hall", "300 State St", "84103")
        gr.addNode("Redwood Park", "3060 Lester St", "84119")
        gr.addNode("Salt Lake County Mental Health", "3148 S 1100 W", "84119")
        gr.addNode("Salt Lake County/United Police Dept", "3365 S 900 W", "84119")
        gr.addNode("West Valley Prosecutor", " 3575 W Valley Central Station bus "
                                             "Loop",  "84119")
        gr.addNode("Housing Auth. of Salt Lake County", "3595 Main St", "84115")
        gr.addNode("Utah DMV Administrative Office", "380 W 2880 S", "84115")
        gr.addNode("Third District Juvenile Court", "410 S State St", "84111")
        gr.addNode("Cottonwood Regional Softball Complex", "4300 S 1300 E", "84117")
        gr.addNode("Holiday City Office", "4580 S 2300 E", "84117")
        gr.addNode("Murray City Museum", "5025 State St", "84107")
        gr.addNode("Valley Regional Softball Complex", "5100 South 2700 West", "84118")
        gr.addNode("City Center of Rock Springs", "5383 South 900 East #104", "84117")
        gr.addNode("Rice Terrace Pavilion Park", "600 E 900 South", "84105")
        gr.addNode("Wheeler Historic Farm", "6351 South 900 East", "84121")

        # create edges weighted with travel distance between locations
        # WGU routes
        gr.addEdge("Western Governors University", "International Peace Gardens", 7.2)
        gr.addEdge("Western Governors University", "Sugar House Park", 3.8)
        gr.addEdge("Western Governors University", "Taylorsville-Bennion Heritage "
                                                   "City Gov Off", 11.0 )
        gr.addEdge("Western Governors University", "Salt Lake City Division of Health Services", 2.2 )
        gr.addEdge("Western Governors University", "South Salt Lake Public Works",  3.5)
        gr.addEdge("Western Governors University", "Salt Lake City Streets and "
                                                   "Sanitation", 10.9 )
        gr.addEdge("Western Governors University", "Deker Lake", 8.6)
        gr.addEdge("Western Governors University", "Salt Lake City Ottinger Hall", 7.6)
        gr.addEdge("Western Governors University", "Columbus Library", 2.8)
        gr.addEdge("Western Governors University", "Taylorsville City Hall", 6.4)
        gr.addEdge("Western Governors University", "South Salt Lake Police", 3.2)
        gr.addEdge("Western Governors University", "Council Hall", 7.6)
        gr.addEdge("Western Governors University", "Redwood Park", 5.2)
        gr.addEdge("Western Governors University", "Salt Lake County Mental Health",
                   4.4 )
        gr.addEdge("Western Governors University", "Salt Lake County/United Police "
                                                   "Dept", 3.7)
        gr.addEdge("Western Governors University", "West Valley Prosecutor", 7.6)
        gr.addEdge("Western Governors University", "Housing Auth. of Salt Lake "
                                                   "County", 2.0)
        gr.addEdge("Western Governors University", "Utah DMV Administrative Office",
                   3.6)
        gr.addEdge("Western Governors University", "Third District Juvenile Court", 6.5)
        gr.addEdge("Western Governors University", "Cottonwood Regional Softball "
                                                   "Complex", 1.9)
        gr.addEdge("Western Governors University", "Holiday City Office", 3.4)
        gr.addEdge("Western Governors University", "Murray City Museum", 2.4)
        gr.addEdge("Western Governors University", "Valley Regional Softball "
                                                   "Complex", 6.4)
        gr.addEdge("Western Governors University", "City Center of Rock Springs", 2.4)
        gr.addEdge("Western Governors University", "Rice Terrace Pavilion Park", 5.0)
        gr.addEdge("Western Governors University", "Wheeler Historic Farm", 3.6)

        # International Peace Gardens Routes
        gr.addEdge("International Peace Gardens", "Sugar House Park", 7.1)
        gr.addEdge("International Peace Gardens", "Taylorsville-Bennion Heritage City Gov Off", 6.4)
        gr.addEdge("International Peace Gardens", "Salt Lake City Division of Health Services", 6.0)
        gr.addEdge("International Peace Gardens", "South Salt Lake Public Works", 4.8)
        gr.addEdge("International Peace Gardens", "Salt Lake City Streets and Sanitation", 1.6)
        gr.addEdge("International Peace Gardens", "Deker Lake", 2.8)
        gr.addEdge("International Peace Gardens", "Salt Lake City Ottinger Hall", 4.8)
        gr.addEdge("International Peace Gardens", "Columbus Library", 6.3)
        gr.addEdge("International Peace Gardens", "Taylorsville City Hall", 7.3)
        gr.addEdge("International Peace Gardens", "South Salt Lake Police", 5.3)
        gr.addEdge("International Peace Gardens", "Council Hall", 4.8)
        gr.addEdge("International Peace Gardens", "Redwood Park", 3.0)
        gr.addEdge("International Peace Gardens", "Salt Lake County Mental Health", 4.6)
        gr.addEdge("International Peace Gardens", "Salt Lake County/United Police Dept", 4.5)
        gr.addEdge("International Peace Gardens", "West Valley Prosecutor", 7.4)
        gr.addEdge("International Peace Gardens", "Housing Auth. of Salt Lake County", 6.0)
        gr.addEdge("International Peace Gardens", "Utah DMV Administrative Office", 5.0)
        gr.addEdge("International Peace Gardens", "Third District Juvenile Court", 4.8)
        gr.addEdge("International Peace Gardens", "Cottonwood Regional Softball Complex", 9.5)
        gr.addEdge("International Peace Gardens", "Holiday City Office", 10.9)
        gr.addEdge("International Peace Gardens", "Murray City Museum", 8.3)
        gr.addEdge("International Peace Gardens", "Valley Regional Softball Complex", 6.9)
        gr.addEdge("International Peace Gardens", "City Center of Rock Springs", 10.0)
        gr.addEdge("International Peace Gardens", "Rice Terrace Pavilion Park", 4.4)
        gr.addEdge("International Peace Gardens", "Wheeler Historic Farm", 13.0)

        # Sugar House Park Routes
        gr.addEdge("Sugar House Park", "Taylorsville-Bennion Heritage City Gov Off",
                   9.2)
        gr.addEdge("Sugar House Park", "Salt Lake City Division of Health Services",
                   4.4)
        gr.addEdge("Sugar House Park", "South Salt Lake Public Works", 2.8)
        gr.addEdge("Sugar House Park", "Salt Lake City Streets and Sanitation", 8.6)
        gr.addEdge("Sugar House Park", "Deker Lake", 6.3)
        gr.addEdge("Sugar House Park", "Salt Lake City Ottinger Hall", 5.3)
        gr.addEdge("Sugar House Park", "Columbus Library", 1.6)
        gr.addEdge("Sugar House Park", "Taylorsville City Hall", 10.4)
        gr.addEdge("Sugar House Park", "South Salt Lake Police", 3.0)
        gr.addEdge("Sugar House Park", "Council Hall", 5.3)
        gr.addEdge("Sugar House Park", "Redwood Park", 6.5)
        gr.addEdge("Sugar House Park", "Salt Lake County Mental Health", 5.6)
        gr.addEdge("Sugar House Park", "Salt Lake County/United Police Dept", 5.8)
        gr.addEdge("Sugar House Park", "West Valley Prosecutor", 5.7)
        gr.addEdge("Sugar House Park", "Housing Auth. of Salt Lake County", 4.1)
        gr.addEdge("Sugar House Park", "Utah DMV Administrative Office", 3.6)
        gr.addEdge("Sugar House Park", "Third District Juvenile Court", 4.3)
        gr.addEdge("Sugar House Park", "Cottonwood Regional Softball Complex", 3.3)
        gr.addEdge("Sugar House Park", "Holiday City Office", 5.0)
        gr.addEdge("Sugar House Park", "Murray City Museum", 6.1)
        gr.addEdge("Sugar House Park", "Valley Regional Softball Complex", 9.7)
        gr.addEdge("Sugar House Park", "City Center of Rock Springs", 6.1)
        gr.addEdge("Sugar House Park", "Rice Terrace Pavilion Park", 2.8)
        gr.addEdge("Sugar House Park", "Wheeler Historic Farm", 7.4)

        # Taylorsville-Bennion Heritage City Gov Off Routes
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Salt Lake City "
                                                                  "Division of Health Services", 5.6)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "South Salt Lake "
                                                                  "Public Works", 6.9)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Salt Lake City "
                                                                  "Streets and "
                                                                  "Sanitation", 8.6)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Deker Lake", 4.0)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Salt Lake City "
                                                                  "Ottinger Hall", 11.1)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Columbus Library",
                   7.3)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Taylorsville City "
                                                                  "Hall", 1.0)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "South Salt Lake "
                                                                  "Police", 6.4)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Council Hall", 11.1)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Redwood Park", 3.9)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Salt Lake County "
                                                                  "Mental Health", 4.3)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Salt Lake "
                                                                  "County/United "
                                                                  "Police Dept", 4.4)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "West Valley "
                                                                  "Prosecutor", 7.2)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Housing Auth. of "
                                                                  "Salt Lake County",
                   5.3)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Utah DMV "
                                                                  "Administrative "
                                                                  "Office", 6.0)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Third District "
                                                                  "Juvenile Court",
                   10.6)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Cottonwood "
                                                                  "Regional Softball "
                                                                  "Complex", 5.9)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Holiday City "
                                                                  "Office", 7.4)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Murray City "
                                                                  "Museum", 4.7)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Valley Regional "
                                                                  "Softball Complex",
                   0.6)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "City Center of "
                                                                  "Rock Springs", 6.4)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Rice Terrace "
                                                                  "Pavilion Park", 10.1)
        gr.addEdge("Taylorsville-Bennion Heritage City Gov Off",  "Wheeler Historic "
                                                                  "Farm", 10.1)
        # Salt Lake City Division of Health Services Routes:
        gr.addEdge("Salt Lake City Division of Health Services", "South Salt Lake "
                                                                 "Public Works", 1.9)
        gr.addEdge("Salt Lake City Division of Health Services", "Salt Lake City "
                                                                 "Streets and "
                                                                 "Sanitation", 7.9)
        gr.addEdge("Salt Lake City Division of Health Services", "Deker Lake", 5.1)
        gr.addEdge("Salt Lake City Division of Health Services", "Salt Lake City Ottinger Hall",
                   7.5)
        gr.addEdge("Salt Lake City Division of Health Services", "Columbus Library", 2.6)
        gr.addEdge("Salt Lake City Division of Health Services", "Taylorsville City "
                                                                 "Hall", 6.5)
        gr.addEdge("Salt Lake City Division of Health Services", "South Salt Lake "
                                                                 "Police", 1.5)
        gr.addEdge("Salt Lake City Division of Health Services", "Council Hall", 7.5)
        gr.addEdge("Salt Lake City Division of Health Services", "Redwood Park", 3.2)
        gr.addEdge("Salt Lake City Division of Health Services", "Salt Lake County "
                                                                 "Mental Health", 2.4)
        gr.addEdge("Salt Lake City Division of Health Services", "Salt Lake "
                                                                 "County/United "
                                                                 "Police Dept", 2.7)
        gr.addEdge("Salt Lake City Division of Health Services", "West Valley "
                                                                 "Prosecutor",1.4 )
        gr.addEdge("Salt Lake City Division of Health Services", "Housing Auth. of "
                                                                 "Salt Lake County",
                   0.5)
        gr.addEdge("Salt Lake City Division of Health Services", "Utah DMV "
                                                                 "Administrative "
                                                                 "Office", 1.7)
        gr.addEdge("Salt Lake City Division of Health Services", "Third District "
                                                                 "Juvenile Court", 6.5)
        gr.addEdge("Salt Lake City Division of Health Services", "Cottonwood Regional Softball Complex", 3.2)
        gr.addEdge("Salt Lake City Division of Health Services", "Holiday City "
                                                                 "Office", 5.2)
        gr.addEdge("Salt Lake City Division of Health Services", "Murray City "
                                                                 "Museum", 2.5)
        gr.addEdge("Salt Lake City Division of Health Services", "Valley Regional "
                                                                 "Softball Complex",
                   6.0)
        gr.addEdge("Salt Lake City Division of Health Services", "City Center of Rock Springs", 4.2)
        gr.addEdge("Salt Lake City Division of Health Services", "Rice Terrace "
                                                                 "Pavilion Park", 5.4)
        gr.addEdge("Salt Lake City Division of Health Services", "Wheeler Historic "
                                                                 "Farm", 5.5)

        # South Salt Lake Public Works Routes
        gr.addEdge("South Salt Lake Public Works", "Salt Lake City Streets and "
                                                   "Sanitation", 6.3)
        gr.addEdge("South Salt Lake Public Works", "Deker Lake", 4.3)
        gr.addEdge("South Salt Lake Public Works", "Salt Lake City Ottinger Hall", 4.5)
        gr.addEdge("South Salt Lake Public Works", "Columbus Library", 1.5)
        gr.addEdge("South Salt Lake Public Works", "Taylorsville City Hall", 8.7)
        gr.addEdge("South Salt Lake Public Works", "South Salt Lake Police", 0.8)
        gr.addEdge("South Salt Lake Public Works", "Council Hall", 4.5)
        gr.addEdge("South Salt Lake Public Works", "Redwood Park", 3.9)
        gr.addEdge("South Salt Lake Public Works", "Salt Lake County Mental Health",
                   3.0)
        gr.addEdge("South Salt Lake Public Works", "Salt Lake County/United Police "
                                                   "Dept", 3.8)
        gr.addEdge("South Salt Lake Public Works", "West Valley Prosecutor", 5.7)
        gr.addEdge("South Salt Lake Public Works", "Housing Auth. of Salt Lake "
                                                   "County", 1.9)
        gr.addEdge("South Salt Lake Public Works", "Utah DMV Administrative Office",
                   1.1)
        gr.addEdge("South Salt Lake Public Works", "Third District Juvenile Court", 3.5)
        gr.addEdge("South Salt Lake Public Works", "Cottonwood Regional Softball "
                                                   "Complex", 4.9)
        gr.addEdge("South Salt Lake Public Works", "Holiday City Office", 6.9)
        gr.addEdge("South Salt Lake Public Works", "Murray City Museum", 4.2)
        gr.addEdge("South Salt Lake Public Works", "Valley Regional Softball "
                                                   "Complex", 9.0)
        gr.addEdge("South Salt Lake Public Works", "City Center of Rock Springs", 5.9)
        gr.addEdge("South Salt Lake Public Works", "Rice Terrace Pavilion Park", 3.5)
        gr.addEdge("South Salt Lake Public Works", "Wheeler Historic Farm", 7.2)

        # Salt Lake City Streets and Sanitation Routes
        gr.addEdge("Salt Lake City Streets and Sanitation", "Deker Lake", 4.0)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Salt Lake City Ottinger Hall", 4.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Columbus Library", 8.0)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Taylorsville City Hall", 8.6)
        gr.addEdge("Salt Lake City Streets and Sanitation", "South Salt Lake Police", 6.9)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Council Hall", 4.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Redwood Park", 4.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Salt Lake County Mental Health", 8.0)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Salt Lake County/United Police Dept", 5.8)
        gr.addEdge("Salt Lake City Streets and Sanitation", "West Valley Prosecutor", 7.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Housing Auth. of Salt Lake County", 7.7)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Utah DMV Administrative Office", 6.6)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Third District Juvenile Court", 3.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Cottonwood Regional Softball Complex", 11.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Holiday City Office", 12.7)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Murray City Museum", 10.0)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Valley Regional Softball Complex", 8.2)
        gr.addEdge("Salt Lake City Streets and Sanitation", "City Center of Rock Springs", 11.7)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Rice Terrace Pavilion Park", 5.1)
        gr.addEdge("Salt Lake City Streets and Sanitation", "Wheeler Historic Farm", 14.2)

        # Deker Lake Routes

        gr.addEdge("Deker Lake",  "Salt Lake City Ottinger Hall", 7.7)
        gr.addEdge("Deker Lake",  "Columbus Library",  9.3)
        gr.addEdge("Deker Lake",  "Taylorsville City Hall",  4.6)
        gr.addEdge("Deker Lake",  "South Salt Lake Police",  4.8)
        gr.addEdge("Deker Lake",  "Council Hall",  7.7)
        gr.addEdge("Deker Lake",  "Redwood Park",  1.6)
        gr.addEdge("Deker Lake",  "Salt Lake County Mental Health",  3.3)
        gr.addEdge("Deker Lake",  "Salt Lake County/United Police Dept",  3.4)
        gr.addEdge("Deker Lake",  "West Valley Prosecutor",  3.1)
        gr.addEdge("Deker Lake",  "Housing Auth. of Salt Lake County",  5.1)
        gr.addEdge("Deker Lake",  "Utah DMV Administrative Office",  4.6)
        gr.addEdge("Deker Lake",  "Third District Juvenile Court",  6.7)
        gr.addEdge("Deker Lake",  "Cottonwood Regional Softball Complex",  8.1)
        gr.addEdge("Deker Lake",  "Holiday City Office",  10.4)
        gr.addEdge("Deker Lake",  "Murray City Museum",  7.8)
        gr.addEdge("Deker Lake",  "Valley Regional Softball Complex",  4.2)
        gr.addEdge("Deker Lake",  "City Center of Rock Springs",  9.5)
        gr.addEdge("Deker Lake",  "Rice Terrace Pavilion Park",  6.2)
        gr.addEdge("Deker Lake",  "Wheeler Historic Farm",  10.7)

        # Salt Lake City Ottinger Hall Routes

        gr.addEdge("Salt Lake City Ottinger Hall", "Columbus Library", 4.8)
        gr.addEdge("Salt Lake City Ottinger Hall", "Taylorsville City Hall", 11.9)
        gr.addEdge("Salt Lake City Ottinger Hall", "South Salt Lake Police", 4.7)
        gr.addEdge("Salt Lake City Ottinger Hall", "Council Hall", 0.6)
        gr.addEdge("Salt Lake City Ottinger Hall", "Redwood Park", 7.6)
        gr.addEdge("Salt Lake City Ottinger Hall", "Salt Lake County Mental Health", 7.8)
        gr.addEdge("Salt Lake City Ottinger Hall", "Salt Lake County/United Police Dept", 6.6)
        gr.addEdge("Salt Lake City Ottinger Hall", "West Valley Prosecutor", 7.2)
        gr.addEdge("Salt Lake City Ottinger Hall", "Housing Auth. of Salt Lake County", 5.9)
        gr.addEdge("Salt Lake City Ottinger Hall", "Utah DMV Administrative Office", 5.4)
        gr.addEdge("Salt Lake City Ottinger Hall", "Third District Juvenile Court", 1.0)
        gr.addEdge("Salt Lake City Ottinger Hall", "Cottonwood Regional Softball Complex", 8.5)
        gr.addEdge("Salt Lake City Ottinger Hall", "Holiday City Office", 10.3)
        gr.addEdge("Salt Lake City Ottinger Hall", "Murray City Museum", 7.8)
        gr.addEdge("Salt Lake City Ottinger Hall", "Valley Regional Softball Complex", 11.5)
        gr.addEdge("Salt Lake City Ottinger Hall", "City Center of Rock Springs", 9.5)
        gr.addEdge("Salt Lake City Ottinger Hall", "Rice Terrace Pavilion Park", 2.8)
        gr.addEdge("Salt Lake City Ottinger Hall", "Wheeler Historic Farm", 14.1)

        # Columbus Library Routes

        gr.addEdge("Columbus Library", "Taylorsville City Hall", 9.4)
        gr.addEdge("Columbus Library", "South Salt Lake Police", 1.1)
        gr.addEdge("Columbus Library", "Council Hall", 5.1)
        gr.addEdge("Columbus Library", "Redwood Park", 4.6)
        gr.addEdge("Columbus Library", "Salt Lake County Mental Health", 3.7)
        gr.addEdge("Columbus Library", "Salt Lake County/United Police Dept", 4.0)
        gr.addEdge("Columbus Library", "West Valley Prosecutor", 6.7)
        gr.addEdge("Columbus Library", "Housing Auth. of Salt Lake County", 2.3)
        gr.addEdge("Columbus Library", "Utah DMV Administrative Office", 1.8)
        gr.addEdge("Columbus Library", "Third District Juvenile Court", 4.1)
        gr.addEdge("Columbus Library", "Cottonwood Regional Softball Complex", 3.8)
        gr.addEdge("Columbus Library", "Holiday City Office", 5.8)
        gr.addEdge("Columbus Library", "Murray City Museum", 4.3)
        gr.addEdge("Columbus Library", "Valley Regional Softball Complex", 7.8)
        gr.addEdge("Columbus Library", "City Center of Rock Springs", 4.8)
        gr.addEdge("Columbus Library", "Rice Terrace Pavilion Park", 3.2)
        gr.addEdge("Columbus Library", "Wheeler Historic Farm", 6.0)

        # Taylorsville City Hall Routes

        gr.addEdge("Taylorsville City Hall", "South Salt Lake Police", 7.3)
        gr.addEdge("Taylorsville City Hall", "Council Hall", 12.0)
        gr.addEdge("Taylorsville City Hall", "Redwood Park", 4.9)
        gr.addEdge("Taylorsville City Hall", "Salt Lake County Mental Health", 5.2)
        gr.addEdge("Taylorsville City Hall", "Salt Lake County/United Police Dept", 5.4)
        gr.addEdge("Taylorsville City Hall", "West Valley Prosecutor", 8.1)
        gr.addEdge("Taylorsville City Hall", "Housing Auth. of Salt Lake County", 6.2)
        gr.addEdge("Taylorsville City Hall", "Utah DMV Administrative Office", 6.9)
        gr.addEdge("Taylorsville City Hall", "Third District Juvenile Court", 11.5)
        gr.addEdge("Taylorsville City Hall", "Cottonwood Regional Softball Complex", 6.9)
        gr.addEdge("Taylorsville City Hall", "Holiday City Office", 8.3)
        gr.addEdge("Taylorsville City Hall", "Murray City Museum", 4.1)
        gr.addEdge("Taylorsville City Hall", "Valley Regional Softball Complex", 0.4)
        gr.addEdge("Taylorsville City Hall", "City Center of Rock Springs", 4.9)
        gr.addEdge("Taylorsville City Hall", "Rice Terrace Pavilion Park", 11.0)
        gr.addEdge("Taylorsville City Hall", "Wheeler Historic Farm", 6.8)

        # South Lake Police Routes

        gr.addEdge("South Salt Lake Police", "Council Hall", 4.7)
        gr.addEdge("South Salt Lake Police", "Redwood Park", 3.5)
        gr.addEdge("South Salt Lake Police", "Salt Lake County Mental Health", 2.6)
        gr.addEdge("South Salt Lake Police", "Salt Lake County/United Police Dept", 2.9)
        gr.addEdge("South Salt Lake Police", "West Valley Prosecutor", 6.3)
        gr.addEdge("South Salt Lake Police", "Housing Auth. of Salt Lake County", 1.2)
        gr.addEdge("South Salt Lake Police", "Utah DMV Administrative Office", 1.0)
        gr.addEdge("South Salt Lake Police", "Third District Juvenile Court", 3.7)
        gr.addEdge("South Salt Lake Police", "Cottonwood Regional Softball Complex", 4.1)
        gr.addEdge("South Salt Lake Police", "Holiday City Office", 6.2)
        gr.addEdge("South Salt Lake Police", "Murray City Museum", 3.4)
        gr.addEdge("South Salt Lake Police", "Valley Regional Softball Complex", 6.9)
        gr.addEdge("South Salt Lake Police", "City Center of Rock Springs", 5.2)
        gr.addEdge("South Salt Lake Police", "Rice Terrace Pavilion Park", 3.7)
        gr.addEdge("South Salt Lake Police", "Wheeler Historic Farm", 6.4)

        # Council Hall Routes

        gr.addEdge("Council Hall", "Redwood Park", 7.3)
        gr.addEdge("Council Hall", "Salt Lake County Mental Health", 7.8)
        gr.addEdge("Council Hall", "Salt Lake County/United Police Dept", 6.6)
        gr.addEdge("Council Hall", "West Valley Prosecutor", 7.2)
        gr.addEdge("Council Hall", "Housing Auth. of Salt Lake County", 5.9)
        gr.addEdge("Council Hall", "Utah DMV Administrative Office", 5.4)
        gr.addEdge("Council Hall", "Third District Juvenile Court", 1.0)
        gr.addEdge("Council Hall", "Cottonwood Regional Softball Complex", 8.5)
        gr.addEdge("Council Hall", "Holiday City Office", 10.3)
        gr.addEdge("Council Hall", "Murray City Museum", 7.8)
        gr.addEdge("Council Hall", "Valley Regional Softball Complex", 11.5)
        gr.addEdge("Council Hall", "City Center of Rock Springs", 9.5)
        gr.addEdge("Council Hall", "Rice Terrace Pavilion Park", 2.8)
        gr.addEdge("Council Hall", "Wheeler Historic Farm", 14.1)

        # Redwood Park Routes

        gr.addEdge("Redwood Park", "Salt Lake County Mental Health", 1.3)
        gr.addEdge("Redwood Park", "Salt Lake County/United Police Dept", 1.5)
        gr.addEdge("Redwood Park", "West Valley Prosecutor", 4.0)
        gr.addEdge("Redwood Park", "Housing Auth. of Salt Lake County", 3.2)
        gr.addEdge("Redwood Park", "Utah DMV Administrative Office", 3.0)
        gr.addEdge("Redwood Park", "Third District Juvenile Court", 6.9)
        gr.addEdge("Redwood Park", "Cottonwood Regional Softball Complex", 6.2)
        gr.addEdge("Redwood Park", "Holiday City Office", 8.2)
        gr.addEdge("Redwood Park", "Murray City Museum", 5.5)
        gr.addEdge("Redwood Park", "Valley Regional Softball Complex", 4.4)
        gr.addEdge("Redwood Park", "City Center of Rock Springs", 7.2)
        gr.addEdge("Redwood Park", "Rice Terrace Pavilion Park", 6.4)
        gr.addEdge("Redwood Park", "Wheeler Historic Farm", 10.5)

        # Salt Lake County Mental Health Routes

        gr.addEdge("Salt Lake County Mental Health", "Salt Lake County/United Police Dept", 0.6)
        gr.addEdge("Salt Lake County Mental Health", "West Valley Prosecutor", 6.4)
        gr.addEdge("Salt Lake County Mental Health", "Housing Auth. of Salt Lake County", 2.4)
        gr.addEdge("Salt Lake County Mental Health", "Utah DMV Administrative Office", 2.2)
        gr.addEdge("Salt Lake County Mental Health", "Third District Juvenile Court", 6.8)
        gr.addEdge("Salt Lake County Mental Health", "Cottonwood Regional Softball Complex", 5.3)
        gr.addEdge("Salt Lake County Mental Health", "Holiday City Office", 7.4)
        gr.addEdge("Salt Lake County Mental Health", "Murray City Museum", 4.6)
        gr.addEdge("Salt Lake County Mental Health", "Valley Regional Softball Complex", 4.8)
        gr.addEdge("Salt Lake County Mental Health", "City Center of Rock Springs", 6.3)
        gr.addEdge("Salt Lake County Mental Health", "Rice Terrace Pavilion Park", 6.5)
        gr.addEdge("Salt Lake County Mental Health", "Wheeler Historic Farm", 8.8)

        # Salt Lake County/United Police Dept Routes

        gr.addEdge("Salt Lake County/United Police Dept", "West Valley Prosecutor", 5.6)
        gr.addEdge("Salt Lake County/United Police Dept", "Housing Auth. of Salt Lake County", 1.6)
        gr.addEdge("Salt Lake County/United Police Dept", "Utah DMV Administrative Office", 1.7)
        gr.addEdge("Salt Lake County/United Police Dept", "Third District Juvenile Court", 6.4)
        gr.addEdge("Salt Lake County/United Police Dept", "Cottonwood Regional Softball Complex", 4.9)
        gr.addEdge("Salt Lake County/United Police Dept", "Holiday City Office", 6.9)
        gr.addEdge("Salt Lake County/United Police Dept", "Murray City Museum", 4.2)
        gr.addEdge("Salt Lake County/United Police Dept", "Valley Regional Softball Complex", 4.6)
        gr.addEdge("Salt Lake County/United Police Dept", "City Center of Rock Springs", 5.9)
        gr.addEdge("Salt Lake County/United Police Dept", "Rice Terrace Pavilion Park", 5.7)
        gr.addEdge("Salt Lake County/United Police Dept", "Wheeler Historic Farm", 8.4)

        # West Valley Prosecutor Routes

        gr.addEdge("West Valley Prosecutor", "Housing Auth. of Salt Lake County", 7.1)
        gr.addEdge("West Valley Prosecutor", "Utah DMV Administrative Office", 6.1)
        gr.addEdge("West Valley Prosecutor", "Third District Juvenile Court", 7.2)
        gr.addEdge("West Valley Prosecutor", "Cottonwood Regional Softball Complex", 10.6)
        gr.addEdge("West Valley Prosecutor", "Holiday City Office", 12.0)
        gr.addEdge("West Valley Prosecutor", "Murray City Museum", 9.4)
        gr.addEdge("West Valley Prosecutor", "Valley Regional Softball Complex", 7.5)
        gr.addEdge("West Valley Prosecutor", "City Center of Rock Springs", 11.1)
        gr.addEdge("West Valley Prosecutor", "Rice Terrace Pavilion Park", 6.2)
        gr.addEdge("West Valley Prosecutor", "Wheeler Historic Farm", 13.6)

        # Housing Auth. of Salt Lake County Routes

        gr.addEdge("Housing Auth. of Salt Lake County", "Utah DMV Administrative Office", 1.6)
        gr.addEdge("Housing Auth. of Salt Lake County", "Third District Juvenile Court", 4.9)
        gr.addEdge("Housing Auth. of Salt Lake County", "Cottonwood Regional Softball Complex", 3.0)
        gr.addEdge("Housing Auth. of Salt Lake County", "Holiday City Office", 5.0)
        gr.addEdge("Housing Auth. of Salt Lake County", "Murray City Museum", 2.3)
        gr.addEdge("Housing Auth. of Salt Lake County", "Valley Regional Softball Complex", 5.5)
        gr.addEdge("Housing Auth. of Salt Lake County", "City Center of Rock Springs", 4.0)
        gr.addEdge("Housing Auth. of Salt Lake County", "Rice Terrace Pavilion Park", 5.1)
        gr.addEdge("Housing Auth. of Salt Lake County", "Wheeler Historic Farm", 5.2)

        # Utah DMV Administrative office Routes

        gr.addEdge("Utah DMV Administrative Office", "Third District Juvenile Court", 4.4)
        gr.addEdge("Utah DMV Administrative Office", "Cottonwood Regional Softball Complex", 4.6)
        gr.addEdge("Utah DMV Administrative Office", "Holiday City Office", 6.6)
        gr.addEdge("Utah DMV Administrative Office", "Murray City Museum", 3.9)
        gr.addEdge("Utah DMV Administrative Office", "Valley Regional Softball Complex", 6.5)
        gr.addEdge("Utah DMV Administrative Office", "City Center of Rock Springs", 5.6)
        gr.addEdge("Utah DMV Administrative Office", "Rice Terrace Pavilion Park", 4.3)
        gr.addEdge("Utah DMV Administrative Office", "Wheeler Historic Farm", 6.9)

        # Third District Juvenile Court Routes

        gr.addEdge("Third District Juvenile Court", "Cottonwood Regional Softball Complex", 7.5)
        gr.addEdge("Third District Juvenile Court", "Holiday City Office", 9.3)
        gr.addEdge("Third District Juvenile Court", "Murray City Museum", 6.8)
        gr.addEdge("Third District Juvenile Court", "Valley Regional Softball Complex", 11.4)
        gr.addEdge("Third District Juvenile Court", "City Center of Rock Springs", 8.5)
        gr.addEdge("Third District Juvenile Court", "Rice Terrace Pavilion Park", 1.8)
        gr.addEdge("Third District Juvenile Court", "Wheeler Historic Farm", 13.1)

        # Cottonwood Regional Softball Complex Routes

        gr.addEdge("Cottonwood Regional Softball Complex", "Holiday City Office", 2.0)
        gr.addEdge("Cottonwood Regional Softball Complex", "Murray City Museum", 2.9)
        gr.addEdge("Cottonwood Regional Softball Complex", "Valley Regional Softball Complex", 6.4)
        gr.addEdge("Cottonwood Regional Softball Complex", "City Center of Rock Springs", 2.8)
        gr.addEdge("Cottonwood Regional Softball Complex", "Rice Terrace Pavilion Park", 6.0)
        gr.addEdge("Cottonwood Regional Softball Complex", "Wheeler Historic Farm", 4.1)

        # Holiday City Office

        gr.addEdge("Holiday City Office", "Murray City Museum", 4.4)
        gr.addEdge("Holiday City Office", "Valley Regional Softball Complex", 7.9)
        gr.addEdge("Holiday City Office", "City Center of Rock Springs", 3.4)
        gr.addEdge("Holiday City Office", "Rice Terrace Pavilion Park", 7.9)
        gr.addEdge("Holiday City Office", "Wheeler Historic Farm", 4.7)

        # Murray City Museum

        gr.addEdge("Murray City Museum", "Valley Regional Softball Complex", 4.5)
        gr.addEdge("Murray City Museum", "City Center of Rock Springs", 1.7)
        gr.addEdge("Murray City Museum", "Rice Terrace Pavilion Park", 6.8)
        gr.addEdge("Murray City Museum", "Wheeler Historic Farm", 3.1)

        # Valley Regional Softball Complex Routes

        gr.addEdge("Valley Regional Softball Complex", "City Center of Rock Springs", 5.4)
        gr.addEdge("Valley Regional Softball Complex", "Rice Terrace Pavilion Park", 10.6)
        gr.addEdge("Valley Regional Softball Complex", "Wheeler Historic Farm", 7.8)

        # City Center of Rock Springs Routes

        gr.addEdge("City Center of Rock Springs", "Rice Terrace Pavilion Park", 7.0)
        gr.addEdge("City Center of Rock Springs", "Wheeler Historic Farm", 1.3)

        # Rice Terrace Pavilion Park

        gr.addEdge("Rice Terrace Pavilion Park", "Wheeler Historic Farm", 8.3)
