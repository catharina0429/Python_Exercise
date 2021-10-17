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
    pivot = array[len(array) // 2] # 중앙값을 pivot값으로 취해줌
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