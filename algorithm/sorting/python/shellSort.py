def shellSort(list):
    n = len(list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = gap // 2
    return list

import random
if __name__ == '__main__':
    m = 10000
    l = [random.randint(0, m) for i in range(m)]
    shellSort(l)
    print(l)