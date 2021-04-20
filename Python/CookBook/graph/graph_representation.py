
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
