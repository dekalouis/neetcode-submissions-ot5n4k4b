class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            count = [0] * 26

            for c in word: 
                idx = ord(c) - ord('a')
                count[idx] += 1
            # print(count)

            signature = tuple(count)
            # print(signature)

            if signature not in res:
                res[signature] = []
            res[signature].append(word)
            # print(res)

        return list(res.values())
            
