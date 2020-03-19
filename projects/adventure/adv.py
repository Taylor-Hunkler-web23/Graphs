from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

#go to room
# if went north, thenn that room has exit to the south


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#rooms visited
visited = {}

#still rooms to visit
while len(visited)< len (room_graph):
    #initiate starting point
    if len(visited) == 0:
        #current room
        room = player.current_room.id
        #exit directions 
        exits = player.current_room.get_exits()

# add room id as id, exits as value
        visited[room] = exits
        
#if room is not in visited
    if player.current_room.id not in visited:
        #add room to visited
        visited[player.current_room.id] = player.current_room.get_exits()



##############################################

# def bfs(starting_room):
     
        
#         # Create a queue
#     queue = Queue()

#       # Enqueue a list to use as A PATH TO the starting vertex      
#     queue.enqueue([starting_room])
#         # Create a set to store visited vertices
#     visited = set()
#         # While the queue is not empty...
#     while queue.size() > 0:
#             # Dequeue the first PATH
#         path = queue.dequeue()
#             # GRAB THE VERTEX FROM THE END OF THE PATH. last item in path
#         room = path[-1]

#             # If vertex hasn't been visited...
#         if room not in visited:
#              # CHECK IF IT'S THE TARGET
#             if room == '?':
#              # IF SO, RETURN THE PATH
#                 return path
#         #add vertex to visited
#             visited.add(room)
#                 # Enqueue A PATH TO all it's neighbors
#             for neighbor in self.get_neighbors(v):
#                     # MAKE A COPY OF THE PATH        
#                 new_path = list(path)
#                     #add
#                 new_path.append(neighbor)  
#                     # ENQUEUE THE COPY
#                 queue.enqueue(new_path)



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
