class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx_holder = {}
        for idx, num in enumerate(numbers):
            complement = target - num
            idx_holder[complement] = idx + 1

        for idx, num in enumerate(numbers):
            if num in idx_holder:
                return [idx + 1, idx_holder[num]]