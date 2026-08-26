impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![1; nums.len()];
        let mut prefix = 1;
        let mut suffix = 1;
        let length = nums.len();

        for i in 0..length {
            res[i] = prefix;
            prefix *= nums[i];
        }

        for i in (0..length).rev() {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        res
    }
}
