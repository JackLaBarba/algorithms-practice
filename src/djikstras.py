from typing import List, Tuple
import math
from dataclasses import dataclass

@dataclass
class Edge():
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
            Edge(weight, i) for i, weight 
            in enumerate(self.edges[vertex]) 
            if weight >= 0
        ]
        

class ShortestPath():
    def __init__(self, graph: Graph):
        self.graph = graph

    def run(self, start: int):
        processed: List[int] = [False for i in range(self.graph.vertex_count)]
        dists: List[int] = [math.inf for i in range(self.graph.vertex_count)]
        parents: List[int] = [None for i in range(self.graph.vertex_count)]

        dists[start] = 0
        next_vertex = start

        while next_vertex is not None:
            for edge in self.graph.edges_from(next_vertex):
                dist_thru = dists[next_vertex] + edge.weight
                if dists[edge.to_vertex] > dist_thru:
                    dists[edge.to_vertex] = dist_thru
                    parents[edge.to_vertex] = next_vertex

            processed[next_vertex] = True
            next_vertex = None
            least_dist = math.inf
            
            for vertex, dist in enumerate(dists):
                if not processed[vertex] and dist < least_dist:
                    next_vertex = vertex
                    least_dist = dist

        self.dists = dists
        self.parents = parents

    def shortest_path_weight(self, end: int):
        return self.dists[end]

    def shortest_path(self, end: int):
        cur = end
        path = [cur]
        while self.parents[cur] is not None:
            path = [self.parents[cur]] + path
            cur = self.parents[cur]
        return path

