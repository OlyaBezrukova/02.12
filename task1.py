def min4(a,b,c,d):
    k = min(a,b)
    l = min(c,d)
    return min(k,l)
print("Give four numbers")
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print("Min:", min4(a,b,c,d))
