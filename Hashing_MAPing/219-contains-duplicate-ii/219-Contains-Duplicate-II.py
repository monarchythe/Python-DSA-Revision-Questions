class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_map = dict()

        for i,num in enumerate(nums):

            if nums[i] in hash_map and i - hash_map[nums[i]] <= k:
                    return True  
            else:
                hash_map[nums[i]] = i
        
        return False


#too much time 

            # if nums[i] in hash_map:
                
            #     #get the previous index
            #     j = hash_map[nums[i]]
            #     #get the diff and check
            #     if abs(i-j) <= k:
            #         return True
            #     else:
            #         #update the hashmap with latest index
            #         hash_map[nums[i]] = i

            # else:
            #     hash_map[nums[i]] = hash_map.get(nums[i],0) + i