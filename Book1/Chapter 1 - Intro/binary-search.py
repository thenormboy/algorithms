# Binary Search function takes two parameters (sortedArray, item)
# sortedArray is an array that has been sorted before put in the function
# item is the object that is being searched for in the array
# The function returns true if item is found in sortedArray and false otherwise

def binarySearch(sortedArray, item):
    low = 0
    high = len(sortedArray) - 1
    mid = (low + high) / 2

    while (True):
        if (mid == low or mid == high):
            return False
        elif (item > mid):
            low = mid
            mid = (low + high) / 2
        elif (item < mid):
            high = mid
            mid = (low + high) / 2
        elif (item == mid):
            return True
        
def binarySearch2(sortedArray, item):
    low = 0
    high = len(sortedArray) - 1

    while low <= high:
        mid = (low + high)
        guess = sortedArray[mid]

        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False
        
testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binarySearch2(testArray, 4))