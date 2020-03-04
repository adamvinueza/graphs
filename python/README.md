# Python implementation of BFS

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
