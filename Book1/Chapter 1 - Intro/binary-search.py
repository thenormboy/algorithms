# Binary Search function takes two parameters (sortedArray, item)
# sortedArray is an array that has been sorted before put in the function
# item is the object that is being searched for in the array
# The function returns index of item if item is found in sortedArray and None otherwise
        
def binarySearch(sortedArray, item):
    low = 0
    high = len(sortedArray) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = sortedArray[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# binarySearchMaxSteps takes one parameter (array)
# array is the array that is to be binary searched
# returns the maximum number of steps required to perform binary search of the array

def binarySearchMaxSteps(array):
    size = len(array) - 1
    steps = 1

    while(size > 1):
        steps += 1
        size = int(size / 2)
    return steps