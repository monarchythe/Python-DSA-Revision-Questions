class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hash_map = dict()
        answer = []

        for string in strs:

            #sort it and convert it into tuple to put it in the hashmap
            key = tuple(sorted(string))

            if key in hash_map:
                #here the string is stored in a list 
                #AND THAT LIST is the Value of the HASH_MAP
                #this is the first time i saw this
                hash_map[key].append(string)

            else:
                
                #hash_map[key].append(string) - this will give error
                hash_map[key] = [string]

        return list(hash_map.values())




        