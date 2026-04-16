# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # initiate the length as n, store the res list, 
        # loop i in range of the length, then initiate j, which is the number before the current i
        # do an inner while loop, when j >= 0, and the key of j in pairs is more than the key on the right, 
        # swap it, and then move j backwards to ensure we compare the moved element with its new left neighbour
        # outside the inner loop, append the new pair as a shallow copy, so we dont get the same value for each.
        # return res. (in a regular insertion we return the pair directly)
        
        n = len(pairs)
        res = []

        for i in range(n):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            res.append(pairs[:])
        return res