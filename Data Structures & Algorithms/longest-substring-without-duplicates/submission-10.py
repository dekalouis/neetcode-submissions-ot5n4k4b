class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize the set, initialize left pointer and maxlength
        # loop r point to the length, here you want to add 
        # the right pointer to the set and looking for maxlen
        # where its between current maxlen and the difference of r-l + 1 (BECAUSE r - l = maxlen - 1)
        # example: abcde, l = 0, r = 4 -> 4-0 = 4 but the substring is 5 characters, add 1
        # but AFTER you loop while value of right pointer exist in the set,
        # you want to always remove it and move left forward.

        charset = set()
        l, maxlen = 0, 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen
            