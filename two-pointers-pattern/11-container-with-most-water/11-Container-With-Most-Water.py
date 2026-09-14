class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1

        max_w = 0

        while i<j:
            
            max_w = max(max_w, (j-i) * min(arr[i], arr[j]))

            if arr[i]<= arr[j]:
                i+=1
            else:
                j-=1

        return max_w



# The trick is: at each step, which pointer do you move? Think about it — if the two heights are different, moving the taller one can never help (why?). That's the whole insight.

            # x_length = j-i
            # min_y_length = min(arr[i], arr[j])

            # total_area = x_length * min_y_length

            # max_w = max(max_w, total_area)