class Solution:

    '''
    The time complexity of the given solution is O(N * M * log M), where N is the number of strings in the input list `strs`, and M is the maximum length of the strings.

    Here's the breakdown of the time complexity:

    1. The outer loop iterates over each string in `strs`, resulting in a time complexity of O(N).

    2. Within the loop, the `sorted` function is applied to each string `i`, which has a time complexity of O(M * log M), where M is the length of the string. Sorting a string takes O(M * log M) time complexity because the algorithm used for sorting (usually based on a comparison-based sorting algorithm like quicksort or mergesort) has an average time complexity of O(M * log M).

    3. The `"".join(sorted(i))` expression is used as the key in the `anagramsMap`. This operation also has a time complexity of O(M * log M) because it involves sorting the string `i`.

    4. Lastly, the values in the `anagramsMap` are retrieved, which has a time complexity of O(1) because dictionary lookups have constant time complexity.

    Considering all these factors, the overall time complexity of the solution is O(N * M * log M).

    Space Complexiity is O(N)
    
    '''
    def groupAnagrams(strs):

        anagramsMap = {}

        for i in strs:
            
            anagramsMap["".join(sorted(i))] = [i] + anagramsMap.get("".join(sorted(i)), [])

        return anagramsMap.values()
    

    '''
        Time Complexity - O(N * M) : where N is list of strings, and M is equal to average length of the individual strings
        Space Complexity - O(N)
    
    '''
    def groupAnagramsEfficient(strs):

        

        anagramsMap = {}

        for i in strs:
            count = [0] * 26 #a.....z
            for c in i:
                count[ord(c) - ord("a")] += 1

            anagramsMap[tuple(count)] = [i] + anagramsMap.get(tuple(count), [])

        return anagramsMap.values()









print(Solution.groupAnagramsEfficient(["eat","tea","tan","ate","nat","bat"]))