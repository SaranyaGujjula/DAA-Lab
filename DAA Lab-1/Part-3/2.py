def max_pair(arr):
    if len(arr) < 2:
        return None

    arr.sort()
    return arr[-1], arr[-2]

arr = list(map(int, input("Enter the array elements separated by space: ").split()))

pair = max_pair(arr)
if pair:
    product = pair[0] * pair[1]
    print(f"Pair with maximum product: {pair}, Product: {product}")
else:
    print("Array is too small to find a pair with maximum product.")
