class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initiate l, maxfreq, res all 0, and count hashtable
        # loop r in range of s, add each s[r] to count
        # find maxfreq, which is the maximum of charcount[s[r]]
        # then, check while window - maxfreq > k (budget)
        # we reduce the count of s[l] window, and move l forward
        # outside, update res with window.

        l = res = maxfreq = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfreq = max(maxfreq, count[s[r]])

            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            res = (r - l + 1)
        
        return res


