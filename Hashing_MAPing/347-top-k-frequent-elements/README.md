# 347. Top K Frequent Elements

🟡 **Medium** &nbsp;|&nbsp; [View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

---

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,2,2,3], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2,1,2,3,1,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>


---

**My Solution:** [347-Top-K-Frequent-Elements.py](./347-Top-K-Frequent-Elements.py)



## LC 347 — Top K Frequent Elements

> [!TIP]
> **Count, then rank.** Frequency map → sort keys by their counts → take first k.

### Code

```python
hash_map = {}
for num in nums:                        # no need to sort first
    hash_map[num] = hash_map.get(num, 0) + 1

return sorted(hash_map, key=hash_map.get, reverse=True)[:k]
```

### Shortcut

```python
from collections import Counter
return [num for num, _ in Counter(nums).most_common(k)]
```

`most_common(k)` returns `(num, count)` pairs → pull out just the nums.

---

## Concept: `sorted()` with `key=`

> [!IMPORTANT]
> `sorted()` **always returns a list** — never a dict, even if you pass a dict.

### What looping over each input gives you

| You pass | `sorted()` returns |
|---|---|
| `hash_map` | list of **keys** |
| `hash_map.items()` | list of **(key, value)** tuples |
| `hash_map.values()` | list of **values** |

### Dry run — `hash_map = {1: 3, 2: 2, 3: 1}`, `k = 2`

```python
sorted(hash_map, key=hash_map.get, reverse=True)[:k]
```

| step | result |
|---|---|
| loop over dict → keys | `[1, 2, 3]` |
| `key=hash_map.get` → sort by counts | counts `3, 2, 1` |
| `reverse=True` → highest first | `[1, 2, 3]` |
| `[:k]` | `[1, 2]` |

### How `key=` works
`key=` takes a **function**. Each item runs through it; sorting uses the result.
The items themselves don't change.

- `key=hash_map.get` — no parentheses; pass the function, don't call it
- Same as `key=lambda k: hash_map[k]`

### Common uses

```python
sorted(words, key=len)                  # shortest first
sorted(pairs, key=lambda p: p[1])       # by 2nd element
sorted(names, key=str.lower)            # case-insensitive

# keys + counts together
sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
# → [(1, 3), (2, 2), (3, 1)]

# back to a dict
dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
```

### Remember
- `sorted()` in → **list** out, always
- Dict in → you get **keys**. Want counts too? Use `.items()`
- Time: **O(n log n)** from the sort
