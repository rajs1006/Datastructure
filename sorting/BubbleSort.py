def bubbleSort(arr):
    """
    Bubble sort starts with very first two elements, comparing them to check which one is greater.
    Here, algorithm compares the first two elements, and swaps the values.
    Now, the array is already sorted, but our algorithm does not know if it is completed.
    The algorithm needs one whole pass without any swap to know it is sorted.

    Time Complexity= O(n^2) because of 2 loops.
    Auxiliary Space: O(1)
    """

    n = len(arr)

    while True:
        swap = False
        for i in range(n - 1):
            j = i + 1
            if arr[i] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                swap = True

        if not swap:
            return arr


def recursiveBubbleSort(arr, n):

    """
    Recursive Bubble Sort has no performance/implementation advantages, but can be a good question to check one’s understanding of Bubble Sort and recursion.
    If we take a closer look at Bubble Sort algorithm, we can notice that in first pass, we move largest element to end (Assuming sorting in increasing order). In second pass, we move second largest element to second last position and so on.
    Recursion Idea.
    """

    swap = False
    for i in range(n - 1):
        j = i + 1
        if arr[i] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            swap = True

    if swap and n != 0:
        recursiveBubbleSort(arr, n - 1)

    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sortedArr = recursiveBubbleSort(arr, len(arr))

    print(sortedArr)
