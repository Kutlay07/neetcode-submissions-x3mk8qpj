class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ans = {}

        for i in nums:
            ans[i] = ans.get(i,0) + 1

        for key,value in ans.items():
            if value % 2 != 0:
                return False
        return True
