class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hash = {}

        for (let i = 0; i<nums.length; i++) {
            if (!hash[nums[i]]) hash[nums[i]]=0
            hash[nums[i]]++

            if (hash[nums[i]] > 1) {
                return true
            }
        }

        return false
    }
}
