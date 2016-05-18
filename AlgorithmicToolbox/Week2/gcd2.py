# Uses python3
a, b = [int(x) for x in input().split()]

if a < b:
    a, b = b, a


def gcd(a, b):
    if b == 0:
        return(a)
    a_new = a % b
    return(gcd(b, a_new))

print(gcd(a, b))
