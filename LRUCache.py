class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.dict[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        cur_tail = self.tail.prev
        self.tail.prev = node
        cur_tail.next = node
        node.prev = cur_tail
        node.next = self.tail

        return node.value



    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.get(key)
            self.tail.prev.value = value
            return

        if len(self.dict) == self.capacity:
            curHead = self.head.next
            self.dict.pop(curHead.key)
            self.head.next = curHead.next
            curHead.next.prev = self.head


        node =  Node(key, value)



        curTail = self.tail.prev
        self.tail.prev = node

        curTail.next = node
        node.next = self.tail
        node.prev = curTail


        self.dict[key] = node


if __name__ == '__main__':
    cache =  LRUCache(2 );

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)

    cache.put(3, 3)

    cache.get(2)
    cache.put(4, 4)

    cache.get(1)
    cache.get(3)

    cache.get(4)

    a = list()
    a.pop()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)