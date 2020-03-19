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

def get_neighbors(vertices, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return vertices[f'{vertex_id}']


def earliest_ancestor(ancestors, starting_node):
    # put all the ancestor pairs in a dictionary with all the parents in the value set()
    vertices = {}
    for pair in ancestors:
        # print('initial pair', pair)
        if vertices.get(f'{pair[1]}') == None:
            # print('pair[0]',pair)
            vertices[f'{pair[1]}'] = set(f'{pair[0]}')
            # print('vertices after adding a new key and value pair',vertices)
        if vertices.get(f'{pair[0]}') == None:
            # print('pair[1]',pair)
            vertices[f'{pair[0]}'] = set()
            # print('vertices after adding a new key',vertices)
        if vertices.get(f'{pair[1]}') != None and vertices.get(f'{pair[0]}') != None:
            # print('pair[0][1]',pair)
            vertices[f'{pair[1]}'].add(f'{pair[0]}')
            # print('vertices after adding new value',vertices)
    # traverse the vertices graph that was just created
    # use a queue to hold all the paths
    queue = Queue()
    # make a set for visited
    visited = set()
    # enqueues a Path To the starting_node
    queue.enqueue([starting_node])
    # creating a place to save the longest path
    longest_path = None
    # keep track of the length of each path
    length_path = 0
    # while queue isn't empty:
    while queue.size() > 0:
        # dequeue the next path
        path = queue.dequeue()
        # current_node is the last thing in the path
        current_node = path[-1]
        # get the length of the path
        current_path_length = len(path)
    # check to see if the previously saved path is shorter or longer to the longest path
        # first time through the longest path will be None, 
        if longest_path == None:
            # replace the None value with the current path
            longest_path = path
            # keep track of the current path length
            length_path = current_path_length
        # if the current path length is longer than the longest path length
        elif current_path_length > length_path:
            # save the new length of the longest path
            length_path = current_path_length
            #replace the longest path with the current path
            longest_path = path
    # if two paths have the same length compare the last value from those paths and return the lowest numeric number.
        elif current_path_length == length_path:
            # keep the path whose last value is the smallest number.
            if longest_path[-1] < current_node:
                longest_path = path
        # else mark this as visited
        visited.add(current_node)
        # get the neighbors
        edges = get_neighbors(vertices, current_node)
        # for each one, ad a Path To IT to the queue
        for edge in edges:
            new_path = list(path)
            new_path.append(edge)
            queue.enqueue(new_path)
    # the oldest ancestor is last value from the longest path
    ancestor = int(longest_path[-1])
    # if the starting node is the oldest ancestor then return -1
    if ancestor == starting_node:
        ancestor = -1
    return ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 8)