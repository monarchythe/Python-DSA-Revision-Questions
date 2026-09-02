class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i=0
        dict_fruits = dict()
        max_fruits = 0

        for j in range(len(fruits)):

            dict_fruits[fruits[j]] = dict_fruits.get(fruits[j], 0) + 1 

            while len(dict_fruits) > 2:

                dict_fruits[fruits[i]] -=1

                if dict_fruits[fruits[i]] == 0:
                    dict_fruits.pop(fruits[i], None) #**imp**

                i+=1

            #max_fruits = max(max_fruits, sum(dict_fruits.values()))
            max_fruits = max(max_fruits, j-i+1) #******** imp *******

        return max_fruits




# do revise all the hashmap addding deleting checking code here **imp**
# **imp**

        