# Selection sort

# Select minimum and swap

# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
        # Move these lines outside the inner loop
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp         
	            


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

# This code is contributed by Mohit Kumra

