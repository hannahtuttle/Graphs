from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Graph:
    def __init__(self):
        self.path = {}
    def dft(self, starting_room, ):

        stack = Stack()

        visited = {}

        travel_path = []

        stack.push(starting_room)

        while stack.size() > 0:
            current_room = stack.pop()
            player.current_room = current_room

            # print('current_room', current_room)

            if current_room.id not in visited:

                exit_dict = {}

                exits = current_room.get_exits()


                for ex in exits:
                    exit_dict[ex] = '?'

                visited[current_room.id] = exit_dict

                # print('visited', visited)
                for e in exits:
                    player.travel(f'{e}')
                    next_room = player.current_room
                    visited[current_room.id][f'{e}'] = next_room.id
                    if e == 'n':
                        player.travel('s')
                    if e == 's':
                        player.travel('n')
                    if e == 'e':
                        player.travel('w')
                    if e == 'w':
                        player.travel('e')
                    stack.push(next_room)
                    # print('next_room',next_room.id)
        return visited
        def bfs(self, visited_graph):
            pass


graph = Graph()

visit = graph.dft(world.starting_room)
print(visit)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
