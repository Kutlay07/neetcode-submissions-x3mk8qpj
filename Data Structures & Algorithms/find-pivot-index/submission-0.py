class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        k = 0

        for i in range(len(nums)):
            k += nums[i]
            if sum(nums[i:]) == k:
                return i
        return -1