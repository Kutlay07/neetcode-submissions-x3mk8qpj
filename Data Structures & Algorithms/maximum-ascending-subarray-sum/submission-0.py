class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        k = nums[0]
        result = nums[0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k += nums[i+1]
            else:
                k = nums[i+1]
            result = max(result,k)
        return result
