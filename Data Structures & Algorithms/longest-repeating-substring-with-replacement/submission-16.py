class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxfreq, res = 0, 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfreq = max(count[s[r]], maxfreq)
            
            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            res = r - l + 1
        return res