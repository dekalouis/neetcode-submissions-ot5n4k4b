class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize empty hash for the count, initialzie the frequency buckets (+1 because 0 ignored)
        # loop for num in nums, add them to the count hash if not there and increment
        # then loop num and the cnt for each count.items, and push the num to the cnt of the freq
        # finally make res, and loop backwards from freq to 0, inside, loop for each number in the ith freq
        # push the num to the res. if the length matches, return

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res