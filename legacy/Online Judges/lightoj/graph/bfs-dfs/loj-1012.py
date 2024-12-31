
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Graph():
    dir_x = [-1, 0, 1, 0];
    dir_y = [0, -1, 0, 1];

    def __init__(self, adj_mat, starting_point, n, m) -> None:
       self.adj_mat = adj_mat;
       self.start_x = starting_point[0];
       self.start_y = starting_point[1];

       self.n = n;
       self.m = m;

       self.visited = [[0 for j in range(m)] for i in range(n)]


    def isInsideGrid(self, x, y):
        return (x >= 0 and x < self.n and y >= 0 and y < self.m)

    def flood_fill(self, x, y):
        self.visited[x][y] = 1;

        res = 1;
        for i in range(4):
            tx = x + self.dir_x[i];
            ty = y + self.dir_y[i];

            if self.isInsideGrid(tx, ty):
                    if self.visited[tx][ty] == 0 and self.adj_mat[tx][ty] != 0:
                        res += self.flood_fill(tx, ty);

        return res;

def solve(caseno):
    m, n = map(int, input().split());

    fields = [[0 for i in range(m)] for j in range(n)];
    starting_point_x = 0;
    starting_point_y = 0;

    for i in range(n):
        line = input()
        j = 0;
        for char in line:
            if char != '#':
                fields[i][j] = 1;
                if char == '@':
                    starting_point_x = i;
                    starting_point_y = j;
            j += 1;


    # for i in range(n):
        # for j in range(m):
            # print(fields[i][j], end=" ");
        # print("")

    graph = Graph(fields, (starting_point_x, starting_point_y), n, m);

    res = graph.flood_fill(starting_point_x, starting_point_y)
    print("Case %d: %d" %(caseno, res));


def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

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
