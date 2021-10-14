"""
Bubble_sort(A)
    for i = 1 to A.length - 1
        for j = A.length down to i + 1
            if A[j] < A[i - 1] :
                swap A[j] <-> A[j - 1]
"""


def BubleSort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) -i -1):
            # print(i, j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] # swap
    return array

a = [7,4,5,1,3]
print(a)
print(BubleSort(a))

b = [-2, 45, 0, 11, -9]
print(b)
print(BubleSort(b))