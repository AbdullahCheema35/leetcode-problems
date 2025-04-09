from typing import Dict, Optional, cast

class Node:
    
    def __init__(self, val=0, key=0, prev=None, next=None):
        self.value: int = val
        self.key: int = key
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.map: Dict[int, Node] = {}
        self.length = 0
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.put(key=key, value=node.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            old_node = self.map[key]
            self.remove(key, old_node)

        node = Node(val=value, key=key, prev=self.tail.prev, next=self.tail)
        assert node.prev is not None and node.next is not None
        node.next.prev, node.prev.next = node, node
        self.map[key] = node
        self.length += 1
        if self.length > self.capacity:
            lru_node = self.head.next
            assert lru_node is not None
            self.remove(key=lru_node.key, node=lru_node)

    def remove(self, key: int, node: Node) -> None:
        assert node.prev is not None and node.next is not None
        node.prev.next, node.next.prev = node.next, node.prev
        del self.map[key]
        self.length -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)