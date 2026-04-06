class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                idx = ord(c) - ord('a')
                count[idx] += 1

            sign = tuple(count)

            if sign not in res:
                res[sign] = []
            res[sign].append(word)

        return list(res.values())
