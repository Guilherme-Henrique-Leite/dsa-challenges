# 69. Sqrt(x)

x = 4

def mySqrt(x: int) -> int:
        start = 1
        end = x

        while start <= end:
            middle = (start + end) // 2

            if middle * middle == x:
                return middle

            if middle * middle > x:
                end = middle - 1
            else:
                start = middle + 1

        return end

print(mySqrt(x=x))