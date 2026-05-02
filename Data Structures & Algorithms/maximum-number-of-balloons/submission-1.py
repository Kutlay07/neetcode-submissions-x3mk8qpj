class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = {}
        balloon_count = {}
        res = float("inf")

        for i in text:
            ans[i] = ans.get(i, 0) + 1

        for i in "balloon":
            balloon_count[i] = balloon_count.get(i, 0) + 1

        for i in balloon_count:
            if i not in ans:
                res = 0
                break
            res = min(res, ans[i] // balloon_count[i])
        return res