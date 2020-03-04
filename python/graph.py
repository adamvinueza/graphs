import sys

MAX_VERTEX_COST = sys.maxsize

class Vertex:
    '''
    Vertex represents a graph vertex.
    '''
    def __init__(self, name):
        self.name = name 
        self.visited = False
        self.parent = None
        self.cost = MAX_VERTEX_COST

class Graph:
    '''
    Graph represents an undirected graph with edges of unit cost--meaning the
    cost of traveling from any vertex to an adjacent vertex is constant.
    '''
    def __init__(self, edges):
        self.vertices = []
        self.edges = {}
        for e in edges:
            self.add_edge(e)

    def adjacents(self, v):
        return self.edges[v]

    def add_edge(self, e):
        '''
        Adds the specified edge to this Graph, if not already in this Graph.
        Because the edge is undirected, two edges are added.
        '''
        first = e[0]
        second = e[1]
        if first not in self.edges:
            self.edges[first] = []
        if second not in self.edges[first]:
            self.edges[first].append(second)
        if second not in self.edges:
            self.edges[second] = []
        if first not in self.edges[second]:
            self.edges[second].append(first)
        self._add_vertices([first, second])

    def _add_vertices(self, e):
        '''
        Adds the specified vertex to this Graph, if not already in this Graph.
        '''
        for v in e:
            if not v in self.vertices:
                self.vertices.append(v)

    def shortest_path(self, src, dest):
        '''
        Returns the shortest path from src to dest.
        '''
        self.bfs(src)
        curr = dest 
        vals = []
        while curr.parent is not None:
            vals.append(curr.name)
            curr = curr.parent
        vals.append(curr.name)
        vals.reverse()
        return ''.join(vals)

    def min_cost(self, src, dest):
        self.bfs(src)
        if src not in self.vertices or dest not in self.vertices:
            return MAX_VERTEX_COST
        curr_cost = dest.cost
        curr = dest
        while curr.parent != src:
            if curr.parent is None:
                return MAX_VERTEX_COST
            curr = curr.parent
        return curr_cost - src.cost

    def reset(self):
        for i in range(len(self.vertices)):
            v = self.vertices[i]
            v.visited = False
            v.parent = None
            v.cost = sys.maxsize

    def bfs(self, s):
        self.reset()
        s.visited = True
        s.cost = 0
        s.parent = None
        queue = []
        queue.append(s)
        while len(queue) > 0:
            u = queue.pop(0)
            for x in self.adjacents(u):
                if not x.visited:
                    x.visited = True
                    x.cost = u.cost + 1
                    x.parent = u
                    queue.append(x)
