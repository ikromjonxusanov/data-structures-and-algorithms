import random


def findMax(arr : list):
    max = arr[0]
    max_index = 0
    for n in range(len(arr)):
        if arr[n] > max:
            max = arr[n]
            max_index = n
    return max_index

def selectionSort(arr : list):
    newArr = []
    for i in range(len(arr)):
        max_index = findMax(arr)
        newArr.append(arr.pop(max_index))
    return newArr

arr = [random.randint(1, 100) for i in range(10)]
print(arr)
print(selectionSort(arr))