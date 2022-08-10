import numpy as  np

def diagonalDifference(arr):
    n= len(arr)
    
    diagonal1 = 0
    for i in range(n):
        diagonal1 += arr[i][i]
        
    diagonal2 = 0
    for i in range(n):
        diagonal2 += arr[i][n - i - 1]
            
    return abs(diagonal1 - diagonal2)

def insertionSort1(n, arr):
    val = arr[n - 1]
    
    for i in range(n - 2, -1, -1):
        print(i, arr[i], val)
        if val < arr[i]:
            arr[i + 1] = arr[i]
            if i == 0:
                arr[i] = val

            st = ""
            for j in arr:
                st  += f"{j} "
            
            print(st)

        else:
            arr[i + 1] = val
        
            st = ""
            for j in arr:
                st  += f"{j} "
            
            print(st)

            break


def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] 
            j -= 1
        
        arr[j + 1] = key
        
        str = ""
        for k in arr:
            str += f"{k} "

        print(str)
    

def answerQuery(Q, arr):

    for q in Q:
        if q[0] == 1:
            arr[q[1]] = True 
        elif q[0] == 2:
            for i in range(q[1], len(arr)):
                if arr[i] == True:
                    return i
            return -1

        print(arr)

arr = [False, False, False, False]
Q = [[1, 2], [2, 1]]

idx = answerQuery(Q, arr)
print(idx)

# res = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
# print(res)

# insertionSort2(6, [1, 4, 3, 5, 6, 2])
