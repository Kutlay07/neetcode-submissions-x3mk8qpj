class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = nums[:]
        
        for i in ans:
            if i == val:
                nums.remove(i)

        k = len(nums)
        return k 

        