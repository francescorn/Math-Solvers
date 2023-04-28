x = int(input("Type the first number: "))
y = int(input("Type the second number: "))

def lcm(x, y, z):
    if x + 1 == z or y + 1 == z:
        return -1
    
    if x % z == 0 and y % z == 0:
        return z
    
    return lcm(x, y, z + 1)

print(lcm(x, y, 2))
