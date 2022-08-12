import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    PS = []
    # print(N, cards)
    #카드 먼저 반으로 나누기
    if N % 2 == 0:
        d1 = cards[0:(N//2)]
        d2 = cards[(N//2)::]
        # print(d1, d2)
    else:
        d1 = cards[0:(N//2)+1]
        d2 = cards[(N//2)+1::]
        # print(d1, d2)
    while len(d1): #번갈아가면서 섞기
        PS.append(d1.pop(0))
        if not len(d2) == 0:
            PS.append(d2.pop(0))
        else:
            break
    
    print(f'#{tc}', *PS)