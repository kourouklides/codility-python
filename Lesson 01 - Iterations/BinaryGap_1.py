# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    i = N
    counter = 0
    result = 0
    found_one = False
    
    while (i > 0):
        if ( (i & 1) == 1):
            if (found_one == False):
                found_one = True
            else:
                result = max(result, counter)
            counter = 0
        else:
            counter += 1
        i >>= 1
        
    return result
