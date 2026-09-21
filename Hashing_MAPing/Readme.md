



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
