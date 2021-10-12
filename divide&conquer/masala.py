def sum(arr:list):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

def list_length(arr:list):
    if arr == []:
        return 0
    return 1 + list_length(arr[1:])
# print(list_length([10, 324, 4, 23, 34, 234]))

def list_max(list):
    if len(list) <= 1:
        return list[0]
    else:
        m = list_max(list[1:])
        return m if m > list[0] else list[0]

# print(list_max([4, 2, 76, 8, 1354, 44656, 25, 234]))

def binarySearch(array, value, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return binarySearch(array, value, start, mid-1)
    else:
        return binarySearch(array, value, mid+1, end)
arr = [1, 2, 3, 4, 5, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300]
print(binarySearch(arr, 20))
print(arr[9])