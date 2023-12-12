# The insertionSort function takes an array arr as input. It first calculates the length of the array (n).
# If the length is 0 or 1, the function returns immediately as an array with 0 or 1 element is considered already sorted.

# For arrays with more than one element, the function proceeds to iterate over the array starting from the second element.
# It takes the current element (referred to as the “key”) and compares it with the elements in the sorted portion of the array that 
# precede it. If the key is smaller than an element in the sorted portion, the function shifts that element to the right,
# creating space for the key. This process continues until the correct position for the key is found, and it is then inserted in 
# that position.

def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1,n - 1):
        j = i
        while(j>0 and (arr[j-1] > arr[j])):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1

    return arr

# Example usage
array_to_sort = [49, 25, 19, 27, 87, 67, 22, 90, 47, 91]
result = insertion_sort(array_to_sort)
print(result)
