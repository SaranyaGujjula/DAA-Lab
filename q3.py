def min_sum_of_products(array_one, array_two):
    # Sort array_one in ascending order
    array_one.sort()
    # Sort array_two in descending order
    array_two.sort(reverse=True)

    # Calculate the sum of products
    n = len(array_one)
    sum_of_products = sum(array_one[i] * array_two[i] for i in range(n))

    return sum_of_products

# Example usage
array_one = []
array_two = []

# Taking user input for array_one
n = int(input("Enter the number of elements in the first array: "))
print("Enter the elements of the first array:")
for i in range(n):
    element = int(input())
    array_one.append(element)

# Taking user input for array_two
n = int(input("Enter the number of elements in the second array: "))
print("Enter the elements of the second array:")
for i in range(n):
    element = int(input())
    array_two.append(element)

# Calculate minimum sum of products
min_sum = min_sum_of_products(array_one, array_two)
print("Minimum sum of products is:", min_sum)
