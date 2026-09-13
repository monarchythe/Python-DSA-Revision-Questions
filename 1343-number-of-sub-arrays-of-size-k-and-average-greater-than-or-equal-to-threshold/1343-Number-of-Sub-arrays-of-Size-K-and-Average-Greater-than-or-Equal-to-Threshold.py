class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        #build the window till k 
        count =0
        avg = 0
        sumw = 0

        for j in range(k):
            sumw = sumw + arr[j]
        
        if sumw/k >= threshold:
            count+=1
        
        for j in range(k, len(arr)):
            #slide the window by removing j-k and adding j 
            sumw = sumw - arr[j-k] + arr[j]
            #keep recording 
            if sumw/k >= threshold:
                count+=1
        
        return count

        
        
        