class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            num = nums[i]
            pot = target - num
            if pot in hash:
                return [hash[pot], i]

            hash[num] = i
        
        return []