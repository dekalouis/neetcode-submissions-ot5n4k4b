class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let freqs = {}

        for (let i = 0; i < nums.length; i++) {
            let n = nums[i]
            if (freqs[n] === undefined) {
                freqs[n] = 0
            }
            freqs[n] = freqs[n] + 1;
        }

        let keys = Object.keys(freqs)

        keys.sort(function(a, b) {
            return freqs[b] - freqs[a]
        })

        let res = []
        for (let i = 0; i < k; i++) {
            res.push(Number(keys[i]))
        }
    return res
    }
}
