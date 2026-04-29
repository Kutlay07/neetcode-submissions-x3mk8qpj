class Solution:
    def maxDifference(self, s: str) -> int:
        min_even = float('inf')
        max_odd = 0
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        for count in freq.values():
            if count % 2 == 0:
                min_even = min(min_even,count)
            else:
                max_odd = max(max_odd,count)

        return max_odd - min_even