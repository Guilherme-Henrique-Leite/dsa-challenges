# 1283. Find the Smallest Divisor Given a Threshold

nums = [1,2,5,9], threshold = 6
def smallestDivisor(nums, threshold):
    def sum_calculate(divisor):
        return sum((num + divisor - 1) // divisor for num in nums)
    
    left, right = 1, max(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        if sum_calculate(mid) <= threshold:
            right = mid
        else:
            left = mid + 1
    return left 

smallestDivisor(nums=nums, threshold=threshold)