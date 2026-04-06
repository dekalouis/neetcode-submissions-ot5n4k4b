class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers, start with empty res array, dont forget to sort original array
        # loop through idx and val with enumerate, check val > 0(break), 
        # and if val is the same as the number before it, num[i-1](cont)
        # init l, r (l should be after val) then while pointer l < r, check the sum
        # finally in the else, append the 3 to res, move pointers inwards and 
        # loopwhile nums in l == the num before it, and l<r 
        # we move l inwards, and return res outside

        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break

            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

                    