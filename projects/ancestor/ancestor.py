from util import Stack


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
        else:
            raise IndexError("vertex does not exist in graph")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        ptv = Stack()
        ptv.push([starting_vertex])

        visited = set()

        while ptv.size() > 0:
            path = ptv.pop()
            cv = path[-1]
            if cv not in visited:
                if cv == destination_vertex:
                    return path
                visited.add(cv)
                for neighbor in self.get_neighbors(cv):
                    new_path = list(path)
                    new_path.append(neighbor)
                    ptv.push(new_path)




def earliest_ancestor(ancestors, starting_node):
    # create graph
    ancestor_graph = Graph()
    # create path
    paths = []

    # add verticies to graph
    for vert in range(0, 12):
        ancestor_graph.add_vertex(vert)

     #create edges acording to ancestors list
    for ancestor in ancestors:
        ancestor_graph.add_edge(ancestor[0], ancestor[1])

    # add path to ancestor paths
    for vert in ancestor_graph.vertices:
        if ancestor_graph.dfs(vert, starting_node) is not None and len(ancestor_graph.dfs(vert, starting_node)) > 0:
            paths.append(ancestor_graph.dfs(vert, starting_node))
    # check if the length of paths is 1 then node has no ancestor return -1
    if len(paths) == 1:
        return -1

    # find longest path or largest vertx  value and set that to start path
    print(paths)
    start_path = paths[0]
    for path in paths:
        if len(path) > len(start_path) or len(start_path) and path[0] < start_path[0]:
            start_path = path
    #return only the oldest verticy
    print(start_path[0])
    return start_path[0]