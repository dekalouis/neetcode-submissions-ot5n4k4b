/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        // let count = 0

        const hash = new Set()
        while (head !== null) {
            if (hash.has(head)) {
                return true
            }
            hash.add(head)
            head = head.next
            // console.log("node", head.val, "next", head.next.val)
            // count++
        }
        return false
    }
}
