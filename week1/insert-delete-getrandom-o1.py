class RandomizedSet:

    def __init__(self):
        
        self.hashTable = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        
        if val not in self.hashTable:
            self.hashTable[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False
        
        
        

    def remove(self, val: int) -> bool:
       
        if val in self.hashTable:
        
            self.hashTable[self.arr[-1]] = self.hashTable[val]
            self.arr[self.hashTable[val]] = self.arr[-1]

            self.arr.pop()
            self.hashTable.pop(val)
            
            return True
        
        return False

    def getRandom(self) -> int:
        
        return random.choice(self.arr)