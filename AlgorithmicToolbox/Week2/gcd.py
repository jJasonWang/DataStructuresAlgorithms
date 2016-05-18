# Uses python3
a, b = [int(x) for x in input().split()]

gcd = 0
for i in range(1, min(a, b) + 1):
    if (a % i == 0) & (b % i == 0):
        gcd = i

print(gcd)
