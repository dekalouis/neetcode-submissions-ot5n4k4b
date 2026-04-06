class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            potential = target - nums[i]
            if potential in count:
                return [count[potential], i]
            else:
                count[nums[i]] = i
        return []
