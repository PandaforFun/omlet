def insertion_sort(arr):
    print("Original array:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Sorted array (Insertion Sort):", arr)

arr = [6,1,3,4,2,5]

insertion_sort(arr)
