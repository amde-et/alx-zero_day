class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = sorted([start, destination])        

        dist1 = sum(distance[start: destination])        
        
        for i in range(destination-1, start-1, -1):
            distance.pop(i)

        dist2 = sum(distance)
        return min(dist1, dist2)