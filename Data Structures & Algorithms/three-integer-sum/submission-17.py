class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        # print(nums)
        for i, val in enumerate(nums):
            if val > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                tsum = nums[l] + nums[r] + val
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else: 
                    res.append([nums[l], nums[r], val])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+= 1
        return res
                        
                