def swap(arr, i, j):
    (arr[i], arr[j]) = (arr[j], arr[i])


def partition(arr, low, high):
    """
    This function takes last element as pivot, places the pivot element at
    its correct position in sorted array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right of pivot
    """
    
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    
    return i + 1


def quickSort(arr, low, high):
    """
    Time taken by QuickSort, in general, can be written as follows.

        T(n) = T(k) + T(n-k-1) + \theta              (n)

    The first two terms are for two recursive calls, the last term is for the partition process.
    k is the number of elements that are smaller than the pivot.
    The time taken by QuickSort depends upon the input array and partition strategy.
    Following are three cases.

    Worst Case:
        The worst case occurs when the partition process always picks the greatest or
        smallest element as the pivot. If we consider the above partition strategy where
        the last element is always picked as a pivot, the worst case would occur when
        the array is already sorted in increasing or decreasing order. Following is
        recurrence for the worst case.

        T(n) = T(0) + T(n-1) + \theta              (n)which is equivalent to  T(n) = T(n-1) + \theta              (n)

        The solution to the above recurrence is                   (n2).

    Best Case:
        The best case occurs when the partition process always picks the middle
        element as the pivot. The following is recurrence for the best case.

        T(n) = 2T(n/2) + \theta              (n)

        The solution for the above recurrence is                  (nLogn). It can be solved using case
        2 of Master Theorem.

    Average Case:
        To do average case analysis, we need to consider all possible permutation of array and
        calculate time taken by every permutation which doesn’t look easy.
        We can get an idea of average case by considering the case when partition puts O(n/9)
        elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.

        T(n) = T(n/9) + T(9n/10) + \theta              (n)

    The solution of above recurrence is also O(nLogn):

    Although the worst case time complexity of QuickSort is O(n2) which is more than many other
    sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice,
    because its inner loop can be efficiently implemented on most architectures, and in
    most real-world data. QuickSort can be implemented in different ways by changing
    the choice of pivot, so that the worst case rarely occurs for a given type of data.
    However, merge sort is generally considered better when data is huge and stored in
    external storage.
    """
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

        return arr


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6]
    sortedArr = partition(arr, 0, len(arr) - 1)

    print(sortedArr)
