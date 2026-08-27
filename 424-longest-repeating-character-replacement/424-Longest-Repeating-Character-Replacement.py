class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_fq, max_l = 0,0
        replacement_needed = 0 #(j-i+1 ) - max_fq
        i,j = 0,0
        h_map = dict()


        for j in range(len(s)):

            wd_size = j-i+1 
            h_map[s[j]] = h_map.get(s[j], 0)+1
            max_fq = max(h_map.values())

            replacement_needed = wd_size - max_fq

            while replacement_needed > k:
                h_map[s[i]] -=1
                i+=1
                max_fq = max(h_map.values())
                replacement_needed = j-i+1 - max_fq #new_window_size - new_max_freq
            
            if replacement_needed <= k:
                after_replacement = wd_size 
                max_l = max(max_l, j-i+1)
            

        return max_l

# Goal: longest substring where all chars are the same, with at most k replacements

# Key insight: don't decide what to replace into — just count: replacements_needed = window_size - max_frequency_in_window. If that's ≤ k, the window is valid

# Pattern: longest valid window → shrink while invalid, record outside

# Invalid condition: (j - i + 1) - max_freq > k

# Data structure: frequency hashmap to track char counts in current window, max(h_map.values()) for max frequency

# Shrink: decrement h_map[s[i]], move i, recalculate max_freq

# Same template as LC 3 and 904 — only the invalid condition and what we track changed