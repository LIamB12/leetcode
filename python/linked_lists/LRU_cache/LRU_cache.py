class Node:
    def __init__(self, val=None, key=None, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.ages_head = None
        self.ages_tail = None
        
    def get(self, key):
        
        if key not in self.cache:
            return -1

        node = self.cache.get(key)

        if len(self.cache) == 1:
            return node.val

        if node == self.ages_head:
            self.ages_head = node.next
            self.ages_head.prev = None
            self.ages_tail.next = node
            node.prev = self.ages_tail
            self.ages_tail = node
            node.next = None
            return node.val
        if node == self.ages_tail:
            return node.val
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.ages_tail.next = node
        node.prev = self.ages_tail
        self.ages_tail = node
        node.next = None
        return node.val
        
        
    def put(self, key, value):

        if key in self.cache:
            updated_node = self.cache.get(key)
            if len(self.cache) == 1:
                updated_node.val = value
                return

            if updated_node == self.ages_head:
                self.ages_head = updated_node.next
                self.ages_head.prev = None
                self.ages_tail.next = updated_node
                updated_node.prev = self.ages_tail
                self.ages_tail = updated_node
                updated_node.next = None
                updated_node.val = value

            elif updated_node == self.ages_tail:
                updated_node.val = value

            else:
                updated_node.prev.next = updated_node.next
                updated_node.next.prev = updated_node.prev
                self.ages_tail.next = updated_node
                updated_node.prev = self.ages_tail
                self.ages_tail = updated_node
                
                updated_node.next = None
                updated_node.val = value

        elif len(self.cache) == 0:
            new_node = Node(value, key, None, None)
            self.ages_head = new_node
            self.ages_tail = new_node
            self.cache[key] = new_node
        elif len(self.cache) < self.capacity:
            new_node = Node(value, key, self.ages_tail, None)
            self.ages_tail.next = new_node
            self.ages_tail = new_node
            self.cache[key] = new_node
        elif self.capacity == 1:
            new_node = Node(value, key, None, None)
            self.ages_head = new_node
            self.ages_tail = new_node
            self.cache = {key: new_node}
        else:
            new_node = Node(value, key, self.ages_tail, None)
            self.ages_tail.next = new_node
            self.ages_tail = new_node
            del self.cache[self.ages_head.key]
            self.ages_head = self.ages_head.next
            self.ages_head.prev = None
            self.cache[key] = new_node




