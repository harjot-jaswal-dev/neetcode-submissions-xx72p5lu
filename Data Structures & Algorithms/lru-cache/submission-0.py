class NodeClass:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}
        self.head = NodeClass(0,0)
        self.tail = NodeClass(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        return node.value
        
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev

            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
        elif key not in self.cache and len(self.cache) < self.capacity:
            # node to add in the end of linked list, we dont remove or update the LRU
            node_to_add = NodeClass(key, value)

            self.cache[key] = node_to_add

            self.tail.prev.next = node_to_add
            node_to_add.prev = self.tail.prev
            node_to_add.next = self.tail
            self.tail.prev = node_to_add
        elif key not in self.cache and len(self.cache) >= self.capacity:

            # update head.next, we need to remove LRU here

            lur = self.head.next

            lur.prev.next = lur.next
            lur.next.prev = lur.prev

            # delete node from dict/cache

            self.cache.pop(lur.key)

            # node to add
            node_to_add = NodeClass(key, value)

            self.cache[key] = node_to_add

            self.tail.prev.next = node_to_add
            node_to_add.prev = self.tail.prev
            node_to_add.next = self.tail
            self.tail.prev = node_to_add

        
