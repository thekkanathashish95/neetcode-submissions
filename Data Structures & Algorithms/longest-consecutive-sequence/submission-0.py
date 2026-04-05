class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = sorted(set(nums))
        max_length = 0
        for num in set_nums:
            if num-1 not in set_nums:
                length = 1
                while num+length in set_nums:
                    length+=1
                max_length= length if length>max_length else max_length
        return max_length
        