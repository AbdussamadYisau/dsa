from typing import List  # Import List from the typing module


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        solutionHash = {}

        for i in nums:

            if i in solutionHash:
                return True
            
            else:
                solutionHash[i] = 1

        return False


print(Solution().containsDuplicate([1,2,3,4]))
        
       