import random

c = 0
def qsort(arr:list):
    global c
    if len(arr) < 2:
        return arr
    else:
        c += 1

        pivot = arr.pop(random.randrange(len(arr)))
        kichik = [i for i in arr if i <= pivot]
        katta = [i for i in arr if i > pivot]
        print(f"{c} - {kichik} + {pivot} + {katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

arr = [64, 34, 25, 12, 22, 90, 11]
print(arr)
print("-"*40)
print(qsort(arr))