from heapq import heappush, heappop
class Graph():

    def __init__(self, V) -> None:
       self.V = V;

       self.adjlist = [[] for i in range(V)];
       self.taken = [0 for i in range(self.V)];
       self.pq = [];

    def add_edge(self, u, v, w):
        self.adjlist[u].append((v, w));
        self.adjlist[v].append((u, w));

    def clear_graph(self):
       self.taken = [0 for i in range(self.V)];
       self.pq = [];


    def process(self, node, isMinPq):
        self.taken[node] = 1;
        
        for item in self.adjlist[node]:
            u = item[0];
            w = item[1];

            if(self.taken[u] == 0):
                if isMinPq:
                    heappush(self.pq, (w, u));
                else:
                    heappush(self.pq, (-w, u));

    def min_mst(self, root, isMinPq):
        mst_cost = 0;
        self.process(root,isMinPq);

        while len(self.pq) != 0:
            front = heappop(self.pq);

            u = front[1];
            w = front[0] if isMinPq else -front[0];

            if(self.taken[u] == 0):
                mst_cost += w;
                self.process(u, isMinPq)
                
        return mst_cost
