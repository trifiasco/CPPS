
import sys
import os
from heapq import heappush, heappop

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

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

def solve(caseno):
    input();

    n = int(input());
    graph = Graph(n + 1);

    while True:
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w);
        if u == 0 and v == 0 and w == 0:
            break;

    min_mst_cost = graph.min_mst(0, True);
    graph.clear_graph()
    max_mst_cost = graph.min_mst(0, False);


    total = min_mst_cost + max_mst_cost;

    if(total % 2 == 0):
        print('Case %d: %d' %(caseno, total//2));
    else:
        print('Case %d: %d/%d' %(caseno, total, 2))

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
