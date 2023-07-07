
class Solution:
    '''
    Time Complexity - O(N^2)
    Space Complexity - O(N)
    '''
    def productExceptSelf(nums):
        eleMap = {}
        ans = []
        n = len(nums)
        for i in range(n):

            eleMap[i] = nums[i]

        for i in range(n):
            posProd = 1

            for k, v in eleMap.items():
                if k != i: 
                    posProd *= v
            ans.append(posProd)

        return ans
    
    '''
    Use prefix and postfix products for every single product - which is o(n) space, but we could also not store prefix and postfix and that would make it o(1)

    nums = [1,2,3,4]
    prefix = [1, 1, 2, 6]
    postfix = [24,24,12,4]

    ans = [default 1 * postfix[1] = 24, prefix[0] * postfix[2] = 12, prefix[1] * postfix[3] = 8, prefix[2] * default 1 = 6]
    ans = [24, 12, 8, 6]
    '''
    
    def productExceptSelfEfficient(nums): 
        n = len(nums)
        output = [1] * n # doesn't count as extra space for this question

        pre = 1

        for i in range(n):
            output[i] = pre
            pre *= nums[i]

            # print("Output and pre = {} - {} ".format(output,pre))
        
            
        post = 1

        '''
        
The line for i in range(len(nums) - 1, -1, -1): is a loop statement that iterates over the indices of the nums list in reverse order. Here's what each part of the range function signifies:

len(nums) - 1: It specifies the starting point of the range. Since Python uses zero-based indexing, len(nums) - 1 represents the index of the last element in the nums list.

-1: It specifies the end point of the range. The -1 indicates that the loop should continue until the index reaches -1 (inclusive), i.e., it iterates until it reaches the first element of the list.

-1: It specifies the step value. The -1 indicates that the loop should decrement the index by 1 in each iteration, moving from the last element towards the first element of the list.

In summary, the loop statement for i in range(len(nums) - 1, -1, -1): allows you to iterate over the elements of the nums list in reverse order, starting from the last element and moving towards the first element. The variable i takes on the values of the indices in reverse order, allowing you to access the elements of the list in that order.
        '''

        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]

        print(range(len(nums)-1, -1, -1))
        return output
    

    '''
    Solution on Leetcode. Interesting cause the prefix and postfix was done in one take
    '''
    
    def productExceptSelfLeet(nums):
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)


print(Solution.productExceptSelfEfficient([1,2,3,4]))