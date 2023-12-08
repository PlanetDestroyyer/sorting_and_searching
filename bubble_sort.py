import timeit
def bubble_sort(nums):
    arr = len(nums)
    for i in range(arr-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1] , nums[j]


nums = [2, 3, 5, 9, 1, 5,11,23,43,54]
bubble_sort(nums)
print(nums)
time_selection_sort = timeit.timeit(lambda: bubble_sort(nums.copy()), number=1)
print(f"bubble Sort: {time_selection_sort} seconds")