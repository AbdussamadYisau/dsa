# Time Complexity - O(N), Space Complexity - O(N), where N is 26 (26 characters)
from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicatesMap = {}

        for i in nums: 
            if i in duplicatesMap:
                return True
            else: 
                duplicatesMap[i] = 1
                
        return False