
# Notes

### `a_list[-1]` — last element
Negative indexing counts from the end: `-1` is last, `-2` second-to-last.
Use it when you want "the most recent thing I kept" — safe even as the list grows.
⚠️ Never index one list with another list's counter; they drift apart.

### `max()` — pick the further value
`max(a, b)` returns the larger. In merges: `end = max(old_end, new_end)`.
Without it, nested intervals break: `[[1,10],[2,3]]` → wrong `[1,3]` instead of `[1,10]`.

### `sort(key=lambda x: x[0])` — sort by a chosen field
`key=` takes a function; each item runs through it and sorts by the result.
`x[0]` = sort by first element. Plain `.sort()` on lists already compares element-by-element.
