class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_counter = Counter(t)
        need_len = len(need_counter)
        window_counter = {}
        have = 0 # for holding how many of required elements from target we have with req freq
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            character = s[right]
            window_counter[character] = window_counter.get(character, 0) + 1

            # Checking if we need to increment have as new character addition is favourable
            if character in need_counter and window_counter[character]==need_counter[character]:
                have+=1
            
            # Checking if we have an acceptable window now based on new addition
            while have == need_len: # Found an acceptable window

                if right-left+1 < res_len:
                    # Updating res idx
                    res = [left,right]
                    res_len = right - left + 1

                # checking if i can remove left element 
                window_counter[s[left]]-=1

                # if unfavourable after removing left element, adjusting have
                if s[left] in need_counter and window_counter[s[left]]< need_counter[s[left]]:
                    have-=1
                # incrementing left element
                left+=1
        left, right = res
        return s[left:right+1]

            

