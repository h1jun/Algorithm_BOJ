n, m = map(int, input().split())

if n == 1:
    count = 1
elif n == 2:
    count = min(4, (m+1)//2)
else:
    if m <= 6:
        count = min(4,m)
    else:
        count = m-2
print(count)