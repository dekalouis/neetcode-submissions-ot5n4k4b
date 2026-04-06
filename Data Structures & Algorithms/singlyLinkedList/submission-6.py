class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        idx = 0
        while current:
            if idx == index:
                return current.val
            current = current.next
            idx += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # new_node = Node(val)
        self.tail.next = Node(val)
        self.tail = self.tail.next

        
    def remove(self, index: int) -> bool:
        idx = 0
        current = self.head
        while idx < index and current:
            idx += 1
            current = current.next
            
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

        

    def getValues(self) -> List[int]:
        result = []
        current = self.head.next
        while current:
            result.append(current.val)
            current = current.next
        return result

        
