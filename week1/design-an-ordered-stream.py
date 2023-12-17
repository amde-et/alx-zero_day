class OrderedStream:
    def __init__(self, n: int):
        self.stream = {}
        self.ptr = 1
        
    def insert(self, idKey: int, value: str) -> List[str]:

        self.stream[idKey] = value

        if idKey > self.ptr:
            return []

        result = []
        while self.ptr in self.stream:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)