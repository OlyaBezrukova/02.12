def my_power(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * my_power(a, n-1)
print("Give a number and a prime power you want")
a, n = int(input()), int(input())
print("Result:", my_power(a,n))

