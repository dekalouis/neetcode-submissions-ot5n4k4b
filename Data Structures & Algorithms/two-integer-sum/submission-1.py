class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            num = nums[i]
            potential = target - num

            if num in hash:
                return [hash[num], i] 
            hash[potential] = i

        print(hash)
        