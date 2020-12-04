from src.djikstras import Graph, ShortestPath


def test_sp_a() -> None:
    graph = Graph(
        4,
        [
            (1, 0, 1),
            (1, 1, 2),
            (1, 0, 3),  # should use this edge only
            (3, 2, 3),
        ],
    )
    sp = ShortestPath(graph)
    sp.run(0)
    assert sp.shortest_path_weight(3) == 1
    assert sp.shortest_path(3) == [0, 3]


def test_sp_b() -> None:
    graph = Graph(
        4,
        [
            (1, 0, 1),
            (2, 1, 2),
            (3, 2, 3),
        ],
    )
    sp = ShortestPath(graph)
    sp.run(0)
    assert sp.shortest_path_weight(3) == 6
    assert sp.shortest_path(3) == [0, 1, 2, 3]
