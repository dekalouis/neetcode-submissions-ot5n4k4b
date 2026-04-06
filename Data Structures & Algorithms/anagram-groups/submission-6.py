class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashtable, start with res and loop, create count and loop again to get the index and add to count
        # dont forget to tuple-ize the count so it can be a key that can be used in the res (res[key])
        res = {}
        
        for word in strs:
            count = [0] * 26

            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1

            sign = tuple(count)

            if sign not in res:
                res[sign] = []
            res[sign].append(word)
            
        return list(res.values())
