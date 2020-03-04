#!/usr/local/bin/python3
import sys

class Vertex:
    '''
    Vertex represents a graph vertex.
    '''
    def __init__(self, name):
        self.name = name 
        self.visited = False
        self.parent = None
        self.cost = sys.maxsize

class Graph:
    '''
    Graph represents an undirected graph with edges of unit cost--meaning the cost
    of traveling from any vertex to an adjacent vertex is constant.
    '''
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def adjacents(self, v):
        return self.edges[v]

    # "undirected" means bidirectional, so we add both vertices as keys
    def add_edge(self, e):
        first = e[0]
        second = e[1]
        if first not in self.edges:
            self.edges[first] = []
        self.edges[first].append(second)
        if second not in self.edges:
            self.edges[second] = []
        self.edges[second].append(first)
        self.add_vertices([first, second])

    def add_vertices(self, e):
        for v in e:
            if not v in self.vertices:
                self.vertices.append(v)

    def reset(self):
        for i in range(len(self.vertices)):
            v = self.vertices[i]
            v.visited = False
            v.parent = None
            v.cost = sys.maxsize


def bfs(g, s):
    s.visited = True
    s.cost = 0
    s.parent = None
    queue = []
    queue.append(s)
    while len(queue) > 0:
        u = queue.pop(0)
        for x in g.adjacents(u):
            if not x.visited:
                x.visited = True
                x.cost = u.cost + 1
                x.parent = u
                queue.append(x)

def path(dest):
    curr = dest 
    vals = []
    while curr.parent is not None:
        vals.append(curr.name)
        curr = curr.parent
    vals.append(curr.name)
    return ' => '.join(vals)

def cost(src, dest):
    curr_cost = dest.cost
    curr = dest
    while curr.parent != src:
        if curr.parent is None:
            return sys.maxsize
        curr = curr.parent
    return curr_cost - src.cost

def run():
    g = Graph()
    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    edges = [
        [r, s],
        [r, v],
        [s, w],
        [t, w],
        [t, u],
        [u, x],
        [u, y],
        [w, x],
        [x, y]
    ]
    for e in edges:
        g.add_edge(e)

    bfs(g, s)
    print('Shortest path from {0} to {1}: {2}'.format(s.name, y.name, path(y)))
    print('Shortest path cost from {0} to {1}: {2}'.format(s.name, y.name, cost(s, y)))

if __name__ == '__main__':
    run()
