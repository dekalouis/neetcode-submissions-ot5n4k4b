class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            print(f'current num {num}')
            if num - 1 not in numset:
                print(f'current num {num} - 1 = {num - 1} NOT in numset, so this is the start, len = 1')
                length = 1
                while num + length in numset:
                    print(f'since num + length is {num + length} and is IN the numset, we add length')
                    length += 1
                longest = max(longest, length)
                print(f'we calculate longest by the max length value which is now {longest}')
        return longest