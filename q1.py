def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    # Calculate the value/weight ratio and sort by this ratio in descending order
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)

    for i in index:
        if weight[i] <= capacity:
            # If the item can be fully included, take it fully
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            # If the item cannot be fully included, take the fraction that fits
            fractions[i] = capacity / weight[i]
            max_value += value[i] * fractions[i]
            break

    return max_value, fractions

# Example usage:
values = []
weights = []

# Taking user input for values and weights
n = int(input("Enter the number of items: "))
for i in range(n):
    value = int(input(f"Enter the value of item {i + 1}: "))
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("Enter the capacity of the knapsack: "))

max_value, fractions = fractional_knapsack(values, weights, capacity)
print("The maximum value of items that can be carried:", max_value)
print("Fractions in which the items are taken:", fractions)
