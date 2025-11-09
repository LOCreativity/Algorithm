def binary_search(arr, target):
    low = 0 # 첫번째 인덱스
    high = len(arr) - 1 # 마지막 인덱스

    # 반복문을 통해 low와 high가 교차할 때까지 실행
    while low <= high:
        mid = (low + high) // 2

        # target 값과 mid 값이 같으면 mid가 target이므로 mid 반환
        if arr[mid] == target:
            return mid

        # target이 mid보다 크면 low를 mid+1로 업데이트하여 범위를 오른쪽으로 줄임
        elif arr[mid] < target:
            low = mid + 1

        # target이 mid보다 작으면 high를 mid-1로 업데이트하여 범위를 왼쪽으로 줄임
        else:
            high = mid - 1
    # target이 없는 경우 -1 반환
    return -1