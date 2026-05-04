class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = {}
        res = 0

        for i in chars:
            chars_count[i] = chars_count.get(i,0) + 1

        for word in words:
            word_count = {}
            valid = True

            for char in word:
                word_count[char] = word_count.get(char,0) + 1

            for char in word_count:
                if char not in chars_count or word_count[char] > chars_count[char]:
                    valid = False
                    break


            if valid:
                res += len(word)
        return res