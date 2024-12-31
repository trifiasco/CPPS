
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def solve(caseno):

    first = input();
    second = input();

    first = first.upper()
    second = second.upper()

    mp_a = dict()
    mp_b = dict()

    for char in first:
        if char == ' ':
            continue;
        key = ord(char) - 65;
        if key in mp_a:
            mp_a[key] += 1;
        else:
            mp_a[key] = 1;
    for char in second:
        if char == ' ':
            continue;
        key = ord(char) - 65;
        if key in mp_b:
            mp_b[key] += 1;
        else:
            mp_b[key] = 1;

    flag = 1;

    for i in range(26):
        freq_a = mp_a[i] if i in mp_a else -1;
        freq_b = mp_b[i] if i in mp_b else -1;

        if freq_a != freq_b:
            flag = 0;
            break;

    print('Case %d: %s' %(caseno, 'Yes' if flag == 1 else 'No'))

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
