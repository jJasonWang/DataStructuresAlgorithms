# Uses python3
n = int(input())

f = [0, 1]
for i in range(n - 1):
    f.append(f[i] + f[i + 1])

print(f[-1])
