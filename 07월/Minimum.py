#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
import math
def minimumAbsoluteDifference(arr,n):
    # Write your code here

    arr = sorted(arr)
    result = 10**20
    
    for i in  range(n-1):
        if arr[i+1] - arr[i] < result:
            result = arr[i+1] - arr[i]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
