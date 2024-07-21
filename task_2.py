def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return (iterations, arr[mid])

    return (iterations, arr[low] if low < len(arr) else arr[high])

# Example usage
arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
result = binary_search(arr, 0.75)
print(result)  # Output: (iterations, upper bound)
