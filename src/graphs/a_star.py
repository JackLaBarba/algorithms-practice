import math
from typing import List, Optional, Set

from src.graphs.graph import Graph


class AStar:
    def __init__(self, graph: Graph, start: int, end: int):
        self.graph: Graph = graph
        self.start: int = start
        self.end: int = end

    def heuristic(self, vertex: int) -> float:
        return abs(self.end - vertex)  # if zero, A* turns into Djikstra's

    def run(self) -> None:
        processed: Set[int] = set()
        dist: List[float] = [math.inf for i in range(self.graph.vertex_count)]
        parents: List[Optional[int]] = [None for i in range(self.graph.vertex_count)]

        dist[self.start] = 0
        vertex: Optional[int] = self.start
        while vertex is not None:
            for edge in self.graph.edges_from(vertex):
                new_dist = dist[vertex] + edge.weight
                if dist[edge.to_vertex] > new_dist:
                    dist[edge.to_vertex] = new_dist
                    parents[edge.to_vertex] = vertex

            processed.add(vertex)
            vertex = None
            least_score: float = math.inf

            for v in range(self.graph.vertex_count):
                if (
                    v not in processed
                    and (this_score := dist[v] + self.heuristic(v)) < least_score
                ):
                    vertex = v
                    least_score = this_score

        self.dist = dist
        self.parents = parents

    def path(self) -> List[int]:
        ret = [self.end]
        v = self.end
        while (parent := self.parents[v]) is not None:
            ret.append(parent)
            v = parent
        return list(reversed(ret))

    def path_distance(self) -> float:
        return self.dist[self.end]
