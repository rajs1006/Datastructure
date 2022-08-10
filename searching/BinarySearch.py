def recursiveBinarySearch(val, arr, start, end):
    """
    Time Complexity: O(log n)
    Auxiliary Space: O(log n)
    """
    mid = (start + end) // 2
    ## right >=1 makes sure that the array is atleast of size 1.
    if end >= 1:
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            return recursiveBinarySearch(val, arr, start, mid - 1)
        elif val > arr[mid]:
            return recursiveBinarySearch(val, arr, mid + 1, end)
    else:
        raise Exception("value not found")

    return mid


def binarySearch(val, arr, start, end):
    while start < end:
        mid = (start + end) // 2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == "__main__":
    arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]

    # Function call
    val = 10
    idx = binarySearch(val, arr, 0, len(arr))
    assert arr[idx] == val, f"arr[{idx}] should be {val}"
    print(f"{val} present at index {idx} in array : arr[{idx}] == {arr[idx]}")
