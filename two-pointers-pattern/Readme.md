
# The 2 pointer Pattern has below questions 

### Core (must do — 7):

- 125 Valid Palindrome — warmup, opposite-ends pattern
- 392 Is Subsequence
- 167 Two Sum II — sorted array, opposite-ends
- 11 Container With Most Water — greedy shrink decision
- 15 3Sum — the classic, teaches sort + fix + two-pointer
- 16 3Sum Closest — variant of 15
- 1768 Merge Strings Alternately — same-direction two-pointer

### Recommended (2):
- 7. 881 Boats to Save People — greedy + two-pointer
- 8. 2563 Count Number of Fair Pairs — two-pointer + binary search hybrid, common interview pattern

### Skip / low value:

- 344 Reverse String — too trivial, done in 2 min, no learning
- 455 Assign Cookies — greedy, not really two-pointer
- 18 4Sum — just 3Sum with an extra loop, learn nothing new after 15
- 1679 Max Number of K-Sum Pairs — hashmap problem, not two-pointer
- 2491 Divide Players — trivial after sorting, not worth it

8 problems is enough to cover: opposite-ends, same-direction, sort-and-fix, greedy shrink. That's the full pattern.

Order to attack: 125 → 167 → 11 → 1768 → 15 → 16 → 881 → 2563. Warmups first, hardest last.


# Notes , for revision

### LC 1 — Two Sum

> [!TIP]
> **Store what you've seen, look up what you need.**

### Idea
For each `num`, the partner needed is `target - num`.
Check the map for it **before** storing `num`.

```python
seen = {}                      # value -> index
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        return [seen[diff], i]
    seen[num] = i
```

### Dry run — `nums = [3, 8, 2, 7, 5]`, `target = 9`

| i | num | diff | in map? | map |
|---|---|---|---|---|
| 0 | 3 | 6 | no | `{3:0}` |
| 1 | 8 | 1 | no | `{3:0, 8:1}` |
| 2 | 2 | 7 | no | `{3:0, 8:1, 2:2}` |
| 3 | 7 | 2 | ✅ | return `[2, 3]` |

### Remember
- **Check before store** → a number can't pair with itself
- Map is `value → index`, not the other way
- Brute force O(n²) → hashmap **O(n) time, O(n) space**
