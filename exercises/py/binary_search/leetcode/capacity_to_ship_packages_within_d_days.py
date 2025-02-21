# 1011. Capacity To Ship Packages Within D Days

weights = [1,2,3,4,5,6,7,8,9,10], days = 5
def shipWithinDays(weights: list[int], days: int) -> int:
        maxWeight, totalWeight = -1, 0
        
        for weight in weights:
            maxWeight = max(maxWeight, weight)
            totalWeight += weight
        left, right = maxWeight, totalWeight

        while left < right:
            mid = (left + right) // 2
            daysNeeded, currWeight = 1, 0
            for weight in weights:
                if currWeight + weight > mid:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += weight
            if daysNeeded > days:
                left = mid + 1
            else:
                right = mid
        return left