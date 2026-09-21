class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        #creating the hash map frequency
        hash_map = dict()
        for item in nums:
            hash_map[item] = hash_map.get(item,0)+1
        
        #We need to sort the hash_map, then get top K keys 
        #SORTED function - TAKES IN A Function, as KEY and ALSO, gives LIST FORMAT output

        print(sorted(hash_map, key= hash_map.get, reverse = True)[:k])

        return sorted(hash_map, key= hash_map.get, reverse = True)[:k]

