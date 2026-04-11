class Solution:
    def countSeniors(self, details: List[str]) -> int:
        k = 0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                k += 1
        return k
