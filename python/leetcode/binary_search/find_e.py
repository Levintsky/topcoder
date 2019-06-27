def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    # test normal
    ori_array = [1, 3, 5, 7, 9]
    array = []
    for i in ori_array:
        array = array + [i] * 5

    lookups = [item for item in range(min(array) - 1, max(array) + 2)]
    print(array)
    for item in lookups:
        id_ = binarySearch(array, 0, len(array) - 1, item)
        if id_ < 0 or id_ >= len(array):
            print(item, id_)
        else:
            print(item, id_, array[id_])
