import sys
import os

LOCAL_ENV: bool = os.environ.get("USER") == "trifiasco"


def SET_LOCAL_READ() -> None:
    sys.stdin = open("debug/in.txt", "r")  # input file
    # sys.stdout = open('out.txt', 'w')


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    if LOCAL_ENV:
        SET_LOCAL_READ()

    while True:
        try:
            n: int = int(input())
            print(n)
            # do stuff
        except EOFError:
            break
    pass
