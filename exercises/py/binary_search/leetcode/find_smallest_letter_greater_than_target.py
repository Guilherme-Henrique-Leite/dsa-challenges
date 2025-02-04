# 744. Find Smallest Letter Greater Than Target

letters = ["c","f","j"]
target = "a"

def nextGreatestLetter(letters: list[str], target: str) -> str:

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        start = 0
        end = len(letters) - 1

        while start <= end:
            middle = (start + end) // 2

            if target >= letters[middle]:
                start = middle + 1
            
            if target < letters[middle]:
                end = middle - 1
        
        return letters[start]

print(nextGreatestLetter(letters=letters, target=target))