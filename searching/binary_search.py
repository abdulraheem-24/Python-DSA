
numbers = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(key):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == key:
            return middle
        elif numbers[middle] < key :
            left = middle + 1
        else : 
            right = middle - 1

print(binarySearch(9))