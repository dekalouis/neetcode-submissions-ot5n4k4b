class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if num - 1 not in numset: 
                length = 1
                print(f'current num {num}, length is {length} is nextnum {num + 1} in numset?')
                while (num + length) in numset: 
                    print(f'yes, adding length, current length = {length}, added to {length + 1}')
                    length += 1
                longest = max(length, longest)
        return longest