# 35. Search Insert Position
nums = [1,3,5,6]
target = 5

def searchInsert(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2

        if target == nums[middle]:
            return middle
        if target > nums[middle]:
            start = middle + 1 
        else:
            end = middle - 1
                
        return start
                
print(searchInsert(nums=nums, target=target))