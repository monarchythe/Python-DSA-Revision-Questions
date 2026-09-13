# Python-DSA-Revision-Questions
After practicing DSA from Strivers sheet, I am making this repo for me to revise the questions before any Interview

## SLIDING WINDOW

- 3 Longest Substring Without Repeating Characters

- 76 Minimum Window Substring

- 209 Minimum Size Subarray Sum

- 424 Longest Repeating Character Replacement

- 713 Subarray Product Less Than K

- 904 Fruit Into Baskets

- 1004 Max Consecutive Ones III

- 1343 Number of Sub arrays of Size K and Average Greater than or Equal to Threshold

- 1438 Longest Continuous Subarray With Absolute Diff Less than or Equal to L

- 1456 Maximum Number of Vowels in a Substring of Given Length

- 2461 Maximum Sum of Distinct Subarrays With Length K

- 2958 Length of Longest Subarray With at Most K Frequency


we did ✅ 3, 76, 209, 424, 904, 1004, 1493 then - 

### Category Fixed-width (3):

- 1456 — Max Vowels
- 1343 — Subarrays of Size K with Avg ≥ Threshold — trivial variant of 1456, just check sum/k >= threshold
- 2461 — Max Sum of Distinct Subarrays of Length K — fixed-width + hashmap to track distinctness

### Variable-width (3) — different tracking logic each time:

- 713 — Subarray Product Less Than K — "count valid windows" variant, product instead of sum. Trickier: how you count matters.
- 2958 — Longest Subarray With At Most K Frequency — direct extension of LC 904 (limit on freq instead of distinct types)
- 1438 — Longest Continuous Subarray With Abs Diff ≤ Limit — variable-width but needs a monotonic deque to track min/max efficiently. This is the hardest !

#### Always remeber 

     for longest / largest / maximest  - WINDOW : we will :
     use inner while loop tp shrink the window till the  condition remains invalid
     and record lenght outside the inner loop
     squeeez the window untill it is valid

     for smallest / minimest - WINDOW : we will :
     use inner while loop tp shrink the window till the  condition remains valid
     and record lenght inside the inner loop 
     squeeez the window untill it breaks/is invalid
