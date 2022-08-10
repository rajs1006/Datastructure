
def linearSearch(arr, x):
    '''
    Linear serach traverse through all the elemnets atleast a once in worst case scneario
    and space coplexity is O(1) as at one time it is trying to search for one integer value
    '''
    for i, v in enumerate(arr):
        if v == x:
            return i

    return -1

def getSum(arr, x):
    
    if x % 2 == 0:
        return 0
    
    sum = 0
    for v in arr:
        sum += v
    return sum 

if __name__ == '__main__':

    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4, 5]

    # idx = linearSearch(arr, x)
    # print(f"value {x} is present at index {idx}")

    print(f"sum of all elements in the array is {getSum(arr1, 4)}")
    print(f"sum of all elements in the array is {getSum(arr2, 5)}")