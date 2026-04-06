class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] = counts[n] + 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num in counts:
            freq = counts[num]
            buckets[freq].append(num)

        res = []
        for f in range(len(buckets) - 1, -1, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res

        return res