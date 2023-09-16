class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        newNums = []
        while n > 0:
            for i in range(n-1): 
                nums[i] = (nums[i] + nums[i+1]) % 10
            n-=1
        return nums[0]


        