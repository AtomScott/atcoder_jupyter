#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]", C: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    C = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        C[i] = int(next(tokens))
    solve(N, S, C)

if __name__ == '__main__':
    main()