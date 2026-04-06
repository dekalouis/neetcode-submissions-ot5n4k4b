class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initiate l, r, also add res at 0, then loop while l < r,
        # calculate the area, which is the min of heights l and heights r, MULTIPLY the min by r-l
        # updae the res to be max of res and area. 
        # if leftheight is less than/equal to right height, more l forward, else move r backwards
        # return res

        l = res = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res