import time
import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BalancedBST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root
    
    def find(self, key):
        return self._find(self.root, key)
    
    def _find(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._find(root.left, key)
        return self._find(root.right, key)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


def generate_random_bst(size):
    bst = BalancedBST()
    keys = random.sample(range(1, 10000000), size)
    for key in keys:
        bst.insert(key)
    return bst


def measure_time(func):
    before = time.time()
    func()
    return time.time() - before


stats = []
for _ in range(100):
    size = random.randint(10, 1000000)
    tree = generate_random_bst(size)
    stats.append((size, tree))

stats.sort(key=lambda item: item[0])
for size, tree in stats:
    find_time = measure_time(lambda: tree.find(random.randint(1, 1000)))
    insert_time = measure_time(lambda: tree.insert(random.randint(1, 1000)))
    delete_time = measure_time(lambda: tree.delete(random.randint(1, 1000)))
    print(f"size - {size}\n  - find time: {find_time:.8f}\n  - insert time: {insert_time:.8f}\n  - delete time: {delete_time:.9f}")

    