class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_holder = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap_holder:
                return [hashmap_holder[complement], index]
            else:
                hashmap_holder[num] = index


        