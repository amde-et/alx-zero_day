class UndergroundSystem:

    def __init__(self):
        self.people = {}
        self.history = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.history[(self.people[id][0], stationName)] = self.history.get((self.people[id][0], stationName), []) + [t-self.people[id][1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.history[(startStation,endStation)])/len(self.history[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)