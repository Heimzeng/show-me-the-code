def swap(list, index1, index2):
    #print("swap " + str(list[index1]) + " and " + str(list[index2]))
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    #print(list)

def quick_sort(list, begin, end):
    if begin >= end:
        return
    left = begin
    right = end
    first = list[begin]
    while True:
        while list[right] >= first and left < right:
            right -= 1
        while list[left] <= first and left < right:
            left += 1
        if left == right:
            break
        swap(list, left, right)
    swap(list, begin, left)
    quick_sort(list, begin, left - 1)
    quick_sort(list, left + 1, end)

if __name__ == "__main__":
    list = [3, 2, 7, 4, 5, 9, 1, 8, 0, 6,]
    quick_sort(list, 0, len(list) - 1)
    print(list)