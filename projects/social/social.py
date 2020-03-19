import random
from graph import Graph
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # To create N random friendships,
        # you could create a list with all possible friendship combinations,
        # shuffle the list, then grab the first N elements from the list.
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        # Create n friendships where n = avg_friendships * num_users // 2
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
     #BFS shortest path

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue= Queue()
        #a list for path
        queue.enqueue([user_id]) 

        #while something in queue
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # GRAB THE last user FROM THE END OF THE PATH. last item in path
            friend = path[-1]

            # If user id key hasn't been visited...
            if friend not in visited:      
         #The key is the friend's ID and the value is the path.  
        #add user id to visited dict key
        #store current path in dict as value
                visited[friend] = path
                # Enqueue A PATH TO all it's neighbors
                #friendships of current user
                #friendship adjanceny list directly
                for neighbor in self.friendships[friend]:
                    # MAKE A COPY OF THE PATH        
                    new_path = list(path)
                    #add 
                    new_path.append(neighbor)  
                    # ENQUEUE THE COPY
                    queue.enqueue(new_path)

            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)