import sys

sys.stdin = open("_등산로조성.txt")

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    site = [list(map(int, input().split())) for _ in range(N)]
    # print(site)