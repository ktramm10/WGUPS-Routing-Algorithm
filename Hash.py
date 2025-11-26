from Object import Package


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value : Package = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def resize(self):
        old = self.table
        oldCap = self.capacity

        # double capacity
        self.capacity = int(self.capacity * 2)
        self.table = [None] * self.capacity
        self.size = 0

        # reinsert and rehash everything
        for node in old:
            current = node
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        # update load factor and check for resize:
        if (self.size + 1) / self.capacity >= 1.5:
            self.resize()

        idx = self._hash(key)

        if self.table[idx] is None:
            self.table[idx] = Node(key, value)
            self.size += 1
        else:
            current = self.table[idx]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new = Node(key, value)
            new.next = self.table[idx]
            self.table[idx] = new
            self.size += 1

    def search(self, key):
        idx = self._hash(key)

        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def lookUp(self, key):
        idx = self._hash(key)

        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value.getData()
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)
        previous = None
        current = self.table[idx]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[idx] = current.next
                self.size -= 1
                return current.value
            previous = current
            current = current.next
        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        if self.search(key):
            return True
        else:
            return False

    def populateHashTableData(ht):
        # insert package data to hash table
        ht.insert(1, Package("South Salt Lake Public Works", "195 W Oakland Ave"
                                    , "10:30 AM", "Salt Lake City",
                                    "84115", 21, "HUB",1, 1))
        ht.insert(2, Package("Columbus Library","2530 S 500 E"
                                    , "EOD", "Salt Lake City",
                                    "84106", 44, "HUB", 2))
        ht.insert(3, Package("Salt Lake City Ottinger Hall","233 Canyon Rd"
                                    , "EOD", "Salt Lake City",
                                    "84103", 2, "HUB", 3))
        ht.insert(4, Package("Utah DMV Administrative Office","380 W 2880 S"
                                    , "EOD", "Salt Lake City",
                                    "84115", 4, "HUB", 4))
        ht.insert(5, Package("Third District Juvenile Court","410 S State St"
                                    , "EOD", "Salt Lake City",
                                    "84111", 5, "HUB", 5))
        ht.insert(6, Package("South Salt Lake Public Works","195 W Oakland Ave"
                                    , "10:30 AM", "West Valley City",
                                    "84119", 88, "HUB", 6, 2))
        ht.insert(7, Package("Redwood Park","3060 Lester St"
                                    , "EOD", "Salt Lake City",
                                    "84106", 8, "HUB", 7))
        ht.insert(8, Package("Sugar House Park","1330 2100 S"
                                    , "EOD", "Salt Lake City",
                                    "84103", 9, "HUB", 8))
        ht.insert(9, Package("Council Hall","300 State St"
                                    , "EOD", "Salt Lake City",
                                    "84103", 2, "HUB", 9))
        ht.insert(10, Package("Rice Terrace Pavilion Park","600 E 900 South"
                                     , "EOD", "Salt Lake City",
                                     "84105", 1, "HUB", 10))
        ht.insert(11, Package("Taylorsville City Hall","2600 Taylorsville Blvd"
                                     , "EOD", "Salt Lake City",
                                     "84118", 1, "HUB", 11))
        ht.insert(12, Package("West Valley Prosecutor","3575 W Valley Central Station bus Loop"
                                     , "EOD", "West Valley City",
                                     "84119",1, "HUB", 12))
        ht.insert(13, Package("Salt Lake City Streets and Sanitation","2010 W 500 S"
                                     , "10:30 AM", "Salt Lake City",
                                     "84104", 2, "HUB", 13, 1))
        ht.insert(14, Package("Cottonwood Regional Softball Complex","4300 S 1300 E"
                                     , "10:30 AM", "Millcreek",
                                     "84117", 88, "HUB", 14, 1))
        ht.insert(15, Package("Holiday City Office","4580 S 2300 E"
                                     , "9:00:00 AM", "Holladay",
                                     "84117", 4, "HUB", 15, 2))
        ht.insert(16, Package("Holiday City Office","4580 S 2300 E"
                                     , "10:30 AM", "Holladay",
                                     "84117", 88, "HUB", 16, 1))
        ht.insert(17, Package("Salt Lake County Mental Health","3148 S 1100 W"
                                     , "EOD", "Salt Lake City",
                                     "84119", 2, "HUB", 17))
        ht.insert(18, Package("Taylorsville-Bennion Heritage City Gov Off","1488 4800 S"
                                     , "EOD", "Salt Lake City",
                                     "84123", 6, "HUB", 18))
        ht.insert(19, Package("Salt Lake City Division of Health Services","177 W Price Ave"
                                     , "EOD", "Salt Lake City",
                                     "84115", 37, "HUB", 19))
        ht.insert(20, Package("Housing Auth. of Salt Lake County","3595 Main St"
                                     , "10:30 AM", "Salt Lake City",
                                     "84115", 37, "HUB", 20, 1))
        ht.insert(21, Package("Housing Auth. of Salt Lake County","3595 Main St"
                                     , "EOD", "Salt Lake City",
                                     "84115", 3, "HUB", 21))
        ht.insert(22, Package("Wheeler Historic Farm","6351 South 900 East"
                                     , "EOD", "Murray", "84121",
                                     2, "HUB", 22))
        ht.insert(23, Package("Valley Regional Softball Complex","5100 South 2700 West"
                                     , "EOD", "Salt Lake City",
                                     "84118", 5, "HUB", 23))
        ht.insert(24, Package("Murray City Museum","5025 State St"
                                     , "EOD", "Murray", "84107",
                                     7, "HUB", 24))
        ht.insert(25, Package("City Center of Rock Springs","5383 South 900 East #104"
                                     , "10:30 AM", "Salt Lake City",
                                     "84117", 7, "HUB", 25, 2))
        ht.insert(26, Package("City Center of Rock Springs","5383 South 900 East #104"
                                     , "EOD", "Salt Lake City",
                                     "84117", 25, "HUB", 26))
        ht.insert(27, Package("International Peace Gardens","1060 Dalton Ave S"
                                     , "EOD", "Salt Lake City",
                                     "84104", 5, "HUB", 27))
        ht.insert(28, Package("South Salt Lake Police","2835 Main St"
                                     , "EOD", "Salt Lake City",
                                     "84115", 7, "HUB", 28))
        ht.insert(29, Package("Sugar House Park","1330 2100 S"
                                     , "10:30 AM", "Salt Lake City",
                                     "84106", 2, "HUB", 29, 1))
        ht.insert(30, Package("Council Hall","300 State St"
                                     , "10:30 AM", "Salt Lake City",
                                     "84103", 1, "HUB", 30, 1))
        ht.insert(31, Package("Salt Lake County/United Police Dept","3365 S 900 W"
                                     , "10:30 AM", "Salt Lake City",
                                     "84119", 1, "HUB", 31, 1))
        ht.insert(32, Package("Salt Lake County/United Police Dept","3365 S 900 W"
                                     , "EOD", "Salt Lake City",
                                     "84119", 1, "HUB", 32))
        ht.insert(33, Package("Columbus Library","2530 S 500 E"
                                     , "EOD", "Salt Lake City",
                                     "84106", 1, "HUB", 33))
        ht.insert(34, Package("Holiday City Office","4580 S 2300 E"
                                     , "10:30 AM", "Holladay",
                                     "84117", 2, "HUB", 34, 1))
        ht.insert(35, Package("International Peace Gardens","1060 Dalton Ave S"
                                     , "EOD", "Salt Lake City",
                                     "84104", 88, "HUB", 35))
        ht.insert(36, Package("Deker Lake","2300 Parkway Blvd"
                                     , "EOD", "West Valley City",
                                     "84119",88, "HUB", 36))
        ht.insert(37, Package("Third District Juvenile Court","410 S State St"
                                     , "10:30 AM", "Salt Lake City",
                                     "84111", 2, "HUB", 37, 1))
        ht.insert(38, Package("Third District Juvenile Court","410 S State St"
                                     , "EOD", "Salt Lake City",
                                     "84111", 9, "HUB", 38))
        ht.insert(39, Package("Salt Lake City Streets and Sanitation","2010 W 500 S"
                                     , "EOD", "Salt Lake City",
                                     "84104", 9, "HUB", 39))
        ht.insert(40, Package("Utah DMV Administrative Office","380 W 2880 S"
                             , "10:30 AM", "Salt Lake City",
                             "84115", 45, "HUB", 40, 1))