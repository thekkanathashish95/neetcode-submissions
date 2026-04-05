class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        coll = set()

        for letter in s:
            while letter in coll:
                coll.remove(s[start])
                start+=1

            # IF NOT
            coll.add(letter)
            # Updating max length as new letter is added to collection
            max_len = max(max_len, len(coll))

        return max_len