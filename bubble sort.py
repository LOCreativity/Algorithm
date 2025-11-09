# 버블 정렬 구현
list = [5, 2, 8, 9, 3]

for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)