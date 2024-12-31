
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Hashing():
    base = 1572872831;
    mod = 1000000007;

    def __init__(self, mx_sz) -> None:
        self.mx_sz = mx_sz

        self.powers = [0] * self.mx_sz;

        # self.powers[0] = 1;
        # for i in range(1, self.mx_sz):
            # self.powers[i] = (self.powers[i - 1] * self.base) % self.mod


    def hashPattern(self, pattern):
        res = -1;

        # print('hash pattern indi')
        for char in pattern:
            order = ord(char);

            if res == -1:
                res = order;
            else:
                res = ((res * self.base) % self.mod + order) % self.mod;

            # print(res)


        return res;

    def hashText(self, text, sz, pattern, psz):
        self.textHashTable = [0] * sz;
        self.powers[0] = 1;
        res = 0;
        patternHash = 0;

        # print('hash pattern combi');

        for i in range(sz):
            char = text[i];
            order = ord(char);

            if(i == 0):
                patternOrder = ord(pattern[i])
                patternHash = patternOrder;
            elif i < psz:
                patternOrder = ord(pattern[i])
                patternHash = ((patternHash * self.base) % self.mod + patternOrder) % self.mod

            # print(patternHash)

            if res == 0:
                self.textHashTable[0] = order;
            else:
                self.textHashTable[res]= ((self.textHashTable[res - 1]* self.base) % self.mod + order) % self.mod;
                self.powers[res] = (self.powers[res -1] * self.base) % self.mod

            res += 1;
        return patternHash;

    def MOD(self, x):
        return ((x % self.mod) + self.mod) % self.mod;

    def getHashValue(self, left, right):
        if left == 0:
            return self.textHashTable[right];

        return self.MOD(self.textHashTable[right] - ((self.textHashTable[left - 1] * self.powers[right - left + 1]) % self.mod));


def solve(caseno, hash):
    text = input();
    pattern = input();


    pattern_len = len(pattern);
    text_len = len(text);

    # targetHash1 = hash.hashPattern(pattern);
    targetHash = hash.hashText(text, text_len, pattern, pattern_len);

    # print(targetHash);
    # print(targetHash1);

    i = 0;
    j = pattern_len - 1;
    res = 0;

    while j < text_len:
        if hash.getHashValue(i, j) == targetHash:
            res += 1;

        i += 1;
        j += 1;

    print('Case %d: %d' %(caseno, res));

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    # sys.setrecursionlimit(200000)

    hash = Hashing(1000001);
    T = int(input());

    for i in range(1, T + 1):
        solve(i, hash);
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
