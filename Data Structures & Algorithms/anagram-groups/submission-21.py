class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            freq = [0] * 26

            for c in word: 
                idx = ord(c) - ord('a')
                freq[idx] += 1
            
            # print(freq)
            signature = tuple(freq)

            if signature not in res: 
                res[signature] = []
            res[signature].append(word)
        # print(res)
        return list(res.values())



        
            
