# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    N_binary = "{0:b}".format(N)
    max_gap = 0
    current_gap = -1
    
    for i in range(1, len(N_binary)):
        if (N_binary[i-1] == '1' and N_binary[i] == '0'):
            current_gap = 1
        elif (N_binary[i - 1] == '0' and N_binary[i] == '0'):
            current_gap += 1
        elif (N_binary[i - 1] == '0' and N_binary[i] == '1'):
            max_gap = max(max_gap, current_gap)
        
    return max_gap
    
