class Solution:
    def threeSumClosest(self, arr: list[int], target: int) -> int:

        arr.sort()
        closest_sum = arr[0]+arr[1]+arr[2]
        
        for k in range(0, len(arr)-2):

            #2sum 
            i=k+1
            j=len(arr)-1

            #difference = target - arr[k]

            while i<j:
                total = arr[k]+arr[i]+arr[j]
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total > target:
                    j-=1
                elif total < target:
                    i+=1
                else:
                    return total

        return closest_sum 