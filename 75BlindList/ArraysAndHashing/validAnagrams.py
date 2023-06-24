# Time Complexity - O(N), Space Complexity - O(N)

class Solution:
    def isAnagram(s, t):
        sMap, tMap = {}, {}

        for i in s:
            sMap[i] = 1 + sMap.get(i, 0)

        for i in t:
            tMap[i] = 1 + tMap.get(i, 0)

        if sMap == tMap:
            return True
        
        return False
    



print(Solution.isAnagram("anagram", "nagaram"))