"""
Selection sort(A, n)
# input: array
# output: sorted array
    for i = 1 to n - 1
        # set current element as minimum index
        MinIndex = i
        for j = i + 1 to n
            MinIndex = j
                if A[j] < A[MinIndex]
                swap A[i] <-> A[MinIndex]
"""

def SelectionSort(array):
    for i in range(len(array) - 1):
        MinIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[MinIndex]:
                MinIndex = j
            array[i], array[MinIndex] = array[MinIndex], array[i]
            print(array)
    return array


a = [20, 12, 10, 15, 2]
print(SelectionSort(a))
