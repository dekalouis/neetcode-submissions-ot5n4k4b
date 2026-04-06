class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        result = 0
        charCount = {}

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxFreq = max(maxFreq, charCount[s[r]])

            while (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1

            result = r - l + 1
        return result