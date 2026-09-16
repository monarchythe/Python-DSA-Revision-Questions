class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:

        #sorting
        arr.sort()
        output = []

        for k in range(0, len(arr) - 2):

            #2 sum
            i = k+1
            j = len(arr) - 1

            target = 0 - arr[k]

            #skipping the duplicate
            # Short - Circuit Evaluation !!!!!!!!!!!!
            if k!=0 and arr[k] == arr[k-1]:
                continue

            while i<j:

                if arr[i] + arr[j] > target:
                    j-=1
                elif arr[i] + arr[j] == target:
                    output.append([arr[k],arr[i],arr[j]])
                    i+=1
                    j-=1
                    # deduplication 2 - keep moving forward untill the numebrs are unique !!!!!!!!!!!!!!
                    while i<j and arr[i] == arr[i-1]:
                        i+=1
                    while i<j and arr[j] == arr[j+1]:
                        j-=1                  
                else:
                    i+=1

        return output
        

# the most trickiest part here is how to handle the duplicates. 

# you need to be aware that if K is repeating , we can skip it as we already found all the triplets , belonging to it

# then skip duplicate i and j 

# The three dedup checks handle three different things:

# Outer k — don't fix the same first element twice
# Inner i — after a match, don't record with the same left value
# Inner j — after a match, don't record with the same right value

    # while i<j and arr[i] == arr[i-1]:
    #                     i+=1
    # while i<j and arr[j] == arr[j+1]:
    #                     j-=1  
# Why: you already advanced i and j. Now you're asking "did I land on the same value as before?" That "before" value is behind you — at arr[i-1] (one step back from your new position) and arr[j+1] (one step back from your new position for j).