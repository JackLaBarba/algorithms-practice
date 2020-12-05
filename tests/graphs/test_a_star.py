from src.graphs.a_star import AStar
from src.graphs.graph import Graph


def test_astar_a() -> None:
    graph = Graph(
        4,
        [
            (1, 0, 1),
            (1, 1, 2),
            (1, 0, 3),  # should use this edge only
            (3, 2, 3),
        ],
    )
    a_star = AStar(graph, 0, 3)
    a_star.run()
    assert a_star.path_distance() == 1
    assert a_star.path() == [0, 3]


def test_astar_b() -> None:
    graph = Graph(
        4,
        [
            (1, 0, 1),
            (2, 1, 2),
            (3, 2, 3),
        ],
    )
    a_star = AStar(graph, 0, 3)
    a_star.run()
    assert a_star.path_distance() == 6
    assert a_star.path() == [0, 1, 2, 3]
