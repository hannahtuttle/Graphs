"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make queue
        queue = Queue()
        #  make set for the visited nodes
        visited = set()
        # put our starting node in the queue
        queue.enqueue(starting_vertex)
        # if the queue is not empty, we have more nodes to visit
        while queue.size() > 0:
            # get the next node out of line
            current_node = queue.dequeue()
            # check to see if it has been visited
            if current_node not in visited:
            # if not, mark as visited
                visited.add(current_node)
                print(current_node)
            # and get all of it's neighbors
                edges = self.get_neighbors(current_node)
            # add neighbors to the queue
                for edge in edges:
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         # make stack
        stack = Stack()
        #  make set for the visited nodes
        visited = set()
        # put our starting node in the stack
        stack.push(starting_vertex)
        # if the stack is not empty, we have more nodes to visit
        while stack.size() > 0:
            # get the next node out of line
            currrent_node = stack.pop()
            # check to see if it has been visited
            if currrent_node not in visited:
            # if not, mark as visited
                visited.add(currrent_node)
                print(currrent_node)
            # and get all of it's neighbors
                edges = self.get_neighbors(currrent_node)
            # add neighbors to the stack
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # first time done
        # # make stack
        # stack = Stack()
        # #  make set for the visited nodes
        # visited = set()
        # # put our starting node in the stack
        # stack.push(starting_vertex)

        # def innner_recursion():
        #     if stack.size() == 0:
        #         # print('stopping')
        #         return
        #     current = stack.pop()
        #     if current not in visited:
        #         visited.add(current)
        #         print(current)
        #         edges = self.get_neighbors(current)
        #         for edge in edges:
        #             stack.push(edge)
        #     return innner_recursion()
        # return innner_recursion()

        # Tim's solution
        visited.add(starting_vertex)
        edges = self.get_neighbors(starting_vertex)
        if len(edges) == 0:
            return
        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # make a queue
        queue = Queue()
        # make a set for visited
        visited = set()
        # enqueues a Path To the starting_vertex
        queue.enqueue([starting_vertex])
        # while queue isn't empty:
        while queue.size() > 0:
            # dequeue the next path
            path = queue.dequeue()
            # current_node is the last thing in the path
            current_node = path[-1]
            # check if its the target, aka the destination_vertex
            if current_node is destination_vertex:
            # if so, return path
                return path
            # else mark this as visited
            visited.add(current_node)
            # get the neighbors
            edges = self.get_neighbors(current_node)
            # for each one, ad a Path To IT to the queue
            for edge in edges:
                new_path = list(path)
                new_path.append(edge)
                queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make stack
        stack = Stack()
        #  make set for the visited nodes
        visited = set()
        # put our a Path To the starting_vertex in the stack
        stack.push([starting_vertex])
        # if the stack is not empty keep going
        while stack.size() > 0:
            # get the next node out of line
            path = stack.pop()
            # current_node is the last thing in the path
            current_node = path[-1]
            # check if its the target, aka the destination_vertex
            if current_node is destination_vertex:
            # if so, return path
                return path
            # if not, mark as visited
            visited.add(current_node)
            # and get all of it's neighbors
            edges = self.get_neighbors(current_node)
            # add neighbors to the stack
            for edge in edges:
                new_path = list(path)
                new_path.append(edge)
                stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """ 
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
           # make stack
        stack = Stack()
        #  make set for the visited nodes
        visited = set()
        # put our starting node in the stack
        stack.push([starting_vertex])

        def innner_recursion():
            if stack.size() == 0:
                # print('stopping')
                return
            path = stack.pop()
            current = path[-1]
            if current is destination_vertex:
                return path
            visited.add(current)
            edges = self.get_neighbors(current)
            for edge in edges:
                new_path = list(path)
                new_path.append(edge)
                stack.push(new_path)
            return innner_recursion()
        return innner_recursion()

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
