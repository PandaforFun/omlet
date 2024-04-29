def selection_sort(arr):
    print("Original array:", arr)
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted array (Selection Sort):", arr)

arr = [6,1,3,4,2,5]

selection_sort(arr)
