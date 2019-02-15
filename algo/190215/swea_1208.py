for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(1, dump + 1):
        index_max = box.index(max(box))
        index_min = box.index(min(box))
        box[index_max] += -1
        box[index_min] += 1
        result = max(box) - min(box)
        if result == 1 or 0:
            break

    print(f'#{tc} {result}')