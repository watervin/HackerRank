#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here


    stack = []
    for i in range(len(s)):
        if len(stack) == 0 or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    return 'Empty String' if len(stack) == 0 else ''.join(stack)
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
