class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = {}
        res = []

        for row in grid:
            for val in row:
                if val not in ans:
                    ans[val] = 0
                ans[val] += 1


        for key, value in ans.items():
            if value > 1:
                res.append(key)

        for i in range(1,len(ans)+2):
            if i not in ans:
                res.append(i)
        return res