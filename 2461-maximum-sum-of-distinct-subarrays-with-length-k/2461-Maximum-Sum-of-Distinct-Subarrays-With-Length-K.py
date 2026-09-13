class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        sum_w = 0
        max_s = 0
        hash_m = dict()

        #build initial window
        for j in range(k):
            hash_m[nums[j]] = hash_m.get(nums[j],0)+1
            sum_w = sum_w + nums[j]
        
        if len(hash_m) == k:
            max_s = max(max_s, sum_w)
        
        #sliding the window
        for j in range(k,len(nums)):

            #calclating the current w sum
            sum_w = sum_w - nums[j-k] + nums[j]

            #remove left one from the hash map
            hash_m[nums[j-k]] -= 1
            if hash_m[nums[j-k]] == 0:
                hash_m.pop(nums[j-k])
            
            #add the right one in the hash map
            hash_m[nums[j]] = hash_m.get(nums[j],0)+1 # here you did j-k which was wrong

            #only add in max if the lenght is 3
            if len(hash_m) == k:
                max_s = max(max_s, sum_w)
            
        return max_s
            

        # this hash map len check we already were aware of fro FRUTIS INTO BASKET PROBLEM