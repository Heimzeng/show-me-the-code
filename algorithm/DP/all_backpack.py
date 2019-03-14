def all_backpack(items, C):
    res = []
    items.sort()
    # remove items > C
    for i in range(C + 1):
        if i == 0:
            res.append(0)
            continue
        temp = 0
        for it in items:
            if i - it >= 0:
                temp = max(temp, res[i-it] + it)
        res.append(temp)
    print(res)

if __name__ == '__main__':
    all_backpack([2, 3, 4, 5, 9], 10)