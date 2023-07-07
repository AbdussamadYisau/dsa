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

        '''
        
The line for i in range(len(nums) - 1, 0, -1): is a loop statement that iterates over the indices of the nums list in reverse order, excluding the first element. Here's what each part of the range function signifies:

len(nums) - 1: It specifies the starting point of the range. Since Python uses zero-based indexing, len(nums) - 1 represents the index of the last element in the nums list.

0: It specifies the end point of the range. The 0 indicates that the loop should stop just before reaching the index 0, i.e., it iterates until the second element of the list.

-1: It specifies the step value. The -1 indicates that the loop should decrement the index by 1 in each iteration, moving from the last element towards the second element of the list.

In summary, the loop statement for i in range(len(nums) - 1, 0, -1): allows you to iterate over the elements of the nums list in reverse order, starting from the last element and moving towards the second element. The variable i takes on the values of the indices in reverse order, allowing you to access the elements of the list in that order, excluding the first element.
        
        '''
        for i in range(len(freqArray) - 1, 0 , -1):
            print("Freq Array: {}".format(freqArray))
            for n in freqArray[i]:
                res.append(n)


                if len(res) == k:
                    return res

        return True

    

print(Solution.topKFrequentEfficent([1,1,1,2,2,3,3,3,3], 2))