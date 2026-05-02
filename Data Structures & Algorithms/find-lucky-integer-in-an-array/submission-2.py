class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return max([k for k, v in freq.items() if k == v] or [-1])