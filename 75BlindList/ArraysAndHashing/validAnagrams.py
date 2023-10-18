'''
TC - O(N), SC - O(N)

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sHashmap , tHashMap = {} , {}

        for i in s:
            if i in sHashmap:
                sHashmap[i] += 1
            else:
                sHashmap[i] = 1

        for i in t:
            if i in tHashMap:
                tHashMap[i] += 1 
            else:
                tHashMap[i] = 1

        
        if sHashmap == tHashMap:
            return True
        


        return False
    


'''
TC - O(N), SC - O(N). A bit faster because we consider length of the words first and foremost. 

'''
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False
        

        sHashmap , tHashMap = {} , {}

        for i in range(len(s)):
           sHashmap[s[i]] = 1 + sHashmap.get(s[i], 0)
           tHashMap[t[i]] = 1 + tHashMap.get(t[i],0)


        
        if sHashmap == tHashMap:
            return True
        


        return False
    



print(Solution1().isAnagram("rat", "car"))
      