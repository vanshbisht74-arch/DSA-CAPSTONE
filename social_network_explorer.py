from collections import deque

# =========================
# USER PROFILE MANAGEMENT
# =========================

class User:
    def __init__(self, username, age, interests):
        self.username = username
        self.age = age
        self.interests = interests

    def __str__(self):
        return f"""
Username : {self.username}
Age      : {self.age}
Interests: {', '.join(self.interests)}
"""


# =========================
# SOCIAL NETWORK GRAPH
# =========================

class SocialNetwork:
    def __init__(self):
        self.users = {}      # Hash Map
        self.graph = {}      # Adjacency List

    # ---------------------
    # ADD USER
    # ---------------------
    def add_user(self, username, age, interests):

        if username in self.users:
            print("User already exists!")
            return

        self.users[username] = User(username, age, interests)
        self.graph[username] = []

        print(f"{username} added successfully!")

    # ---------------------
    # GET PROFILE
    # ---------------------
    def get_profile(self, username):

        if username not in self.users:
            print("User not found!")
            return

        print(self.users[username])

    # ---------------------
    # UPDATE PROFILE
    # ---------------------
    def update_profile(self, username, age=None, interests=None):

        if username not in self.users:
            print("User not found!")
            return

        if age:
            self.users[username].age = age

        if interests:
            self.users[username].interests = interests

        print("Profile updated successfully!")

    # ---------------------
    # ADD FRIENDSHIP
    # ---------------------
    def add_friendship(self, user1, user2):

        if user1 not in self.users or user2 not in self.users:
            print("One or both users not found!")
            return

        if user2 not in self.graph[user1]:
            self.graph[user1].append(user2)

        if user1 not in self.graph[user2]:
            self.graph[user2].append(user1)

        print(f"Friendship added between {user1} and {user2}")

    # ---------------------
    # REMOVE FRIENDSHIP
    # ---------------------
    def remove_friendship(self, user1, user2):

        if user2 in self.graph[user1]:
            self.graph[user1].remove(user2)

        if user1 in self.graph[user2]:
            self.graph[user2].remove(user1)

        print(f"Friendship removed between {user1} and {user2}")

    # ---------------------
    # VIEW FRIENDS
    # ---------------------
    def get_friends(self, username):

        if username not in self.users:
            print("User not found!")
            return

        print(f"Friends of {username}:")
        print(self.graph[username])

    # =========================
    # BFS SHORTEST PATH
    # =========================

    def shortest_path(self, start, end):

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

        return None

    # =========================
    # DFS EXPLORATION
    # =========================

    def dfs_explore(self, start, depth):

        visited = set()

        def dfs(node, current_depth):

            if current_depth > depth:
                return

            visited.add(node)

            for neighbor in self.graph[node]:

                if neighbor not in visited:
                    dfs(neighbor, current_depth + 1)

        dfs(start, 0)

        visited.remove(start)

        return visited

    # =========================
    # FRIEND RECOMMENDATION
    # =========================

    def recommend_friends(self, username):

        if username not in self.users:
            print("User not found!")
            return

        recommendations = []

        user_interests = set(self.users[username].interests)

        for other_user in self.users:

            if other_user == username:
                continue

            if other_user in self.graph[username]:
                continue

            other_interests = set(self.users[other_user].interests)

            common = user_interests.intersection(other_interests)

            if common:
                recommendations.append(
                    (other_user, len(common))
                )

        recommendations.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return recommendations


# =========================
# MAIN PROGRAM
# =========================

sn = SocialNetwork()

# ADD USERS
sn.add_user("Vansh", 19, ["Coding", "AI", "Gaming"])
sn.add_user("Aman", 20, ["Music", "Gaming", "Football"])
sn.add_user("Riya", 18, ["AI", "Reading", "Coding"])
sn.add_user("Karan", 21, ["Cricket", "Gaming"])
sn.add_user("Neha", 19, ["Music", "AI"])
sn.add_user("Rahul", 20, ["Coding", "Football"])
sn.add_user("Priya", 18, ["Reading", "Music"])
sn.add_user("Arjun", 22, ["Gaming", "Coding"])

print("\n")

# UPDATE PROFILE
sn.update_profile("Aman", interests=["Music", "Gaming", "AI"])

print("\n")

# SHOW PROFILES
sn.get_profile("Vansh")
sn.get_profile("Aman")
sn.get_profile("Riya")

print("\n")

# ADD CONNECTIONS
sn.add_friendship("Vansh", "Aman")
sn.add_friendship("Vansh", "Riya")
sn.add_friendship("Aman", "Karan")
sn.add_friendship("Riya", "Neha")
sn.add_friendship("Rahul", "Arjun")
sn.add_friendship("Priya", "Neha")
sn.add_friendship("Karan", "Rahul")
sn.add_friendship("Arjun", "Vansh")

print("\n")

# REMOVE CONNECTION
sn.remove_friendship("Karan", "Rahul")

print("\n")

# VIEW FRIENDS
sn.get_friends("Vansh")

print("\n")

# BFS SHORTEST PATH
path = sn.shortest_path("Vansh", "Neha")

print("Shortest Path:")
print(path)

print("\n")

# DFS EXPLORATION
print("DFS Exploration Depth 2:")
print(sn.dfs_explore("Vansh", 2))

print("\n")

print("DFS Exploration Depth 3:")
print(sn.dfs_explore("Vansh", 3))

print("\n")

# FRIEND RECOMMENDATION
print("Friend Recommendations for Vansh:")

recommendations = sn.recommend_friends("Vansh")

for user, score in recommendations:
    print(f"{user} -> {score} common interests")
