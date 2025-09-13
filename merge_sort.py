def merge_both_left_and_right_sorted_subarray(arr, left, mid, right):
    left_subarray_size, right_subarray_size = (mid - left + 1), (right - mid)

    left_subarray  = [None] * left_subarray_size
    right_subarray = [None] * right_subarray_size

    for l in range(left_subarray_size):
        left_subarray[l] = arr[left + l]

    for r in range(right_subarray_size):
        right_subarray[r] = arr[mid + 1 + r]
    
    l, r, i = 0, 0, left

    while l < left_subarray_size and r < right_subarray_size:
        if left_subarray[l] <= right_subarray[r]:
            arr[i] = left_subarray[l]
            l += 1
        else:
            arr[i] = right_subarray[r]
            r += 1
        i += 1
    
    if l < left_subarray_size:
        while l < left_subarray_size:
            arr[i] = left_subarray[l]
            l += 1
            i += 1
    elif r < right_subarray_size:
        while r < right_subarray_size:
            arr[i] = right_subarray[r]
            r += 1
            i += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) >> 1
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge_both_left_and_right_sorted_subarray(arr, left, mid, right)


def main():
    n = int(input("Enter the size of the array : "))

    arr = [int(v) for v in input(f"Enter {n} numbers : ").split(' ')] [:n]
    # print(arr, len(arr), type(arr[0]))

    mergeSort(arr, 0, n - 1)

    print("The sorted array is :", arr)

if __name__ == "__main__":
    main()