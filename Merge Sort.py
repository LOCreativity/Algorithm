"""
기본 조건(종료 조건): 배열의 길이가 1일 때
재귀 조건: 배열의 길이가 1보다 클 때
배열을 분할할 가운데 위치를 구한다.
배열의 왼쪽 하위 배열에 대해 합병 정렬한다. → 재귀 호출
배열의 오른쪽 하위 배열에 대해 합병 정렬한다. → 재귀 호출
정렬된 두 배열을 합병한다. → merge 함수 호출
"""

def merge(left, right):
    res = []
    index1 = index2 = 0 # 서로의 리스트 0번째부터 원소를 비교하기 위함
    while index1 < len(left) and index2 < len(right):
        if left[index1] <= right[index2]: # 각 0번째 원소의 크기 비교(왼쪽 리스트 0번째 원소가 작거나 같을 경우)
            res.append(left[index1]) # res 리스트에 왼쪽 리스트 0번째 원소 추가
            index1 += 1 # 왼쪽 리스트의 다음 원소부터 비교
        else:
            res.append(right[index2])
            index2 += 1

    if index1 == len(left): # 왼쪽 리스트의 원소들을 res 리스트에 모두 추가했을 경우
        res += right[index2:] # 오른쪽 리스트가 남았을 것이므로 오른쪽 리스트의 남은 원소들 모두 추가
    else:
        res += left[index1:]

    return res

def merge_sort(list):
    if len(list) == 1: return list # 리스트 원소가 1개이면 그대로 반환
    mid = len(list) // 2 # 가운데 인덱스 계산
    left = merge_sort(list[:mid]) # 0 ~ (mid-1)까지의 원소
    right = merge_sort(list[mid:]) # mid ~ 마지막까지의 원소
    return merge(left, right) # 두 배열 합병

list = [24, 26, 2, 16, 32, 31, 25, 12]
print(merge_sort(list))
