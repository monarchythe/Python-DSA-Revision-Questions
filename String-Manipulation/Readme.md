# Notes 

## LC 20 — Valid Parentheses

> [!TIP]
> **Close must match the most recent open → stack.**

```python
pairs = {')': '(', ']': '[', '}': '{'}
stack = []

for char in s:
    if char in pairs:
        if not stack or stack[-1] != pairs[char]:
            return False
        stack.pop()
    else:
        stack.append(char)

return not stack
```

**Rules:** open → push · close → must match top, then pop · end → stack empty

**Why not a counter?** `"(]"` and `")("` both balance to 0 but are invalid.

### Stack in Python

```python
stack.append(x)   # push
stack[-1]         # peek
stack.pop()       # remove top (no argument)
not stack         # empty?
```

⚠️ Check `not stack` before `stack[-1]` — peeking empty crashes.
