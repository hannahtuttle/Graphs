import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
        for user in range(num_users):
            self.add_user(user)
        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)
        # then shuffle it randomly
        random.shuffle(possible_friendships)
        # and ony take as many as we need,
        total_friendships = num_users * avg_friendships //2
        random_friendships = possible_friendships[:total_friendships]
        # and add those friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])
    
    def get_neighbors(self, user_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # print(self.friendships[user_id])
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        # do a bfs and save the last node to the disctionary as a key and then save the shortest path as a value
                # make a queue
        print('user_id',user_id)
        queue = Queue()
        # Note that this is a dictionary, not a set
        visited = {}  
        # enqueues a Path To the starting_vertex
        queue.enqueue([user_id])
        # while queue isn't empty:
        while queue.size() > 0:
            # dequeue the next path
            path = queue.dequeue()
            # current_node is the last thing in the path
            current_node = path[-1]
            # print('current_node', current_node)
            # else mark this as visited
            if current_node not in visited:
                visited[current_node]= path
                # get the neighbors
                edges = self.get_neighbors(current_node)
                # for each one, ad a Path To IT to the queue
                for edge in edges:
                    print('edge', edge)
                    new_path = list(path)
                    new_path.append(edge)
                    queue.enqueue(new_path)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
