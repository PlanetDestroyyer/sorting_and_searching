import timeit
def quick_sort(nums):
    arr = len(nums)
    if arr <= 1:
        return nums
    else:
        pivot = nums.pop()

    high = []
    low = []

    for i in nums:
        if i > pivot:
            high.append(i)
        else:
            low.append(i)

    return quick_sort(low) + [pivot] + quick_sort(high)

nums = [2, 3, 5, 9, 1, 5,11,23,43,54]
sorted_nums = quick_sort(nums) 
print(sorted_nums)
time_selection_sort = timeit.timeit(lambda: quick_sort(nums.copy()), number=1)
print(f"Quick Sort: {time_selection_sort} seconds")