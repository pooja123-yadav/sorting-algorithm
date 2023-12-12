# Selection sort

# Select minimum and swap

# Python program for implementation of Selection Sort

# Function to do Selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
array_to_sort = [49, 25, 19, 27, 87, 67, 22, 90, 47, 91]
result = selection_sort(array_to_sort)
print(result)


