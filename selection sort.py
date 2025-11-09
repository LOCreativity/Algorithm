# 선택 정렬 구현
list = [5, 2, 8, 9, 3]

for i in range(len(list)):
    min_index = i
    for j in range(i + 1, len(list)):
        if list[min_index] > list[j]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[i]

print(list)
