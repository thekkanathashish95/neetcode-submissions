class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = [e for e in s if e.isalnum()]
        lenth = len(s_clean)
        for i in range(lenth):
            # print(f"Comparing: {s_clean[i]} and {s_clean[lenth-1-i]}")
            if s_clean[i].lower() !=s_clean[lenth-1-i].lower():
                return False
        return True
        