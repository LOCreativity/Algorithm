"""
이진 탐색 구현 코드
탐색 전제조건: 리스트가 정렬된 리스트여야 함
시작점, 중간점, 끝점을 이용
탐색 한 단계마다 리스트의 크기가 반절씩 줄어듦(시간 복잡도 O(logN))
"""
def binary_search(sortedList, searchNum):
    start = 0
    end = len(sortedList) - 1

    while start <= end:
        mid = (start + end) // 2
        if sortedList[mid] == searchNum: return mid
        elif sortedList[mid] > searchNum: end = mid - 1
        else: start = mid + 1

    return -1


a = [6, 28, 21, 16, 3, 19, 34]
a.sort() # 리스트 정렬
print(binary_search(a, 35))