class HashTable:
    
    def __init__(self, capacity: int):

        self.map = []

        for i in range(capacity):
            self.map.append([])

        self.capacity = capacity
        self.size = 0


    def insert(self, key: int, value: int) -> None:

 
        index = key % self.capacity

        for idx, i in enumerate(self.map[index]):
            if i[0] == key:
                self.map[index][idx] = (key, value)
                self.size += 1
                return
        #if not in maps
        self.map[index].append((key, value))
        self.size += 1
        
        if self.size >= (self.capacity // 2):
            self.resize()


    def get(self, key: int) -> int:

        index = key % self.capacity

        for i in self.map[index]:
            if i[0] == key:
                return i[1]
        return -1


    def remove(self, key: int) -> bool:

        index = key % self.capacity

        for idx, i in enumerate(self.map[index]):
            if i[0] == key:
                self.size -= 1
                self.map[index].pop(idx)
                return True
        return False
        


    def getSize(self) -> int:

        return self.size


    def getCapacity(self) -> int:

        return self.capacity


    def resize(self) -> None:

        old_map = self.map
        self.capacity = self.capacity * 2
        self.map = []
        self.size = 0
        for i in range(self.capacity):
            self.map.append([])
        
        for elements in old_map:
            for key, value in elements:
                index = key % self.capacity

                self.map[index].append((key, value))
                self.size += 1
            
        return

