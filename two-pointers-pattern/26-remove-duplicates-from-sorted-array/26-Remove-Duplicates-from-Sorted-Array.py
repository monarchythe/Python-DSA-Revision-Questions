class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i,j = 1,1
        while i<len(nums):

            #if adjacent are equal:
            if nums[i] == nums[i-1]:
                #fix j
                #just keep moving i
                i+=1
            else:
                nums[j] = nums[i]
                i+=1
                j+=1
                #count+=1
        
        return j

    # #count = J only 
            #clean code 
        # j=1
        # for i in range(1, len(n)):

        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j+=1

        # return j
            