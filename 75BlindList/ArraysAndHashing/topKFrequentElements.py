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
    

print(Solution.topKFrequent([1,1,1,2,2,3], 2))