import sys

k = int(sys.stdin.readline())

temp = []
for i in range(k):
    n = int(input())
    if n == 0:
        temp.pop()
    else:
        temp.append(n)

print(sum(temp))
