def solution():
    n = 101
    while n > 100 and n < 1000000:
        digitals = 0
        n_copy = n
        while n_copy > 0:
            n_copy = int(n_copy / 10)
            digitals += 1
        # num = ''
        # n_copy = n
        # k = digitals - 1
        # while k > 0:
        #     num = num.join(str(int(n_copy/pow(10, k))))
        #     print(n_copy)
        #     n_copy -= pow(10, k)
        #     print(n_copy)
        #     k -= 1
        num = str(n)
        i = 0
        j = 0
        middle = int(digitals / 2)
        if digitals % 2 == 0:
            j = middle
            i = j - 1
        else:
            i = middle - 1
            j = middle + 1
        if num[i] == num[j] and num[j] == num[middle]:
            while i >= 0:
                if num[i] == num[j]:
                    i -= 1
                    j += 1
                    continue
                else:
                    break
            if i == -1:
                print(num)
        n += 1
if __name__ == '__main__':
    solution()
