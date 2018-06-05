# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re as regex

def solution(N):
    # write your code in Python 3.6
    
    N_binary = "{0:b}".format(N)
    
    gaps = regex.split("1+", N_binary)
    
    max_gap = []
    repetitions = len(gaps) - 1
    for i in range(0, repetitions):
    	max_gap.append(len(gaps[i]))
    
    return max(max_gap)
    
