class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in nums[:i]:
                if nums[i] == j:
                    count += 1
        return count 