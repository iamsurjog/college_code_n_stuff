###############
##  numpy needs to be installed 
##  output takes time to generate as it is parsing through 16 million posibilities (may or may not be a reference to doctor strange)
###############

import numpy as np
n = 8



def placequeen(i, j, arr):
    diag_vals = []
    # for the forward slash diagonals, the sum of the i+j is same
    for k in range(n):
        for l in range(n):
            if k + l == i + j:
                diag_vals.append((k, l))
    # for back slash diagonals, subtraction works, but only j-i and mod won't work as it takes 2 diagonals
    for k in range(n):
        for l in range(n):
            if l - k == j - i:
                diag_vals.append((k, l))
    # for the rows and columns
    for o in range(n):
        arr[i, o] = 1
        arr[o, j] = 1

    for var in diag_vals:
        arr[var] = 1

    arr[i, j] = 2
    return arr

# uses octal system to place queens
for i in range(0, 16777215):
    array = np.zeros((n, n))
    string = oct(i)[2:]
    while len(string) < 8:
        string = string[::-1]
        string = string + "0"
        string = string[::-1]
    lis = list(string)
    for i in range(len(lis)):
        lis[i] = int(lis[i])
    # print(lis)
    for i in range(len(lis)):
        placequeen(lis[i], i, array)
    for i in array:
        j = list(i).count(2)
        if j != 1:
            break
    else:
        print(array)

