def my_div(n):
    i = 1
    max = 1
    while i < n:
        if n % i == 0:
            max = i
        i = i + 1
    if max == 1 and n != 1:
        max = n
    return max
print("Give a number:")
a = int(input())
print("Maximum divisor:", my_div(a))
