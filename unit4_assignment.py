# Unit 4 Assignment :
# BST + Graph + BFS + DFS + Hash Table

# Aim :
# Combine multiple data structures and algorithms in one program.

# What you will implement :
# BST (insert, search, delete, inorder)
# Graph (adjacency list)
# BFS and DFS traversal
# Hash Table with chaining

# ----------------------------------
# BST IMPLEMENTATION
# ----------------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)

    return search(root.right, key)


def find_min(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)

    elif key > root.val:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root


# ----------------------------------
# GRAPH + BFS + DFS
# ----------------------------------

from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
    print()


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for n in graph[node]:
            dfs(graph, n, visited)


# ----------------------------------
# HASH TABLE
# ----------------------------------

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        self.table[self.hash_func(key)].append((key, value))

    def get(self, key):
        for k, v in self.table[self.hash_func(key)]:
            if k == key:
                return v
        return None

    def delete(self, key):
        bucket = self.table[self.hash_func(key)]
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)


# ----------------------------------
# DEMO RUN
# ----------------------------------

# BST
root = None
for v in [5, 3, 7, 2, 4, 6, 8]:
    root = insert(root, v)

print("BST inorder:", end=" ")
inorder(root)
print("\nSearch 4:", "Found" if search(root, 4) else "Not Found")

root = delete(root, 7)
print("After delete:", end=" ")
inorder(root)
print()

# Graph
bfs(graph, 1)
print("DFS:", end=" ")
dfs(graph, 1, set())
print()

# Hash Table
ht = HashTable(5)
ht.insert(1, "A")
ht.insert(6, "B")
ht.insert(11, "C")

print("Hash Get 6:", ht.get(6))
ht.delete(6)
print("After delete 6:", ht.get(6))


# Reason :
# Combines tree, graph, hashing → real-world system building.


# Viva :
# 1. Why BST?
# Fast search O(log n)

# 2. BFS vs DFS?
# BFS level, DFS depth

# 3. Hash collision?
# Same index → handled by chaining