from graph import Graph

# dfs = deepest ansector
def earliest_ancestor(ancestors, starting_node):
    
# build graph
    graph = Graph()

#for each pair in ancestors
    for pair in ancestors:
        #add verticies
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build edges, link from children to parents
        graph.add_edge(pair[1], pair[0])

        #create path with dfs 
        for (pair[0], pair[1]) in ancestors:
            path= graph.dfs(pair[1], pair[0])

    