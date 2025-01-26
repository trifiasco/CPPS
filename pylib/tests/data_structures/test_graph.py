from pylib.data_structures.graph import Graph


def test_graph():
    graph = Graph(5)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(5, 1)

    graph.dfs(1)
    assert graph.visited == [0, 1, 1, 1, 1, 1]

    graph.visited = [0] * 6
    graph.bfs(1)
    assert graph.visited == [0, 1, 1, 1, 1, 1]
    pass
