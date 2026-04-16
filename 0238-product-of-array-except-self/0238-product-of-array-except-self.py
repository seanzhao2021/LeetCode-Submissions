class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [0 for _ in range(len(nums))]
        suffix = [0 for _ in range(len(nums))]
        res = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if i == 0:
                prefix[i] = 1
                suffix[j] = 1
            else:
                prefix[i] = prefix[i-1] * nums[i - 1]
                suffix[j] = suffix[j+1] * nums[j + 1]
        
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res