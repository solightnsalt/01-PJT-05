import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
for tc in range(1, T+1):
    
    N, M = map(int, input().split())
    villager = [[] for _ in range(N+1)] #1번~N번사람 
    
    for i in range(M):
        v1, v2 = map(int, input().split())
        villager[v1].append(v2)
        villager[v2].append(v1)
    # print(villager)
    
    visited = [False] * (N+1) 
    cnt = 0
   
    for i in range(1, N+1): 
        if visited[i] == False:
            cnt += 1
            stack = [i]
            visited[i] = True

        while stack:
            current = stack.pop()

            for adj in villager[current]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)                    
    print(f'#{tc} {cnt}')  
    
    # ㅡ.ㅡ