import sys

sys.stdin = open("_반반.txt")

T = int(input())
for tc in range(1, T+1):
    S = input()
    SS = list(set(S))
    # print(SS, len(SS)) 22213
    if len(SS) != 2:
        print(f'#{tc}', 'No')
    else:
        if S.count(SS[0]) == 2 and S.count(SS[1]) == 2:
            print(f'#{tc}', 'Yes')
        else:
            print(f'#{tc}', 'No')