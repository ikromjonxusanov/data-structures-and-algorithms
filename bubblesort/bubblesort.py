def bubbleSort(arr):
    n = len(arr)
    c = 0
    for i in range(n):
        for j in range(n-i-1):
            c += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"{c} -", arr)
    print("--------------------------")
arr = [64, 34, 25, 12, 22, 90, 11]
print(str(arr)+"\n--------------------------")
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    if i == len(arr)-1:
        print("%d" % arr[i], end="")
    else:
        print("%d" % arr[i], end=", ")
