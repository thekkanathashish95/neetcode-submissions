class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap_holder = {}
        for num in nums:
            if num in hashmap_holder:
                return True
            else:
                hashmap_holder[num] = None
        return False
