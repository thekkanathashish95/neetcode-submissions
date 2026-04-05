class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Array to hold output of len(nums)
        #Two distinct loops
        #Loop 1- prefix for every i, where prefix is product of elements excluding i from 0
        #Loop 2- suffix for every i, where suffix is the product of elements from i till n

        n = len(nums)
        output = [1] * n

        #prefix loop
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix*=nums[i]
        
        #suffix loop
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i]*=suffix
            suffix*=nums[i]
        
        return output


        