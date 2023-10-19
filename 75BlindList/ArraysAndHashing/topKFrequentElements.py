from typing import List


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
        
        # reverse makes it sorted in descending order
        freqArray.sort(key=lambda x:len(x), reverse=True)


        # print("freq array - {f}".format(f = freqArray))

        position = 0

        for i in range(len(freqArray)):

            if k != 0: 
                answer.append(freqArray[position][0])
                k -= 1
                position += 1

            if k == 0:
                return answer



        return []
    
print("Solution 1 - {f}".format(f = Solution.topKFrequent([1,1,1,2,2,3,3,3,3], 2)))




'''
TC - O(N*log N)
SC - O(N)

Basically same thing as above, just less lines and perhaps shows growth in intuition?

'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for i in nums: 
            hash[i] = 1 + hash.get(i, 0)

# sort in descending order (highest frquency should be 1st and so on)
        sortedHash = dict(sorted(hash.items(), key=lambda item: item[1], reverse=True))


        ans = list(sortedHash.keys())

        return(ans[:k])
        


print("Solution 2 - {f}".format( f = Solution().topKFrequent([1,1,1,2,2,3], 2)))




class Solution:

    '''
    Time Complexity - O(N)
    Space Complexity - O(N)

    Bucket Sort

    '''
    def topKFrequentEfficent(nums, k):
        # hashmap for storing items and count
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

        '''
        
        range(start, stop, increment)

        start - where it should start looping from, in our case, the end
        stop - it should stop before the number put here, in our case, it should not get to 0
        increment - it is 1 by default, since we are doing reverse, we need it to be -1
        
        '''
        for i in range(len(freqArray) - 1, 0 , -1):
            # print("Freq Array: {f}".format(f = freqArray))
            for n in freqArray[i]:
                res.append(n)


                if len(res) == k:
                    return res

        return True

    

print("Solution 3 - {f}".format(f = Solution.topKFrequentEfficent([1,1,1,2,2,3,3,3,3], 2)))







