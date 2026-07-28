class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            count = [0] * 26

            for c in word: 
                idx = ord(c) - ord('a')
                count[idx] += 1

            # print(count)
            sign = tuple(count)
            # print(sign)
            if sign not in res: 
                res[sign] = []
            res[sign].append(word)

        # print(res)
        return list(res.values())
            


        
            
