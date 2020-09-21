def quicksort(nums):
    qsort(nums, 0, len(nums)-1)
    return nums

def qsort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        qsort(nums, low, p-1)
        qsort(nums, p+1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


x = [1,5,3,2,8,7,6,4]
print(quicksort(x))