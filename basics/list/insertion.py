# insertion at the end 
# time complexity = O(1) amortized

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)




# insertion at the middle or begenning 
# time complexity = O(n)  "need shifing"

def inserting (arr , i , val) :
    arr.append(None)
    for r in range(len(arr) - 1, i , -1):
        arr[r] = arr[r - 1]
    arr[i] = val
    return arr

print(inserting(numbers, 1, 10))





# task


def insertscore(scores , val) :
    scores.append(None)
    i = len(scores) - 2
    while i >= 0 and scores[i] < val:
        scores[i+1] = scores[i]
        i -= 1
    scores[i + 1] = val
    return scores
    
scores = [95, 90, 87, 80, 72]
print(insertscore(scores,100))
