# 정려뢴 리스트 반환
def merge_sort(lst):
    #리스트의 길이가 1 이하인 경우 그대로 반환
    if len(lst) <= 1:
        return lst

    # 리스트를 반으로 나누어 재귀적으로 호출
    mid = len(lst) // 2
    left = merge_sort(lst[:mid]) # 첫 번째부터 중간까지의 요소
    right = merge_sort(lst[mid:]) # 중간부터 마지막까지의 요소
    return merge(left, right) # 병합

# 두 개의 정렬된 리스트 병합
def merge(left, right):
    result = []
    while left and right: # 리스트가 모두 비어있지 않은 동안 반복문을 실행
        # left와 right의 첫 번째 요소를 비교하고, 작은 값을 result에 추가
        if left[0] < right[0]:
            # 추가한 요소는 원본 리스트에서 제거
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 남아있는 리스트의 모든 요소를 result에 추가
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    #정렬이 완료된 result 리스트 반환
    return result