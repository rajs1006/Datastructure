def selectionSort(arr):
    """
    Selection Sort uses 2 loops to sort the elments. It holds first lopp as contant
    and then traverse through second loop to find the minimum value and then swap
    it with the original value. This is not a stable sorting algorithm
    Time cmplexity = O(n^2) AS there are two nested loops:
                       1. One loop to select an element of Array one by one = O(N)
                       2. Another loop to compare that element with every other Array element = O(N
    Space complexity = O(1) only extra memory used is for temporary variable
                        while swapping two values in Array. The good thing about
                        selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation
    """
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp

        print(min_idx, arr)

    return arr


def stableSelectionSort(arr):
    """
    Stable selection sort is where 2 identical values maintain the same sequence.
    To achive that, we don't blindly swap tha values with min_idx but before swapping we
    shift all the values to maintain the sequence
    Time complexity : O(n2 + n) so, O(n2)
    Space complexity : O(1)
    """

    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        tmp = arr[min_idx]
        for k in range(min_idx, i, -1):
            arr[k] = arr[k - 1]

        arr[i] = tmp

    return arr


def recursiveSelSort(arr, low, high):

    min_idx = low
    for j in range(low + 1, high + 1):
        if arr[min_idx] > arr[j]:
            min_idx = j

    (arr[low], arr[min_idx]) = (arr[min_idx], arr[low])

    if low < high:
        recursiveSelSort(arr, low + 1, high)

    return arr


if __name__ == "__main__":
    arr = [4, 5, 3, 2, 4, 1]
    sortedArr = selectionSort(arr)

    print(sortedArr)
