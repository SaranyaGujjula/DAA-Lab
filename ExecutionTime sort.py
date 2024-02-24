import timeit
import random

# Bubble Sort
A_bubble = [random.randint(1, 100) for _ in range(100)]

def bubble_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

swaps_bubble = bubble_sort(A_bubble.copy())

bubble_time = timeit.timeit(lambda: bubble_sort(A_bubble.copy()), number=1000)

print("Bubble Sort:")
print("Randomly generated array:", A_bubble)
print("Sorted array:", sorted(A_bubble.copy()))
print("Execution Time: %.8f seconds" % (bubble_time / 1000))  # Divide by 1000 for average time
print("Number of Swaps: %d" % swaps_bubble)
print()

# Selection Sort
A_selection = [random.randint(1, 100) for _ in range(100)]

def selection_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return swaps

swaps_selection = selection_sort(A_selection.copy())

selection_time = timeit.timeit(lambda: selection_sort(A_selection.copy()), number=1000)

print("Selection Sort:")
print("Randomly generated array:", A_selection)
print("Sorted array:", sorted(A_selection.copy()))
print("Execution Time: %.8f seconds" % (selection_time / 1000))  # Divide by 1000 for average time
print("Number of Swaps: %d" % swaps_selection)
print()

# Python's built-in sorted function (Timsort)
array1 = [random.randint(1, 100) for _ in range(100)]

sort_time = timeit.timeit(lambda: sorted(array1.copy()), number=1000)

print("Python Sorted (Timsort):")
print(array1)
print("Execution Time: %.8f seconds" % (sort_time / 1000))  # Divide by 1000 for average time
