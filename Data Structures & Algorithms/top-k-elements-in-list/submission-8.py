class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num, cnt in count.items():
            # print(num, cnt)
            freq[cnt].append(num)
        
        # print(freq)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res