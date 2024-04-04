def segregate_zeros_and_ones(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
            
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = list(map(int, input("Enter the array elements separated by space (0s and 1s only): ").split()))

segregate_zeros_and_ones(arr)
print("Segregated Array:", arr)
