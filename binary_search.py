# declaring a variable pos
pos = 0
#defing function
def binary_search(nums,tar):
    low = 0 #assing low to 0
    high = len(nums)-1 # assinging high to last index in list

    while low <= high:#assiging a loop and setting the condition that low shouldnt be greater than high
        mid = (low+high)//2 #diving the list and  two parts and making index to median element
        if nums[mid] == tar : #cheching if mid is equal to tar we want to find
            globals() ['pos'] = mid #assinging the index to pos 
            return True
        else:
            if nums[mid] < tar:#cheching if the element is less than the tar
                low  = mid # if so then we are reassigning value to low 
            else :
                high = mid #if no then reassignin value to high

    

#list of numbers
nums = [1, 2, 3, 5, 5, 9, 11, 23, 43, 54]
tar = 11

if binary_search(nums,tar):
    print("Found at " ,pos )
else:
    print("Not Founded")