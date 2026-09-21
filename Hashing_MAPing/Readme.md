



# Notes for revision:
## LC 49 — Group Anagrams

> [!TIP]
> **Anagrams share a signature.** Sort the letters → same key → same bucket.

### Idea
`"eat"`, `"tea"`, `"ate"` → sorted → `('a','e','t')`
Use that as the dict key. Value = list of words.

### What the map looks like

```python
{
    ('a', 'e', 't'): ['eat', 'tea', 'ate'],
    ('a', 'n', 't'): ['tan', 'nat'],
    ('a', 'b', 't'): ['bat'],
}
```

### Code

```python
hash_map = {}
for string in strs:
    key = tuple(sorted(string))       # list → tuple (hashable)
    if key in hash_map:
        hash_map[key].append(string)  # bucket exists → drop word in
    else:
        hash_map[key] = [string]      # new bucket
return list(hash_map.values())        # return buckets, not keys
```

### Remember
- `sorted("eat")` returns a **list** → wrap in `tuple()` or `"".join()`
- **Keys** must be immutable. **Values** can be anything, including lists
- `hash_map[key]` *is* the list → append to it directly
- Shortcut: `defaultdict(list)` skips the `if/else`
- Time: **O(n · k log k)** — n words, k = word length

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
