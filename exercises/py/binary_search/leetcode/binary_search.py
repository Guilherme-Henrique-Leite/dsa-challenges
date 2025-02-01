## 704. Binary Search

nums = [-1,0,3,5,9,12]
target = 9

def search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

print(search(nums=nums, target=target))