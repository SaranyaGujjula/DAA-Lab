import random
import time
import matplotlib.pyplot as plt

# Function to generate random numbers
def generate_random_numbers(n):
    return [random.randint(1, 10000) for _ in range(n)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate random numbers
random_numbers = generate_random_numbers(1000)

# Measure time taken for each sorting algorithm
sorting_algorithms = [bubble_sort, selection_sort, insertion_sort]
sorting_times = []

for sort_algo in sorting_algorithms:
    start_time = time.time()
    sorted_numbers = random_numbers.copy()
    sort_algo(sorted_numbers)
    end_time = time.time()
    sorting_time = end_time - start_time
    sorting_times.append(sorting_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(["Bubble Sort", "Selection Sort", "Insertion Sort"], sorting_times, color=['red', 'green', 'blue'])
plt.xlabel("Sorting Algorithm")
plt.ylabel("Time Taken (seconds)")
plt.title("Time Taken by Different Sorting Algorithms")
plt.show()
