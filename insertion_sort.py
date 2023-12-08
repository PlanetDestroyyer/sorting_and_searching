import timeit
def insertion_sort(nums):
    arr = range(1 , len(nums))
    for i in arr:
        start = nums[i]

        while nums[i-1] > start and i>0 :
            nums[i] , nums[i-1]= nums[i-1] , nums[i]
            i= i-1
    
    return nums

nums = [2, 3, 5, 9, 1, 5,11,23,43,54]
sorted = insertion_sort(nums)
print(sorted)
time_selection_sort = timeit.timeit(lambda: insertion_sort(nums.copy()), number=1)
print(f"insertion Sort: {time_selection_sort} seconds")