#Algorithm to find minimum in a rotated list
#This algorithm contains a difference 

import math

def findMin(nums: list) -> int:
    if nums[-1] > nums[0] or len(nums) == 1:
        return nums[0]
    
    def findMinRecursive(nums, start, end) -> int:
        length = end - start
        
        if length == 1:
            return min(nums[start], nums[end])
        
        middle = start + math.floor(length/2)
        
        if nums[middle] > nums[start]:
            return findMinRecursive(nums, middle, end)
        
        return findMinRecursive(nums, start, middle)

    return findMinRecursive(nums, 0, len(nums) - 1)


print(findMin([4,5,6,7,0,1,2]))

