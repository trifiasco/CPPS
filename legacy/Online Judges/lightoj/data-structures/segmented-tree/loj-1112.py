import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class SegmentedTree():
    def __init__(self, sz, arr) -> None:
       self.tree = [0] * (4 * sz);
       self.values = [0] * (sz + 1);

       for i in range(sz):
           self.values[i + 1] = arr[i];

       # print(self.values)


    def build(self, index, left, right):
        if(left == right):
            # print(left, self.values[left])
            self.tree[index] = self.values[left];
            return;


        mid = (left + right) >> 1;
        leftChild = index << 1;
        rightChild = leftChild + 1;
        # print(index, left, right,  mid, leftChild, rightChild)

        self.build(leftChild, left, mid);
        self.build(rightChild, mid + 1, right);
        
        self.tree[index] = self.tree[leftChild] + self.tree[rightChild]


    def query(self, index, left, right, qleft, qright):
        if qleft > right or qright < left:
            return 0;
        elif (left >= qleft and right <= qright):
            return self.tree[index];

        mid = (left + right) >> 1;
        leftChild = index << 1;
        rightChild = leftChild + 1;

        return self.query(leftChild, left, mid, qleft,
                          qright) + self.query(rightChild, mid + 1, right, qleft,
                          qright)


    def update(self, index, left, right, pos, val):
        if left == right:
            if val == -1:
                current = self.tree[index];
                self.tree[index] = 0;
                return current
            self.tree[index] += val;
            return;

        mid = (left + right) >> 1;
        leftChild = index << 1;
        rightChild = leftChild + 1;

        res = 0;
        if pos <= mid:
            res = self.update(leftChild, left, mid, pos, val);
        else:
            res = self.update(rightChild, mid + 1, right, pos,
                        val);

        self.tree[index] = self.tree[leftChild] + self.tree[rightChild];
        # print(index, left, right, res)
        return res;



def solve(caseno):
    n, q = map(int, input().split());

    arr = list(map(int, input().split()));
    
    tree = SegmentedTree(n, arr);

    tree.build(1, 1, n);

    print('Case %d:' %(caseno))
    for i in range(q):
        qq = list(input().split());

        mType = int(qq[0]);

        if mType == 1:
            pos = int(qq[1]);

            print(tree.update(1, 1, n, pos + 1, -1));
        if mType == 2:
            pos = int(qq[1]);
            val = int(qq[2]);

            tree.update(1, 1, n, pos + 1, val);

        if mType == 3:
            ql = int(qq[1]);
            qr = int(qq[2]);

            print(tree.query(1, 1, n, ql + 1, qr + 1));



        

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

