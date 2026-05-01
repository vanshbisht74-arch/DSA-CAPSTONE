# Final Capstone :
# Social Network Explorer

# Aim :
# Build a mini social network using DSA concepts.

# Features :
# Profiles (hashing)
# Graph (connections)
# BFS (shortest path)
# DFS (exploration)


from collections import deque

class SocialNetwork:
    def __init__(self):
        self.users = {}     # profiles
        self.graph = {}     # connections

    # add user
    def add_user(self, name, interests):
        self.users[name] = interests
        self.graph[name] = []

    # add connection
    def add_friend(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # remove connection
    def remove_friend(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    # BFS shortest path
    def bfs(self, start, end):
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == end:
                return path

            if node not in visited:
                visited.add(node)

                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    # DFS exploration
    def dfs(self, node, visited, depth):
        if depth == 0:
            return
        print(node, end=" ")
        visited.add(node)

        for n in self.graph[node]:
            if n not in visited:
                self.dfs(n, visited, depth - 1)


# ----------------------------------
# DEMO
# ----------------------------------

sn = SocialNetwork()

sn.add_user("A", ["music", "sports"])
sn.add_user("B", ["music"])
sn.add_user("C", ["sports"])
sn.add_user("D", ["tech"])
sn.add_user("E", ["music"])
sn.add_user("F", ["tech"])

sn.add_friend("A", "B")
sn.add_friend("A", "C")
sn.add_friend("B", "D")
sn.add_friend("C", "E")
sn.add_friend("D", "F")

print("Shortest path A to F:", sn.bfs("A", "F"))

print("DFS from A depth 2:", end=" ")
sn.dfs("A", set(), 2)


# Reason :
# Uses hashing + graph + BFS + DFS → real system simulation.


# Viva :
# 1. BFS use?
# Shortest path

# 2. DFS use?
# Explore network

# 3. Why hashing?
# Fast profile access