from typing import List


'''
TC - O(N), SC - O(N)

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}


        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hash:

                return([i, hash[complement]])

            hash[nums[i]] = i

'''
This would only work if the array is sorted, if you test this solution with [2,7,1,11]. It would fail, i found that interesting. So you can only use two pointers / sliding window for particular scenarios. 

TC - O(N) if we don't consider the sorting, SC - O(1)

'''


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums.sort() # o(logn)

        i, j = 0, len(nums) - 1

        while i < j:

            currentSum = nums[i] + nums[j]
            
            if currentSum == target:

                return([i,j])
            
            elif currentSum > target: 
                j -= 1

            else: 
                i += 1




print(Solution1().twoSum([2,7, 1,5], 9))
        