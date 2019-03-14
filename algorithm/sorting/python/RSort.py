import math
import random

def RSort(arr, radix=10):
    K = int(math.ceil(math.log(max(arr)+1, radix)))
    for i in range(1, K+1):
        bucket = [[] for j in range(radix)]
        for val in arr:
            bucket[val%(radix**i)//(radix**(i-1))].append(val)
        del arr[:]
        for each in bucket:
            arr.extend(each)
    return arr
if __name__ == '__main__':
    data = [random.randint(0, 10000) for i in range(100000)]
    data = RSort(data)
    print(data)