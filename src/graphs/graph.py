from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Edge:
    weight: int
    to_vertex: int


class Graph:
    def __init__(self, vertex_count: int, edges: List[Tuple[int, int, int]]):
        self.vertex_count = vertex_count
        self.edges = [[-1 for i in range(vertex_count)] for j in range(vertex_count)]
        for weight, x, y in edges:
            self.edges[x][y] = weight
            self.edges[y][x] = weight

    def edges_from(self, vertex: int) -> List[Edge]:
        return [
            Edge(weight, i)
            for i, weight in enumerate(self.edges[vertex])
            if weight >= 0
        ]
