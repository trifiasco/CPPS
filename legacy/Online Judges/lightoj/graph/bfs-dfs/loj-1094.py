
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Graph():

    INF = 300000007
    def __init__(self, n, edges, root) -> None:
       self.V = n;
       

       self.adjlist = [[] for i in range(n + 1)];

       for edge in edges:
           self.adjlist[edge[0]].append((edge[1], edge[2]));
           self.adjlist[edge[1]].append((edge[0], edge[2]));

       self.distance = [0 if i == root else self.INF for i in range(n)]
       self.visited = [0 for i in range(n)]

    def clear_graph(self, node):
       self.distance = [0 if i == node else self.INF for i in range(self.V)]
       self.visited = [0 for i in range(self.V)]

    def dfs(self, node):
        self.visited[node] = 1;

        for item in self.adjlist[node]:
            v = item[0];
            w = item[1];

            if self.visited[v] == 0 and self.distance[v] > self.distance[node] + w:

                self.distance[v] = self.distance[node] + w;
                self.dfs(v);

        return;

    def get_node_with_max_distance(self):
        return self.distance.index(max(self.distance));

    def get_max_distance(self):
        return max(self.distance);

def solve(caseno):
    n = int(input());

    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split());
        edges.append((u, v, w));


    graph = Graph(n, edges, 0);
    # first dfs to get the one of the furthest node
    graph.dfs(0);
    first_furthest_node = graph.get_node_with_max_distance();

    # second dfs to get the other furthest node
    graph.clear_graph(first_furthest_node);
    graph.dfs(first_furthest_node);
    res = graph.get_max_distance();
   

    print('Case %d: %d' %(caseno, res))

        

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    sys.setrecursionlimit(200000)
    T = int(input());
    for i in range(1, T + 1):
        solve(i);
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
