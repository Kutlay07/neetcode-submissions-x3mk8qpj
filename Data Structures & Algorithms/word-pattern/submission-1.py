class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2w = {}
        w2p = {}
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p not in p2w:
                p2w[p] = w
            
            if w not in w2p:
                w2p[w] = p

            if p2w[p] != w or w2p[w] != p:
                return False

        return True
