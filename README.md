# graphs
Implementations of graph data structures, for teaching purposes.

## The breadth-first search algorithm and shortest paths

One of the standard uses of graphs is to discover the shortest path from one
place to another, where all distances between adjacent vertices is the same.
Traversing grids is one of the typical examples.

When distances between adjacent vertices is always the same, you can use an
algorithm known as _breadth-first search_ to find the shortest paths from a
source vertex to any other vertex in graph. (When distances are _not_ always the
same, you will need to use a different algorith.)

The algorithm works by giving vertices three properties: _visited_, _parent_ and
_distance_ (sometimes also referred to as a _cost_). The visited property is set
to keep track of which vertices have already been touched by the algorithm. The
parent property is set during the algorithm so that one can retrieve the
shortest path from source to destination by running the algorithm and following
the destination's parents to the source. The distance property is set so that
retrieving the minimum distance from source to destination is a simple matter of
subtraction.

Here is the algorithm, in pseudocode:
```
BFS(g, s):
    for v in g.vertices:
        v.visited = FALSE
        v.parent = NIL
        v.distance = MAX_DISTANCE
    s.visited := TRUE
    s.parent := NIL
    s.distance := 0
    Q := QUEUE
    Q.enqueue(s)
    while Q.size != 0:
        u := Q.dequeue()
        for v in g.adjacents(u):
            v.visited = TRUE
            v.distance = u.distance + 1
            v.parent = u
            Q.enqueue(v)
```

Running BFS on a graph creates a shortest-path tree whose root is the source
vertex. You can then find the shortest path from source to a given vertex by
following that vertex's parents back to the source.

### Why is the algorithm "breadth-first"?

Search through a graph can proceed by following a single path as far as possible
until a visited vertex is found: that is what's known as "depth-first" search.
But it's also possible to search by putting all the vertices adjacent to the
source vertex into a queue, then pull them off one by one, marking them as
visited and putting their adjacent vertices into the queue. This way of
searching prioritizes visiting a vertex's adjacent vertices before going any
deeper into the graph: the "breadth" of the graph is first in searching.

### How do we know BFS computes shortest paths?

So far all we've seen is that BFS computes paths from a source vertex to all the
other vertices in the graph. How do we know that those paths are the _shortest_
ones from the source to the other vertices? The full proof of this is rather
involved, but the basic idea can be seen by considering the interaction between
a vertex's visited and distance properties. A vertex starts out as unvisited and
with a 0 distance. Once it is visited, its distance is updated to 1 plus the
distance of the visiting vertex; but _this happens precisely once_. So it should
be intuitive that if we start from the source vertex (distance = 0), then all
and only its adjacent vertices will have a distance of 1, and all and only
_their unvisited adjacent vertices_ will have a distance of 2, and so on. That
is, if there were a shorter path from the source to a vertex, _it would have
already been visited_; but given how we're traversing the graph, this is
impossible. So once BFS computes a path from a source to a vertex, that path is
_provably_ shortest.

## Python Implementation

The Python implementation contains a simple version of breadth-first search. An
instance of the `Graph` class has the following methods:
- `Graph.shortest_path(src, dest)` returns the path from the `src` vertex to the
  `dest` vertex, as a string. (Vertices are named, and the convention is to name
  a vertex with a single letter of the alphabet.)
- `Graph.min_cost(src, dest)` returns the minimum cost of traveling from the
  `src` vertex to the `dest` vertex, as an integer.

To see it in action, you can run the tests in `graph_test.py`. You'll need the
`pytest` package for that:

```
pip3 install pytest
```
Once you've installed `pytest`, run:
```
pytest
```
It should give you standard test output.

If you're using Visual Studio Code you can step into the code to see how it
behaves.
