class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_h = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != sorted_h[i]:
                count += 1
        return count