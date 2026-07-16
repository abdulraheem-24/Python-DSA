
numbers = [1,2,3,4,5,6,7]

def reverselist (li) :
    l = 0
    r = len(li) - 1
    while l < r :
        temp = li[l]
        li[l] = li[r]
        li[r] = temp
        l += 1
        r -= 1
    return li

print(reverselist(numbers))

# time complexity = O(n)