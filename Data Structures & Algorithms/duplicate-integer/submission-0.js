class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen = {}
        for (let i = 0; i<nums.length; i++){
            if (!seen[nums[i]]) {
                seen[nums[i]] = 0
            }
            seen[nums[i]]++
            if (seen[nums[i]] > 1) {
                return true
            } 
        }
        return false
    }
}
