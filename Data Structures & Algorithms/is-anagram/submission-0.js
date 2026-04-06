class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let seen_s = {}
        let seen_t = {}
        for (let char of s) {
            if (!seen_s[char]) {
                seen_s[char] = 0
            }
            seen_s[char]++
        }
        for (let char of t) {
            if (!seen_t[char]) {
                seen_t[char] = 0
            }
            seen_t[char]++
        }
        function deepEqual(x, y) {
            const ok = Object.keys, tx = typeof x, ty = typeof y;
            return x && y && tx === 'object' && tx === ty ? (
            ok(x).length === ok(y).length &&
            ok(x).every(key => deepEqual(x[key], y[key]))
            ) : (x === y);

}
  return deepEqual(seen_s, seen_t)

       
    }
}
