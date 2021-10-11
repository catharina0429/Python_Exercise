# Introduction to Algorithms 3rd edition
# Exercise 2.1-1 Insertion-sort
A = [31, 41, 59, 26, 41, 58]
def insertion_sort(array):
    for j in range(1, len(array)):
        i = j - 1
        key = array[j]
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array

print(insertion_sort(A))

def InsertionSort(array):
    for end in range(1, len(array)):
        for i in range(end, 0, -1):
            if array[i - 1] > array[i]:
                array[i - 1] , array[i] = array[i], array[i - 1]
            else:
                break
    return array

print(InsertionSort(A))
