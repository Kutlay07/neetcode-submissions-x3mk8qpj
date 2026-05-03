class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        res = 0

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for k in freq.values():
            res += k*(k-1)//2
        return res