def bubble_sort(arr):
    print("Original array:", arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array (Bubble Sort):", arr)

arr = [6,1,3,4,2,5]

bubble_sort(arr)
