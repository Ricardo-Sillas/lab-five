import math

##################### Node for Doubly Linked List ###########################
class Node:
    def __init__(self, data, value):
        self.data = data
        self.value = value
        self.next = None
        self.previous = None

######################### Doubly Linked List ###############################
class DLL:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

# Method to add the new node to the end, making it the most recently used.
    def add_last(self, node):
# If list is empty>
        if not self.head:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            temp.next = node
            node.previous = temp
            node.next = None
            self.tail = node

# Method to remove the Least Recently Used.
    def remove_first(self):
        temp = self.head.next
        self.head = temp
        temp.previous = None

# Method to relocate node if the key is already in the cache.
    def relocate(self, node):
        if node is self.tail:
            return
        temp_n = node.next
        if node is self.head:
            if temp_n:
                temp_n.previous = None
                self.head = temp_n
            self.add_last(node)
            return
        temp_p = node.previous
        temp_p.next = node.next
        temp_n.previous = temp_p
        self.add_last(node)

####################################### LRU ######################################
class LRU:
    def __init__(self, capacity):
        self.LRU = {}
        self.capacity = capacity
        self.list = DLL()
        self.size = 0

    def get(self, key):
        if key in self.LRU:
            self.list.relocate(self.LRU[key])
            return self.LRU[key]
        return -1

    def put(self, key, value):
        node = Node(key, value)
# If key is not in the cache.
        if key not in self.LRU:
            self.LRU[key] = node
            if self.size != self.capacity:
                self.size += 1
                self.list.add_last(node)
            else:
                self.list.remove_first()
                self.list.add_last(node)
# If key is in the cache.
        else:
            self.list.relocate(self.LRU[key])
            self.list.tail.value = value

    def sizes(self):
        return self.size

    def max_capacity(self):
        return self.capacity

    def print_list(self):
        a = self.list.head
        while a:
            print(a.data, a.value)
            a = a.next

############################## Max Heap ##############################
class MaxHeap:
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def _percolate_up(self, i):
        if i == 0:
            return
        pi = (i - 1) // 2
        if self.tree[pi] < self.tree[i]:
            self.tree[i], self.tree[pi] = self.tree[pi], self.tree[i]
            self._percolate_up(pi)

    def _percolate_down(self, i):
        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return
        mci = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2
        self.tree[i], self.tree[mci] = self.tree[mci], self.tree[i]
        self._percolate_down(mci)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self._percolate_down(0)
        return root

# Sorting using the Max Heap class
def heap_sort(lists):
    heap = MaxHeap()
    for a in lists:
        heap.insert(a)
    i = 0
    while not heap.is_empty():
        lists[i] = heap.extract_max()
        i += 1


def most_frequent_element(arr, k):
    dict = {}
    lists = list()
    most = list()
    mosts = list()
# Creating dictionary with words/letters as keys, and the number of occurrence as values
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
# Putting the number of occurrence into a list
    for i in dict:
        lists.append(dict[i])
    heap_sort(lists)
    print(lists)
# Gets the key corresponding with the occurrence and alphabetizing those with same occurrences
    i = 0
    while i < len(lists):
        l = i
        for j in dict:
            if lists[l] == dict[j]:
                mosts.append(j)
                i += 1
        mosts.sort()
        for m in range(len(mosts)):
            most.append(mosts[m])
        mosts.clear()

    if len(mosts) != 0:
        mosts.sort()
        for m in range(len(mosts)):
            most.append(mosts[m])
    if k > len(lists) or k < 0:
        print("Error: k Out of Bounds")
        return
    for i in range(k):
        print(most[i])



def main():
    s = ["a", "a", "a", "b", "B", "c"]
    most_frequent_element(s, 2)
    s1 = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o"]
    s2 = ["view", "blue", "apple"]
    most_frequent_element(s2, 6)
    s3 = ["a", "e", "b", "e", "b", "d", "f", "a", "c", "e", "u", "g", "l"]
    most_frequent_element(s3, 5)
    # lru = LRU(4)
    # lru.put("a", 4)
    # lru.print_list()
    # print("____")
    # lru.put("N", 10)
    # lru.print_list()
    # print("____")
    # lru.put("C", 99)
    # lru.print_list()
    # print("____")
    # lru.get("a")
    # lru.print_list()
    # print("____")
    # lru.put("F", 42)
    # lru.print_list()


main()
