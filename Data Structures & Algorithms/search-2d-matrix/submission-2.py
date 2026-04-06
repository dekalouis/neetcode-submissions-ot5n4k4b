class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # declare row and col with the length of the matrix and matrix[0]
        # declare top and bot, which is 0 and row - 1
        # while top <= bot, replace row with top + bot // 2 to get midpoint
        # if the target is greater than the last item in that row, replace top with midpoint + 1
        # else if less than the first item in that row, replace bot with mid (row) - 1
        # otherwise break. then if top is not <= bot, return false, means number not inbetween any of the rows
        # then find midpoint again row = (top+bot)//2, and add pointer l, r (0 and cols - 1)
        # while loop again l <= r, find midpoint, l + r //2, 
        # check if target > the m of the matrix[row], move l to be m + 1, the reverse as well if target < matrix[row][m]
        # move r to be the m - 1, otherwise return true. after all that return false
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1

        while top <= bot: 
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break

        if not top <= bot:
            return False
        row = (top + bot) // 2
        l, r = 0, (col - 1)
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False