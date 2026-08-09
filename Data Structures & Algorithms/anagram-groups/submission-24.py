class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for word in strs: 
            freq = [0] * 26

            for c in word:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            
            # print(freq)

            sign = tuple(freq)

            if sign not in res:
                res[sign] = []
            res[sign].append(word)
        # print(res.values())
        return list(res.values())