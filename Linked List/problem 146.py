class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key -> node mappings

        # left (least recently used) and right (most recently used)
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # connect left and right initially
        self.left.next = self.right
        self.right.prev = self.left

    # Function to remove a node from the linked list
    def remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    # Function to insert a node at the most recently used position (before tail)
    def insert(self, node):
        last_node = self.right.prev  # node right before the right Node

        last_node.next = node
        node.prev = last_node

        node.next = self.right
        self.right.prev = node

    # Function to get a value from the cache
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Remove from current position
            self.insert(node)  # Move to most recently used position
            return node.value
        return -1  # Key not found

    # Function to put a key-value pair into the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            existing_node = self.cache[key]
            self.remove(existing_node)  # Remove old node

        new_node = Node(key, value)
        self.cache[key] = new_node  # Store new node in dictionary
        self.insert(new_node)  # Insert at most recently used position

        if len(self.cache) > self.capacity:
            # Remove least recently used node (first real node after head)
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]  # Remove from dictionary


lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4

'''
the reason we need both key and value in linked list

is that the key makes it easy to delete in the cache if we exceed capactiy
'''