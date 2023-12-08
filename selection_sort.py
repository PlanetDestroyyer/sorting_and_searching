import timeit
def selection_sort(nums):
    arr = len(nums)
    for i in range(arr):
        min_pos = i
        for j in range(i,arr):
            if nums[j] < nums[min_pos] :
                min_pos = j
        

        nums[i],nums[min_pos] = nums[min_pos] , nums[i]



nums = [2, 3, 5, 9, 1, 5,11,23,43,54]
selection_sort(nums)
print(nums)
time_selection_sort = timeit.timeit(lambda: selection_sort(nums.copy()), number=1)
print(f"Selection Sort: {time_selection_sort} seconds")