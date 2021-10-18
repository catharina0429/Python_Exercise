"""
Quick sort
- Merge sort와 마찬가지로 Devide and Conquer과 recursion을 사용함
- 가운데를 기준으로 분할하는 merge sort와 달리 pivot이라 불리는 임의의 기준값을 사용
- pivot을 기준으로 작은 값(보통 왼쪽)과 큰 값(보통 오른쪽)의 그룹으로 divide(혹은 partitioning이라고도 부름)
- O(n lg n)의 시간복잡도를 지님
"""

a = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]

def QuickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    # 시간복잡도 O(n^2)를 피하기 위해 중앙값을 pivot 값으로 취해줌
    lesser_array, equal_array, greater_array = [], [], []
    for arr in array:
        if arr < pivot:
            lesser_array.append(arr)
        elif arr > pivot:
            greater_array.append(arr)
        else:
            equal_array.append(arr)
    return QuickSort(lesser_array) + equal_array + QuickSort(greater_array)

print(QuickSort(a))

def quick_sort(array):
    # 종료조건
    if len(array) <= 1:
        return array
    # pivot은 첫번째 element, 나머지는 tail
    pivot, tail = array[0], array[1:]

    left = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행 recursive method, 전체 리스트를 반환
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(a))

import time
import random

ls = [x for x in range(10001)] # 10000개의 element를 갖는 리스트
random.shuffle(ls) # 무작위로 섞기
# print(ls)

start = time.time()
QuickSort(ls)
time1 = time.time() - start

start = time.time()
quick_sort(ls)
time2 = time.time() - start

print("첫번째 알고리즘 실행시간: ", time1)
print("두번째 알고리즘 실행시간: ", time2)