class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize 0 res, and a set of the string,
        # loop each char from the set (outer loop), init count and left pointer at 0 
        # then loop with r pointer to the string length,
        # if the right value = char, add the count,
        # while r - l + 1 (total length) - count > k, 
        # check if left value = char, if yes reduce count
        # increment left pointer
        # still in INNER loop outside the while, find the result, which is the max res and total length
        # return res.



        res = 0 
        charset = set(s)

        for char in s:
            count = l = 0

            for r in range(len(s)):
                if s[r] == char:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res