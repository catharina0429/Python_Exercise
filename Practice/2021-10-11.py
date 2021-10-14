# Introduction to Algorithms 3rd edition
"""
INSERTION-SORT(A)
1   for j = 2 to A.length
2       key = A[j]
3       # Insert A[j] into the sorted sequence A[1 ....j-1]
4       i = j - 1
5       while i > 0 and A[i] > key
6           A[i + 1] = A[i]
7           i = i - 1
8       A[i + 1] = key
"""
# Exercise 2.1-1 Insertion-sort

def insertion_sort(array):
    for j in range(1, len(array)):
        i = j - 1
        key = array[j]
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array
A = [31, 41, 59, 26, 41, 58]
# print(A)
print(insertion_sort(A))

def InsertionSort(array):
    for end in range(1, len(array)):
        for i in range(end, 0, -1):
            if array[i - 1] > array[i]:
                array[i - 1] , array[i] = array[i], array[i - 1]
            else:
                break
            print(array)
    return array

print(InsertionSort(A))

b = [2, 4, 5, 1, 3]
# print(b)
print(InsertionSort(b))