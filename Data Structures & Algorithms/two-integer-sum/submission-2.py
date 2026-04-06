class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            pot = target - nums[i]

            if pot in hash:
                return [hash[pot], i]
            else:
                hash[nums[i]] = i
        return []