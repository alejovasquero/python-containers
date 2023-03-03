import plotly.graph_objects as go
from igraph import Graph, EdgeSeq

from src.priority_queue.priority_heap import Heap


def draw_heap(heap: Heap):
    E: set = create_edges_graph(heap)
    V: list = [str(i) for i in heap.list_data]

    vertices_number = len(heap)
    v_label = list(map(str, heap.list_data))
    tree: Graph = Graph(directed=True)
    tree.add_vertices(V)
    tree.add_edges(E)

    lay = tree.layout('tree')

    position = {k: lay[k] for k in range(vertices_number)}
    Y = [lay[k][1] for k in range(vertices_number)]
    M = max(Y)

    es = EdgeSeq(tree)  # sequence of edges
    E = [e.tuple for e in tree.es]  # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2 * M - position[k][1] for k in range(L)]
    Xe = []
    Ye = []
    for edge in E:
        Xe += [position[edge[0]][0], position[edge[1]][0], None]
        Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

    labels = v_label
    draw(labels, Xe, Ye, Xn, Yn)


def draw(labels, Xe, Ye, Xv, Yv):
    fig = go.Figure()
    fig.update_layout()
    fig.add_trace(go.Scatter(x=Xe,
                             y=Ye,
                             mode='lines',
                             name="Relations",
                             line=dict(color='rgb(210,210,210)', width=1),
                             hoverinfo='none'
                             ))
    fig.add_trace(go.Scatter(x=Xv,
                             y=Yv,
                             mode='markers',
                             name='Priority',
                             marker=dict(symbol='circle-dot',
                                         size=18,
                                         color='#6175c1',  # '#DB4551',
                                         line=dict(color='rgb(50,50,50)', width=1)
                                         ),
                             text=labels,
                             hoverinfo='text',
                             opacity=0.8
                             ))
    fig.add_scatter()

    axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                )

    fig.update_layout(xaxis=axis, yaxis=axis)
    fig.show()


def create_edges_graph(heap: Heap) -> set:
    E = set()
    for i in range(1, heap.current_size + 1):

        if i * 2 <= heap.current_size:
            E.add((str(heap.list_data[i - 1]), str(heap.list_data[i * 2 - 1])))
        if i * 2 + 1 <= heap.current_size:
            E.add((str(heap.list_data[i - 1]), str(heap.list_data[i * 2])))

    return E
