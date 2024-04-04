def sum_of_two_num(arr, K):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return arr[left], arr[right]
        elif current_sum < K:
            left += 1
        else:
            right -= 1
    return False

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
K = int(input("Enter the target sum: "))

pair = sum_of_two_num(arr, K)
if pair:
    print(f"Pair with sum {K}: {pair}")
else:
    print("No such pair found.")
