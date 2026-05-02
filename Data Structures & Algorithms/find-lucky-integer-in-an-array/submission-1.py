class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        res = -1

        for i in arr:
            freq[i] = freq.get(i,0) + 1

        for key,value in freq.items():
            if key == value:
                res = max(res,key)
                
        return res