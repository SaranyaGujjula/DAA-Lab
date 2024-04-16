def maximize_sum(arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize sum
    max_sum = 0

    # Compute the sum of products
    for i in range(len(arr)):
        max_sum += arr[i] * i

    return max_sum

# Example usage
arr = []

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

result = maximize_sum(arr)
print(f"Maximum sum of products is: {result}")
