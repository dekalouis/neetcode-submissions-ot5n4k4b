class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let read = 1
        let write = 1

        while (read < nums.length) {

            if (nums[read] !== nums[read-1]) {
                nums[write] = nums[read]
                write++
                read++
            } else {
                read++
            }
        }
        return write
    }
}
