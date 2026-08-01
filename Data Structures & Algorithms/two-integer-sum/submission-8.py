class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            potential = target - nums[i]
            if potential in seen:
                return [seen[potential], i]
            if nums[i] not in seen: 
                seen[nums[i]] = i
            # print(seen)
        return []


            