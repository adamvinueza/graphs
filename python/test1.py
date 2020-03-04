from graph import Vertex

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
src = s
dest = y
s_to_y_path = "swxy"
s_to_y_cost = 3
