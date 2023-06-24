class Solution:

    # This solution is O(N^2) time complexity and O(N) space complexity
    def twoSum(nums, target):
        pairsMap = {}

        # Put elements in pairs map
        for i in range(len(nums)):

            pairsMap[i] = nums[i]

        for i in pairsMap: 

            ans = target - pairsMap[i]

            for key, val in pairsMap.items():
                if ans == val and key != i:
                    return ([i, key])
                
    # This solution is O(N) time complexity and O(N) space complexity
    def twoSumEfficient(nums, target): 
        pairsMap = {}

        for i in range(len(nums)):
            ans = target - nums[i]

            if ans in pairsMap:
                return([pairsMap[ans], i])
            else: 
                pairsMap[nums[i]] = i
                
    
                



print(Solution.twoSumEfficient([2,7,11,15], 9))
print(Solution.twoSumEfficient([3,3], 6))
