# Find Minimum in Rotated Sorted Array

nums = [3,4,5,1,2]
def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right) // 2
                    
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
                    
    return nums[left]

findMin(nums=nums)