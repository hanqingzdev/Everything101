"""
Implement hash table by array data structure.
"""
class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, size=100):
        self.hashed = [None] * size
        self.hash = lambda key: key % size
        self.size = 0

    def put(self, key, val):
        pos = self.hash(key)
        newNode = Node(key, val)

        node = self.hashed[pos]
        if node is None:
            self.hashed[pos] = newNode
            self.size += 1
        else:
            while node.key != key and node.next:
                node = node.next

            if node.key == key:
                node.val = val
            else:
                node.next = newNode
                self.size += 1

    def get(self, key):
        pos = self.hash(key)
        node = self.hashed[pos]

        while node:
            if node.key == key:
                return node.val
            else:
                node = node.next

        return None


    def remove(self, key):
        pos = self.hash(key)
        node = self.hashed[pos]

        dumHead = Node(None, None, node)
        previous = dumHead

        while node:
            if node.key == key:
                previous.next = node.next
                self.size -= 1
                break
            else:
                node = node.next
                previous = node

        self.hashed[pos] = dumHead.next
