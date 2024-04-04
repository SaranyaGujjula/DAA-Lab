def sum_of_two_num(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return arr[i], arr[j]
    return False

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
K = int(input("Enter the target sum: "))

pair = sum_of_two_num(arr, K)
if pair:
    print(f"Pair with sum {K}: {pair}")
else:
    print("No such pair found.")
