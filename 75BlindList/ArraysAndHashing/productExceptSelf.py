
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
    prefix = [1, 2, 6, 24]
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

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]

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