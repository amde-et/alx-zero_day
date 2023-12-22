class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        down=False
        up=False 
        if len(arr) <3:
            return False

        for i in range(1, len(arr)):

            if not down:
                if arr[i] < arr[i-1]:
                    down = True
                elif arr[i] == arr[i-1] :
                    return False
                else:
                    up = True
            else:
                if arr[i] >= arr[i-1]:
                    return False

        return up and down