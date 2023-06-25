class Solution:

    '''
     Time Complexity - O(NLogN)
     Space Complexity - O(N)
    
    '''
    def topKFrequent(nums, k):

        eleMap = {}

        freqArray = []

        answer = []

        for i in range(len(nums)):
            eleMap[nums[i]] = 1 + eleMap.get(nums[i], 0)

        for key, val in eleMap.items():
            freqArray.append([key]*val)
        
        freqArray.sort(key=lambda x:len(x))

        
        position = -1

        for i in range(len(freqArray)):

            if k != 0: 
                answer.append(freqArray[position][0])
                k -= 1
                position -= 1

            if k == 0:
                return answer



        return []
    


    '''
    Time Complexity - O(N)
    Space Complexity - O(N)

    Bucket Sort
    
    '''
    def topKFrequentEfficent(nums, k):
        eleMap = {}

        # Plus 1 cause we are not going to use position 0
        freqArray = [[] for i in range(len(nums) + 1)]

        for i in nums:
            eleMap[i] = 1 + eleMap.get(i, 0)
        # n is key, c is value - which is count, also what would be used to identify the position we want to append values to in freqArray
        for n, c in eleMap.items():
            freqArray[c].append(n)

        
        res = []

        # loop through freq Array in descending order

        # 0 in position 2 of range because we are not taking cognisance of position 0 as we didn't earlier
        for i in range(len(freqArray) - 1, 0 , -1):
            for n in freqArray[i]:
                res.append(n)

                if len(res) == k:
                    return res

        return True

    

print(Solution.topKFrequentEfficent([1,1,1,2,2,3], 2))