def binarySearch(arr, item):
    n, arr1 = len(arr), []
    if arr_not_sorted(arr):
        arr1 = insertionSort(arr)

    low, high = 0, len(arr1) - 1

    while low < high and arr1[(mid := (low + high) >> 1)]!= item:
        (low := mid + 1) if arr1[mid] < item else (high := mid - 1)
    
    return "The number is not in the array" if arr1[mid] != item else f"The number's index in original array = {[i for i in range(n) if arr[i] == item][0]}."

def arr_not_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return True
            
    print("The array is already sorted.")
    return False

def insertionSort(arr):
    arr1 = arr.copy()
    for i in range(1, len(arr1)):
        cur_value = arr1[i]
        if arr1[i] < arr1[i-1]:

            for j in range(i-1, -1, -1):
                if cur_value >= arr1[j]:
                    break
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
    
    print("The sorted array is ", arr1)
    return arr1

n = int(input("Enter the size of the array : "))
arr = [int(v) for v in input(f"Enter {n} numbers : ").split()][:n]

search = int(input("Enter the number whose index you want to search : "))
print(binarySearch(arr, search))