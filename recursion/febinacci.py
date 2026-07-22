def febinacci(n):
    if n <= 1:
        return 1
    
    return febinacci(n-1) + febinacci(n-2)

print(febinacci(10))
