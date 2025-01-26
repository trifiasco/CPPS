from dataclasses import dataclass


@dataclass
class Graph:
    def __init__(self, V: int, E: int = 0) -> None:
        self.V: int = V
        self.E: int = E
        self.adjlist: list[list[int]] = [[] for _ in range(V + 1)]
        self.visited: list[int] = [0] * (V + 1)

    def add_edge(self, u: int, v: int) -> None:
        self.E += 1
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

    def is_node_processed(self, node: int) -> bool:
        return self.visited[node] != 0

    def dfs(self, node: int) -> None:
        print(node)
        self.visited[node] = 1

        for neighbor in self.adjlist[node]:
            if not self.is_node_processed(neighbor):
                self.dfs(neighbor)
        return

    def bfs(self, node: int) -> None:
        from collections import deque

        q: deque[int] = deque()
        q.append(node)
        self.visited[node] = 1

        while q:
            current_node = q.popleft()
            print(current_node)

            for neighbor in self.adjlist[current_node]:
                if not self.is_node_processed(neighbor):
                    q.append(neighbor)
                    self.visited[neighbor] = 1
        return
