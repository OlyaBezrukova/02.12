def my_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a == 1:
        return b + 1
    else:
        return my_sum(a-1, b+1)
print("Give two numbers")
a, b = int(input()), int(input())
print("Sum: ", my_sum(a,b))
    
