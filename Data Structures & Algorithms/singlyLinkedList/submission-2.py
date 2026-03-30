class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:

        if self.head == None:
            return -1
        
        current = self.head

        counter = 0
        while current:

            if counter == index:
                return current.value
            counter += 1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:

        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
        

    def insertTail(self, val: int) -> None:

        current = self.head

        if self.head == None:
            new_val = Node(val)
            self.head = new_val
            return None

        while current:
            if current.next == None:
                new_node = Node(val)
                current.next = new_node
                return None
            current = current.next
        

    def remove(self, index: int) -> bool:

        if self.head == None:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        
        current = self.head 
        current_idx = 0
        while current and current.next:
            if current_idx + 1 == index:
                current.next = current.next.next
                return True
            current = current.next
            current_idx += 1
        return False

        

    def getValues(self) -> List[int]:

        if self.head == None:
            return []
        
        value_list = []

        current = self.head

        while current:
            value_list.append(current.value)
            current = current.next
        
        return value_list