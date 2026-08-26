impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = vec![];
        nums.sort();
        let n = nums.len();

        for i in 0..n {
            let num = nums[i];
            if num > 0 {
                break;
            }

            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let mut l = i + 1;
            let mut r = n - 1;

            while l < r {
                let mut tsum = nums[l] + nums[r] + num;
                if tsum > 0 {
                    r -= 1;
                } else if tsum < 0 {
                    l += 1;
                } else {
                    res.push(vec![nums[l], nums[r], num]);
                    l += 1;
                    r -= 1;
                    while nums[l] == nums[l - 1] && l < r {
                        l += 1;
                    }
                }
            }
        }
        res


    }
}
