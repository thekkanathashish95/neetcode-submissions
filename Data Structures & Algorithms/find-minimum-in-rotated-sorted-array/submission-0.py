class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right = len(nums) - 1
        res = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]: #found a fully sorted array
                res = min(res, nums[left])
                break
            mid = (left + right) // 2

            # checking if till mid it is sorted in either way
            if nums[mid] >= nums[left]:
                # [left...mid] - need to consider left as min candidate
                res = min(res, nums[left])
                # need to check the right side as we already looked at left
                left = mid + 1

            else:
                # [mid...left]
                # mid can be smaller and need yo search left side
                res = min(res, nums[mid])
                right = mid - 1

        return res
            
