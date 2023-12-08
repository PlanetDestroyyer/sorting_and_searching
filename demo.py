def bubble_sort(nums):
    arr = len(nums)
    for i in range(arr-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


nums = [2, 3, 5, 9, 1, 6]
bubble_sort(nums)
print(nums)


def selection_sort(nums):
    arr = len(nums)
    for i in range(arr):
        min_pos = i
        for j in range(i, arr):
            if nums[min_pos] > nums[j]:
                min_pos = j

        nums[i], nums[min_pos] = nums[min_pos], nums[i]


nums = [2, 3, 5, 9, 1, 5, 7, 23, 54]
selection_sort(nums)

print(nums)


def selection_sort2(nums):
    arr = len(nums)
    for i in range(arr):
        min_pos = i
        for j in range(i, arr):
            if nums[min_pos] > nums[j]:
                min_pos = j
        nums[i], nums[min_pos] =nums[min_pos], nums[i]


nums = [2, 3, 5, 9, 1, 5, 7, 23, 54]
selection_sort2(nums)

print(nums)

def bubble_sort2(nums):
    arr = len(nums)
    for i in range(arr-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                nums[j], nums[j+1] =  nums[j+1], nums[j]




nums = [2, 3, 5, 9, 1, 6]
bubble_sort2(nums)
print(nums)


def quick_sort(nums):
    arr = len(nums)
    if arr <= 1:
        return nums
    else:
        pivot = nums.pop()
    
    low = []
    high = []

    for i in nums:
        if i < pivot:
            low.append(i)
        else:
            high.append(i)
        
    
    return quick_sort(low) + [pivot] + quick_sort(high)

nums = [2, 3, 5, 9, 1, 5,11,23,43,54]

sorted_nums = quick_sort(nums) 
print(sorted_nums)

def insertion_sort(nums):
    arr = range(1,len(nums))
    for i in arr:
        start = nums[i]

        while nums[i-1] > start and i>0:
            nums[i] , nums[i-1] = nums[i-1] , nums[i]
            i = i-1

    return nums


nums = [2,3,5,9,1,5,-3]
sorted = insertion_sort(nums)
print(sorted)