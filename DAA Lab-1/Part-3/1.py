def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    for num in arr:
        target_pair = target_sum - num
        if target_pair in seen:
            pairs.append((num, target_pair))
        seen.add(num)
    return pairs

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
target_sum = int(input("Enter the target sum: "))

pairs = find_pairs_with_sum(arr, target_sum)
if pairs:
    print(f"Pairs with sum {target_sum}: {pairs}")
else:
    print("No pairs found with the given sum.")
