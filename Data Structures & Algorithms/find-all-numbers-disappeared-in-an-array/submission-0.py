class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set(nums)
        lost = []

        for i in range(1,len(nums) + 1):
            if i not in ans:
                lost.append(i)
        return lost
