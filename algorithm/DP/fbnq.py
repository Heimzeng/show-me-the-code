def fbnq(n):
    res = []
    for i in range(n):
        if i < 2:
            res.append(i)
        else:
            res.append(res[i-1] + res[i-2])
    return res[n-1]

if __name__ == '__main__':
    print(fbnq(100))