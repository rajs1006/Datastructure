"""
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.

Heap sort is an in-place algorithm. 
Its typical implementation is not stable, but can be made stable (See this)
Typically 2-3 times slower than well-implemented QuickSort.  The reason for slowness is a lack of locality of reference.

Efficiency –  
    The time required to perform Heap sort increases logarithmically while other 
    algorithms may grow exponentially slower as the number of items to sort increases. 
    This sorting algorithm is very efficient.
Memory Usage – 
    Memory usage is minimal because apart from what is necessary to hold the initial 
    list of items to be sorted, it needs no additional memory space to work
Simplicity –  
    It is simpler to understand than other equally efficient sorting algorithms because 
    it does not use advanced computer science concepts such as recursion
"""


def heapify(arr, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

    return arr


def heapSort(arr):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]

    # Function call
    sortedArr = heapSort(arr)

    print(sortedArr)
