class Node {
    constructor(val, next = null) {
        this.val = val
        this.next = next
    }
}

class LinkedList {
    constructor() {
        this.head = new Node(-1) //add dummy
        this.tail = this.head 
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) { // just a simple traversing and returning the value at the index 
        let curr = this.head.next // start at actual head (not dummy)
        let i = 0 //create an index (counter)
        while (curr) { //as long as current still has value (notnull) means we traverse
            if (i === index) { //if the index matches the counter, return currs value
                return curr.val
            } 
            i++ //otherwise keep increasing the i, and keep going inside curr's next
            curr = curr.next
        }
        return -1 // if we go past the last curr's index, we return -1 (out. of bounds)
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) { //inserting a new value at the head
        let newNode = new Node(val) //create the new node
        newNode.next = this.head.next //make the newnode POINT to the real head (since we have dummy at head)
        this.head.next = newNode //we change the head to be the newnode (again its the next bcs of dummy)
        if (this.head === this.tail) { // if the list is empty
            this.tail = newNode //then the tail should also be the newNode
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let newNode = new Node(val) //create the new node
        this.tail.next = newNode //make the last node (current tail) Point to the new node
        this.tail = newNode //then update the tail so that it's the new node 
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) { // removing node at a certain index
        //dummy -> 1 -> 2 -> 3 -> 4 
        let i = 0 // start the counter
        let curr = this.head // start at the dummy head, and traverse
        while (i < index && curr) { // as long as i is not at index, and curr.next is not null
            curr = curr.next //replace current with the next value
            i++ //keep adding i
        } // we now reach the index

        //this is the actual removal
        if (curr && curr.next) { // if the current node and the next has value
            if (curr.next === this.tail) { //if the next node is the tail
                this.tail = curr // just replace the tail with this node
            }

            curr.next = curr.next.next
            return true 
        }
        return false



    }

    /**
     * @return {number[]}
     */
    getValues() {
        let curr = this.head.next //start with real noce
        let res = []
        while (curr) {
            res.push(curr.val) 
            curr = curr.next
        }
        return res
    }
}
