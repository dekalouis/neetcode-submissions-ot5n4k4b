class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            num = nums[i]
            potential = target - num
            if potential in hash: 
                return [hash[potential], i]
            else:
                hash[num] = i
        return []
                
            
            