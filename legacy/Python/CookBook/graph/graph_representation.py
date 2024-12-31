
class Graph():
    
    def __init__(self, V, E = 0) -> None:
       self.V= V;
       self.E = E;
       self.adjlist = [[] for i in range(V + 1)];
       
       self.visited = [0] * (V + 1);

    def add_edge(self, u, v):
        self.E += 1
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

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
    return
