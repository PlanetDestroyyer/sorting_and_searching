pos = 0

def binary_search(nums, tar):
    nonlocal pos
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == tar:
            pos = mid
            return True
        else:
            if nums[mid] < tar:
                low = mid + 1
            else:
                high = mid - 1

    return False

nums = [1, 2, 3, 5, 5, 9, 11, 23, 43, 54]
tar = 11

if binary_search(nums, tar):
    print("Found at", pos)
else:
    print("Not Found")