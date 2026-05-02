class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = [0] * (n * n + 1)  # dict yerine array → daha hızlı

        for row in grid:
            for val in row:
                count[val] += 1

        repeated = missing = 0
        for i in range(1, n * n + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i

        return [repeated, missing]