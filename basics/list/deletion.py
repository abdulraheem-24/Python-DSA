# deletion at the end 
# time complexity = O(1) amortized

numbers = [1,2,3,4,5]
numbers.pop()
print(numbers)




# insertion at the middle or begenning 
# time complexity = O(n)  "need shifing"

def deleteval (arr , i) :
   
    for r in range(i , len(arr) - 1):
        arr[r] = arr[r + 1]
    numbers.pop()
    return arr

print(deleteval(numbers, 1,))



