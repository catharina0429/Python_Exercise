"""
# 배열을 1/2로 나눠서 다시 합치면서 정렬하는 방식
MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    Let LeftArray[1,...,n1 + 1] and RightArray[1,...,n2 + 1]
    for i = i to n1
        LeftArray[i] = A[p + i -1]
        for j = 1 to n2
            RightArray[j] = A[q + j]
    LeftArray[n1 + 1] = Inf
    RightArray[n2 + 1] = Inf
    i = 1
    j = 1
    for k = p to r
        if LeftArray[i] <= RightArray[j]
            A[k] = LeftArray[i]
            i = i + 1
        else
            A[k] = RightArray[j]
            j = j + 1
"""

a = [6,7,2,3,9,5,1]
print(len(a)//2)
print(a[3:])
print(a[:3])
def MergeSort(array):
    length = len(array)
    # 종료 조건 : 정렬할 요소가 1개인 경우
    if length <= 1:
        return array
    # 그룹을 나누어 재귀적으로 정렬함
    mid_len = length // 2 # p와 r을 더해서 2로 나눈 후 정수로 만듧
    # 각각의 하위 배열을 재귀적으로 정렬함
    g1 = MergeSort(array[:mid_len])
    g2 = MergeSort(array[mid_len:])

    # 정렬된 두 하위 배열을 하나의 정렬된 하위배열로 결합
    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

print(MergeSort(a))

b = [14, 7, 3, 12, 9, 11, 6, 2]
print(MergeSort(b))

# The time complexiti of merge sort is O(n * lg n)