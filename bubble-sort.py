# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
# This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# In Bubble Sort algorithm:

# 1. traverse from left and compare adjacent elements and the higher one is placed at right side. 
# 2. In this way, the largest element is moved to the rightmost end at first. 
# 3. This process is then continued to find the second largest and place it and so on until the data is sorted.

# Total no. of passes: n-1
# Total no. of comparisons: n*(n-1)/2 (n,n-1,n-2,n-3..................1 = n*(n-1)/2)

# Note:  It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap. 


def bubbleSort(arr):
    n = len(arr)
     
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
arr = [49, 25, 19, 27, 87, 67, 22, 90, 47, 91]
bubbleSort(arr)
print(arr)
