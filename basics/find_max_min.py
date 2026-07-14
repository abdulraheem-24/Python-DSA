numbers = [1,2,3,2,1,3,2,457,8,53,2,654,1231]

def f_mx_mn () :
    large = numbers[0]
    mini = numbers[0]
    for i in range(1,len(numbers)):
        if (numbers[i] > large) : large = numbers[i]; 
        if (numbers[i] < mini) : mini = numbers[i]; 

    return mini , large

print(f_mx_mn())
