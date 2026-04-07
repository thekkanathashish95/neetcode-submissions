class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        end = k
        while end < len(nums)+1:
            window_max = max(nums[end-k:end])
            output.append(window_max)
            end+=1
        return output

        