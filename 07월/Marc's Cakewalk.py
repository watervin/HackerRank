#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

import math
def marcsCakewalk(calorie,n):
    # Write your code here
    
    result = 0
    calorie = sorted(calorie,reverse = True)
    
    for i in range(n):
        result += ( calorie[i] * (2**i))
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie,n)

    fptr.write(str(result) + '\n')

    fptr.close()
