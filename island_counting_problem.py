Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


# nodes: 1's
# edges: NSEW neighbors, not diagonals
# connected components: islands

# mark what has been visited.
# add the number of islands
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def getNeighbors(matrix, node):
    row = node[0]
    column = node[1]
    neighboring_islands = []
    if row > 0:
        stepNorth = row -1
    if col > 0:
        stepWest = column -1
    if row < len(matrix) - 1:
        stepSouth = row + 1
    if column < len(matrix) -1:
        stepEast = column + 1
    
    if stepNorth is not False and matrix[stepNorth][column] == 1:
        neighboring_islands.append((stepNorth, column))
    if stepSouth is not False and matrix[stepSouth][column] == 1:
        neighboring_islands.append((stepSouth, column))
    if stepWest is not False and matrix[row][stepWest] == 1:
        neighboring_islands.append((row, stepWest))
    if stepEast is not False and matrix[row][stepEast] == 1:
        neighboring_islands.append((row, stepEast))

def dft(matrix, node, visited=set()):
    stack = Stack()
    stack.push(node)
    while stack.size() > 0:
        current_node = stack.pop
        if node not in visited:
        visted.add(node)
        neighbors = getNeighbors(matrix, node)
        for neighbor in neighbors:
            stack.push(neighbor)

def island_counter(matrix):
    total_islands = 0
    visited = set()
    # iterate through the matrix
    for row in range(len(matrix)):
        for column in range(len(row)):
            node = (row, column)
            if node not in visited and matrix[row][column] == 1:
                visited.add(node)
                dft(matrix, node, visited)
                total_islands +=1
    return total_islands

    # if it's a 1, then run DFT/BFT

island_counter(islands) # returns 4