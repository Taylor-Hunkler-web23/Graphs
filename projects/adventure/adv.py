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



#start in current room
#add room to visited. key is room id, value is exits
#go in the direction of the last exit in visited
#keep repeating until no more exits unvisted in room
#if no more exits unvisited, go back in the direction you came from
#repeat steps until theres no more rooms left unvisited


#keep track of every move made
traversal_path = []

#rooms visited id-room value-exits
visited = {}

#keep track of the opposite direction of move we make
trailback = []

#opposite directions n=s
opposite_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

#while still rooms not visited
while len(visited)< len(room_graph):   

    #initiate starting room
    if len(visited) == 0:
        
    #add room to visited room.id as key, exits as values- {0: ['n']} 
        visited[player.current_room.id] = player.current_room.get_exits()     
      
        
    #if room is not in visited
    if player.current_room.id not in visited:
    #add room to visited {0: [], 1: ['n', 's']} \
        visited[player.current_room.id] = player.current_room.get_exits()
        # print(visited.keys(),"key")    
      
        
    #if we explored all exits of current room
    while len(visited[player.current_room.id]) <1: 
       
        # then we need to go back to the room we just came from
        go_back= trailback.pop() #n
        # print(go_back,"go back")

       #log the direction of the move we are about to make in traversal_path
        traversal_path.append(go_back)
        #go to the room in that direction
        player.travel(go_back)

    


    #go_to = the last exit in visited
    go_to = visited[player.current_room.id].pop()


    #log the direction we are going 
    traversal_path.append(go_to) #n s n

    #log the opposite direction we are going in
    trailback.append(opposite_direction[go_to])#n = s n s 

    #go to the room in that direction
    player.travel(go_to)#n s n


    # print(visited, 'visited end')
    # print(trailback, 'trailback end')
    # print(traversal_path,'traversal end')




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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
