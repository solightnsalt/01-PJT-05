import sys

sys.stdin = open("_Flatten.txt")

for tc in range(1, 11):
    dump_ = int(input())
    boxes = list(map(int, input().split()))
    # print(boxes)
    for i in range(dump_):
        if max(boxes) - min(boxes) > 1:
            # boxes.index[max(boxes)] = max(boxes) - 1 안 됨
            max_idx = boxes.index(max(boxes))
            min_idx = boxes.index(min(boxes))
            boxes[max_idx] = max(boxes) - 1 
            boxes[min_idx] = min(boxes) + 1
        else:
            break
    print(f'#{tc}', max(boxes) - min(boxes))