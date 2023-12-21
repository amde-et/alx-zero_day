class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = next_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= next_smallest:
                next_smallest = num
            else:
                return True
        return False