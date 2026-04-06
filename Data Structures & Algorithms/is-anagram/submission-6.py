class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for c in s:
            if c not in countS:
                countS[c] = 0
            countS[c]+=1
            
        for c in t:
            if c not in countT:
                countT[c] = 0
            countT[c]+=1

        return countS == countT