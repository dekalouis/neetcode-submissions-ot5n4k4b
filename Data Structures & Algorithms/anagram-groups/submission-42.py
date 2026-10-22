class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for s in strs:
            freq = [0] * 26

            for c in s: 
                idx = ord(c) - ord('a')
                freq[idx] += 1

            sign = tuple(freq)

            if sign not in count:
                count[sign] = []
            count[sign].append(s)

        return list(count.values())