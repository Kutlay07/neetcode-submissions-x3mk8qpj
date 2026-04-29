class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []


        for i in range(len(nums1)):
            x = nums1[i]
            pos = nums2.index(x)

            for j in range(pos + 1, len(nums2)):
                if nums2[j] > x:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans
