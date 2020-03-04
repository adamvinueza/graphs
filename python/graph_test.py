from graph import Graph, Vertex
import sys
import test1

def test_graph_ctr():
    g = Graph([])
    assert 0 == len(g.vertices)
    assert 0 == len(g.edges)
    h = Graph(test1.edges)
    assert 8 == len(h.vertices)

def test_vertex_ctr():
    expected_name = 'dog'
    expected_parent = None
    expected_cost = sys.maxsize
    v = Vertex(expected_name)
    assert expected_name == v.name
    assert expected_parent == v.parent
    assert expected_cost == v.cost

def test_bfs_shortest_path():
    g = Graph(test1.edges)
    assert test1.s_to_y_path == g.shortest_path(test1.src, test1.y)
    assert test1.s_to_y_cost == g.min_cost(test1.src, test1.y)

def test_reset():
    g = Graph(test1.edges)
    g.bfs(test1.src)
    assert test1.y.parent is not None
    g.reset()
    assert test1.y.parent is None

