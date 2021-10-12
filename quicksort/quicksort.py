import random


def qsort(arr:list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(random.randrange(len(arr)))
        kichik = [i for i in arr if i <= pivot]
        katta = [i for i in arr if i > pivot]
        print(f"{kichik} + {pivot} + {katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

arr = [random.randint(1, 100) for i in range(1 ,21)]
print(arr)
print("-"*40)
print(qsort(arr))