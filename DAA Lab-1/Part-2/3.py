import heapq

def find_k_largest_elements(arr, k):
    if k >= len(arr):
        return arr
    
    # Create a min-heap of size K
    heap = arr[:k]
    heapq.heapify(heap)
    
    # Iterate through the remaining elements
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)  # Remove the smallest element from the heap
            heapq.heappush(heap, arr[i])  # Push the current element to the heap
    
    # The heap now contains the K largest elements
    return heap

# Function to take user input for the array
def get_array_from_user():
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    return arr

# Function to take user input for the value of K
def get_k_from_user():
    k = int(input("Enter the value of K: "))
    return k

# Example usage:
arr = get_array_from_user()
k = get_k_from_user()

k_largest_elements = find_k_largest_elements(arr, k)
print(f"The {k} largest elements in the array are:", k_largest_elements)
