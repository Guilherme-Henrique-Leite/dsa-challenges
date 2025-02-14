from collections import defaultdict


s = "anagram"
t = "nagaram"

#s = "rat", t = "car"
def isAnagram(s: str, t: str) -> bool:
        count = defaultdict(int)
  
        for x in s:
            count[x] += 1
        
        for x in t:
            count[x] -= 1
        
        for val in count.values():
            if val != 0:
                return False
        
        return True

isAnagram(s=s, t=t)