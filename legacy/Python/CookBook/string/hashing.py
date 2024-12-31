
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Hashing():

    mods = [1000000007, 2117566807];
    bases = [1572872831, 1971536491]
    def __init__(self, size) -> None:
        self.size = size;
        self.power = [] * size

        self.power[0] = 1

        for i in range(1, size):
            self.power[i] = (self.power[i - 1] * self.bases[0]) % self.mods[0]

    def makeForwardHashTable(self, string):
        sz = len(string)
        self.forwardHashTable = [] * sz;
        for i in range(sz):
            current = string[i] - ' ';

            if i != 0:
                self.forwardHashTable[i] = ((self.forwardHashTable[i - 1] *
                                            self.bases[0]) * self.mods[0] +
                current) % self.mods[0];

            else:
                self.forwardHashTable[i] = current

    def makeBackwardHashTable(self, string):
        sz = len(string)
        self.backwardHashTable = [] * sz;
        for i in range(sz -1, 0, -1):
            current = string[i] - ' ';

            if i != sz - 1:
                self.backwardHashTable[i] = ((self.backwardHashTable[i - 1] *
                                            self.bases[0]) * self.mods[0] +
                current) % self.mods[0];

            else:
                self.backwardHashTable[i] = current


    def getForwardHashingQuery(self, left, right):
        if(left == 0):
            return self.forwardHashTable[right];

        else:
            return self.MOD(self.forwardHashTable[right] - (self.forwardHashTable[left
                                                                       - 1]
                       * self.power[right - left + 1]) % self.mods[0])
    def getBackwardHashingQuery(self, left, right = None):
        if(left == None):
            return self.forwardHashTable[left];

        else:
            return self.MOD(self.backwardHashTable[left] -
                            (self.backwardHashTable[right
                                                                       + 1]
                       * self.power[right - left + 1]) % self.mods[0])


    def MOD(self, x):
        return (x % self.mods[0] + self.mods[0]) % self.mods[0]


def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    sys.setrecursionlimit(200000)
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
