inputList = [12,11,9,8,7,6,5,4,3,2,1]
def bubbleSort(a):
    print(f'initial: {a}')
    def swap(x, y):
        a[x], a[y] = a[y], a[x]
    for j in range(len(a) - 1, 0, -1):
        for i in range(j):
#            print(f'a[i]: {a[i]}, a[i+1]: {a[i+1]}')
            if a[i] > a[i + 1]:
                swap(i, i+1)
        print(a)
    return a


print(bubbleSort(inputList))
