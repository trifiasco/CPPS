
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Graph():
    
    def __init__(self, V, E, edges) -> None:
       self.num_of_vertex = V;
       self.num_of_edges = E;
       self.edges = edges;
       self.adjlist = [[] for i in range(V + 1)];

       for edge in edges:
         self.adjlist[edge[0]].append(edge[1]);
         self.adjlist[edge[1]].append(edge[0]);

       
       self.visited = [0] * (V + 1);


    def dfs(self, node, color):
        self.visited[node] = 1;

        vampire = 0;
        lykan = 0;
        if color == 0:
            vampire += 1;
        if color == 1:
            lykan += 1;

        for v in self.adjlist[node]:
            if self.visited[v] == 0:
                res = self.dfs(v, 1 - color)
                vampire += res[0];
                lykan += res[1];

        return (vampire, lykan)

    def is_node_processed(self, node):
        return self.visited[node] != 0;



def solve(caseno):
    m = int(input());

    edges = []

    mp = dict();
    currentNode = 1;
    for i in range(m):
        u, v = map(int, input().split())

        if mp.get(u, 0) == 0:
            mp[u] = currentNode
            currentNode += 1;
        
        if mp.get(v, 0) == 0:
            mp[v] = currentNode
            currentNode += 1;
        edges.append((mp[u], mp[v]))


    graph = Graph(currentNode, len(edges), edges);

    res = 0;
    for i in range(1, currentNode):
        if graph.is_node_processed(i) == False:
            cluster = graph.dfs(i, 0);

            res += max(cluster[0], cluster[1])

    print("Case %d: %d" %(caseno, res))
    
    return

def READ():
    sys.stdin = open('in.txt', 'r');
    # sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    sys.setrecursionlimit(200000)
    T = int(input());
    for i in range(1, T + 1):
        solve(i)
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
