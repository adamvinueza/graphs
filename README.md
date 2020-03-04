# graphs
Implementations of graph data structures, for teaching purposes.

## Python

The Python implementation contains a simple version of breadth-first search. An
instance of the `Graph` class has the following methods:
- `Graph.shortest_path(src, dest)` returns the path from the `src` vertex to the
  `dest` vertex, as a string. (Vertices are named, and the convention is to name
  a vertex with a single letter of the alphabet.)
- `Graph.min_cost(src, dest)` returns the minimum cost of traveling from the
  `src` vertex to the `dest` vertex, as an integer.
