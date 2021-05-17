import sys

n = int(sys.stdin.readline())
temp = []
for i in range(n):
    m = list(sys.stdin.readline().split())
    if m[0] == 'push':
        temp.append(m[1])
    elif m[0] == 'pop':
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[-1])
            temp.pop()
    elif m[0] == 'size':
        print(len(temp))
    elif m[0] == 'empty':
        if len(temp) == 0:
            print(1)
        else:
            print(0)
    elif m[0] == 'top':
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[-1])
