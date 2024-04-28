def bubble_sort(arr):
    print("Original array:", arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array (Bubble Sort):", arr)

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

def selection_sort(arr):
    print("Original array:", arr)
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted array (Selection Sort):", arr)

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    sorted_arr = merge(left, right)
    
    return sorted_arr

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    

arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr.copy())
insertion_sort(arr.copy())
selection_sort(arr.copy())

print("Original array:", arr)
sorted_arr = merge_sort(arr.copy())
print("Sorted array (Merge Sort):", sorted_arr)

print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array (Quick Sort):", arr)
