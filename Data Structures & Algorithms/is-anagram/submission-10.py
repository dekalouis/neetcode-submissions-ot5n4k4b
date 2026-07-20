class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # DO IT HERE
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)): 
            if s[i] not in hashS:
                hashS[s[i]] = 0
            if t[i] not in hashT:
                hashT[t[i]] = 0
            hashS[s[i]] += 1
            hashT[t[i]] += 1
        return hashS == hashT
            
