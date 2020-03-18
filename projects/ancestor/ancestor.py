from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    
# build graph
    graph = Graph()

#for each pair in ancestors
    for pair in ancestors: 
        #parent
        parent = pair[0]
        #child
        child=pair[1]

    #add parent vertex
        graph.add_vertex(parent)        
    #add child vertex        
        graph.add_vertex(child)

        # build edges, directed, link from children to parents
        graph.add_edge(child, parent)
  #[(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    #         '''
    #    10
    #  /
    # 1   2   4  11
    #  \ /   / \ /
    #   3   5   8
    #    \ / \   \
    #     6   7   9
    # '''
   #BFS [6] copy[6,3] now queue [6,3] now longer path for [6] -[6,3,1] -[6,3,1,10]
    queue = Queue()
        #enqueue a path with starting node
    queue.enqueue([starting_node])
       #longest path
    longest_path_length = 1
    # If the input individual has no parents, the function should return -1.
    earliest_ancestor= -1 #6 #3
    
    while queue.size() >0:
        path=queue.dequeue()#6  -[6,3] -[6,3,1] -[6,3,1,10]
             #last things in path
        ver=path[-1]#6 -3- -1- -10-

# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. #looking for path longer than current
        if (len(path) >= longest_path_length and ver < earliest_ancestor) or (len(path)>longest_path_length):
            #earliest ancestor now vertex
            earliest_ancestor=ver#6 #3 -1- -10-
             #update with length of path
            longest_path_length = len(path)

          
        for neighbor in graph.vertices[ver]:
            #make copy
            path_copy = list(path)
            # add neighbor
            path_copy.append(neighbor)#3 -1- -10-
            #enque new path
            queue.enqueue(path_copy)#[6,3] [6,3,1] [6,3,1,10]

#furthest path
        print(longest_path_length, 'Lpath')
        print(path, 'path')
        print(earliest_ancestor, 'Earliest a')

    return earliest_ancestor #10




    