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
        processed: List[bool] = [False for i in range(self.graph.vertex_count)]
        dist: List[int] = [math.inf for i in range(self.graph.vertex_count)]
        parent: List[int] = [None for i in range(self.graph.vertex_count)]

        next_to_process = start
        dist[start] = 0

        while next_to_process is not None:
            for edge in self.graph.edges_from(next_to_process):
                dist_thru = edge.weight + dist[next_to_process]
                print(next_to_process, edge, dist_thru)
                if dist_thru < dist[edge.to_vertex]:
                    dist[edge.to_vertex] = dist_thru
                    parent[edge.to_vertex] = next_to_process

            processed[next_to_process] = True

            least_distance = math.inf
            next_to_process = None
            for vertex, distance in enumerate(dist):
                if not processed[vertex] and distance < least_distance:
                    next_to_process = vertex
                    least_distance = distance

        print(dist)
        print(parent)
        self.dist = dist
        self.parent = parent


    def shortest_path_weight(self, end: int) -> int:
        return self.dist[end]

    def shortest_path(self, end: int) -> List[int]:
        cur = end
        path = [end]
        while self.parent[cur] is not None:
            path = [self.parent[cur]] + path
            cur = self.parent[cur]
        
        return path
