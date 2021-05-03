n = int(input())
temp_sum = 0
temp_list = []
min = list(map(int, input().split()))
min.sort()

for i in range(n):
    temp_sum += min[i]
    temp_list.append(temp_sum)
print(sum(temp_list))
