
import sys
import os
from heapq import heappush, heappop 

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Graph():

    INF = sys.maxsize
    def __init__(self, V, E) -> None:
       self.V = V;
       self.E = E;

       self.adjlist = [[] for i in range(V)];
       self.distance = [self.INF] * V;
       self.weights = [0 for i in range(V)]


    def add_edge(self, u, v, w):
        self.adjlist[u].append((v, w))
        self.adjlist[v].append((u, w))

    def calc_shortest_distance(self, source):

        priority_queue = [];

        heappush(priority_queue, (0, source));
        self.distance[source] = 0;
        self.weights[source] = 0;

        while len(priority_queue) != 0:
            current = heappop(priority_queue);
            u = current[1];
            d = current[0];

            if d > self.distance[u]:
                continue;

            for node in self.adjlist[u]:
                v = node[0];
                w = node[1];

                if self.distance[v] > max(self.distance[u], w):
                   self.distance[v] = max(self.distance[u], w);
                   heappush(priority_queue, (self.distance[v], v));

        return;

    def print_solution(self):
        for i in range(self.V):
            if i != 0:
                print("");
            if self.distance[i] != self.INF:
                print('%d' %(self.distance[i]), end="")
            else:
                print("Impossible", end="")

        print("")

def solve(caseno):
    input();

    n, m = map(int, input().split());

    graph = Graph(n, m);

    for i in range(m):
        u, v, w = map(int, input().split());
        graph.add_edge(u, v, w);


    source_city = int(input())
    graph.calc_shortest_distance(source_city);

    print('Case %d:' %(caseno));
    
    graph.print_solution()


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
