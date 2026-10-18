class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        #start with i = 1 
        pre_sum = nums[0]
        for i in range(1,len(nums)):

            nums[i-1] = pre_sum
            pre_sum = nums[i]+nums[i-1]

        nums[len(nums)-1] = pre_sum

        return nums




