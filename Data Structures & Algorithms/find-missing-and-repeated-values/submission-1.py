class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n
        
        actual_sum = 0
        actual_sq_sum = 0
        
        for row in grid:
            for val in row:
                actual_sum += val
                actual_sq_sum += val * val
        
        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6
        
        # repeated - missing = diff
        diff = actual_sum - expected_sum          # a - b
        # repeated² - missing² = sq_diff → (a-b)(a+b) = sq_diff
        sq_diff = actual_sq_sum - expected_sq_sum
        
        total = sq_diff // diff   # a + b
        
        repeated = (diff + total) // 2
        missing = total - repeated
        
        return [repeated, missing]