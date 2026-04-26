class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashtable, start with res and loop, 
        # create count for each letter with 0 array, and then loop char in each word
        # to get the index and add to count, base it from ascii
        # dont forget to tuple-ize the count so it can be a key that can be used in the res (res[key]), 
        # check if exists in res, if not add [] and then append word
        # res at this point    
        # {
        #     (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
        #     (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
        #     (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']
        # }
        # return as list of res.values.
        res = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                idx = ord(c) - ord('a')
                count[idx] += 1

            signature = tuple(count)

            if signature not in res:
                res[signature] = []
            res[signature].append(word)

        return list(res.values())
            
            
            
            