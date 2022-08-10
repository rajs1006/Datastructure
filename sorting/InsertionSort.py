def insertionSort(arr):
    """
    Basically, Insertion sort is efficient for small data values
    Insertion sort is adaptive in nature, i.e. it is appropriate for
    data sets which are already partially sorted.

    Time Complexity: O(n^2)
    Auxiliary Space: O(1)
    """

    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def recursionInsertionSort(arr, n):
    """
    Recursive Insertion Sort has no performance/implementation advantages,
    but can be a good question to check one’s understanding of Insertion Sort and recursion.
    If we take a closer look at Insertion Sort algorithm, we keep processed elements sorted
    and insert new elements one by one in the sorted array.
    """

    if n > 1:
        recursionInsertionSort(arr, n - 1)
        last = arr[n - 1]
        j = n - 2
        while j >= 0 and arr[j] > last:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = last

    return arr


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6]
    sortedArr = recursionInsertionSort(arr, len(arr))

    print(sortedArr)
