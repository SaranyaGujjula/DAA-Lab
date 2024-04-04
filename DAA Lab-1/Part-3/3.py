def find_swapped_elements(arr):
    first_swapped = None
    last_swapped = None
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            first_swapped = i
            break
            
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            last_swapped = i
            break
            
    return first_swapped, last_swapped

def sort_array_linear(arr):
    first_swapped, last_swapped = find_swapped_elements(arr)
    
    if first_swapped is None or last_swapped is None:
        return arr  # Array is already sorted
    
    # Swap the two elements
    arr[first_swapped], arr[last_swapped] = arr[last_swapped], arr[first_swapped]
    
    return arr

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element {}: ".format(i + 1))))

print("Original array:", arr)

# Sorting the array
sorted_arr = sort_array_linear(arr)
print("Sorted array:", sorted_arr)
