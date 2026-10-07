class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            # print("current")
            # print(f"l pos {l} val {s[l]}") 
            # print(f"r pos {r} val {s[r]}")
            # print(f"longest {longest}")
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

        
