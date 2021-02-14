arr = [3,5,4,1,6,2]


def partition(start, end):
    pivot = arr[start]
    low = start+1
    high = end

    while low <= high:
        while low <= high and arr[low] <= pivot:
            low += 1

        while low <= high and arr[high] >= pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]

    arr[start], arr[high] = arr[high], arr[start]

    return high


def quick_sort(start, end):
    if start >= end:
        return 

    part = partition(start, end)
    quick_sort(start, part-1)
    quick_sort(part+1, end)


quick_sort(0, len(arr)-1)
print(arr)