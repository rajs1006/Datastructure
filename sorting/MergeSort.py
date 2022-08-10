def mergeSort(arr):
    """
    Time Complexity: O(n log(n)),  Sorting arrays on different machines.
    Merge Sort is a recursive algorithm and time complexity can be expressed as
    following recurrence relation.

    T(n) = 2T(n/2) + θ(n)

    The above recurrence can be solved either using the Recurrence Tree method or the Master method.
    It falls in case II of Master Method and the solution of the recurrence is θ(nLogn).
    The time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as
    merge sort always divides the array into two halves and takes linear time to merge two halves.

    Auxiliary Space: O(n)
    Space Complexity :
            • In merge sort all elements are copied into an auxiliary array
            • so N auxiliary space is required for merge sort.
    """

    n = len(arr)

    if n > 1:
        mid = n // 2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        ## We start the counter and start merging
        # to merge we look in all the elements in left and right
        # and then based on order we start arranging them in the array.
        # however when we arrange an item in the array we do not swap it
        # we just replace the value at an index with the smallest value either from left or right
        # and so to the ither value in arr should be replaced with the other array of left or right
        # which value was not replaced.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sortedArr = mergeSort(arr)

    print(sortedArr)
