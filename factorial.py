def factorial_iterative(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        x = 1
        while(n > 1):
            x *= n
            n -= 1
        return x
print(factorial_iterative(int(input("Enter a positive integer: "))))

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)
print(factorial_recursive(int(input("Enter a positive integer: "))))
