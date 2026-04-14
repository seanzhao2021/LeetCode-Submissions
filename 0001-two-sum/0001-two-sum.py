class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashmap and hashmap[x] != i:
                return [i, hashmap[x]]
            hashmap[nums[i]] = i

            

            
            
        