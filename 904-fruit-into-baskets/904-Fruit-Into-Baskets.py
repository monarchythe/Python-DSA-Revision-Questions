class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i,j =0,0
        n= len(fruits)
        hash_map = dict()
        sum_ = 0
        max_ = 0
        
        for j in range(n):

            hash_map[fruits[j]] = hash_map.get(fruits[j], 0) +1 #**imp**

            #inner while runs till condition is invalid
            while len(hash_map) > 2:

                #reducing the count from left
                hash_map[fruits[i]] = hash_map[fruits[i]] - 1 #**imp**
                
                #now deleting the key+value if the value of the key i is 0
                if hash_map[fruits[i]] == 0:
                    del hash_map[fruits[i]] #**imp**
                i+=1

            sum_ = sum(hash_map.values()) #**imp**
            max_ = max(max_, sum_)

        return max_
    

# do revise all the hashma addding deleting checking code here **imp**
# **imp**

        