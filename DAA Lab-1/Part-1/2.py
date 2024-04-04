import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    start = time.time()
    for i, num in enumerate(arr):
        if num == target:
            return (time.time() - start) * 10**6  # Convert to microseconds
    return -1

def binary_search(arr, target):
    start = time.time()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return (time.time() - start) * 10**6  # Convert to microseconds
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [random.randint(1, 1000) for _ in range(10000)]
key = random.choice(arr)  # Generate a search key from the array itself
print("Search key is", key)

linear_times = []
binary_times = []

for _ in range(5):
    linear_times.append(linear_search(arr, key))
    arr.sort()  # Binary search requires a sorted array
    binary_times.append(binary_search(arr, key))

print("Linear search times (microseconds):", linear_times)
print("Binary search times (microseconds):", binary_times)

plt.plot(range(1, 6), linear_times, label='Linear Search')
plt.plot(range(1, 6), binary_times, label='Binary Search')
plt.xlabel('Trial')
plt.ylabel('Time (microseconds)')
plt.title('Execution Time for Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.show()
