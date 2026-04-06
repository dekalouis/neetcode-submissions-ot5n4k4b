class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # DO IT HERE
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(t)):

            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            
        return countS == countT