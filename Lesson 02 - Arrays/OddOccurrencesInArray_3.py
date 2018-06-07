# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    dictionary = {}
    
    for number in A:
    	if dictionary.get(number) == None:
    		dictionary[number] = 1
    	else:
    		dictionary[number] += 1
    
    for key in dictionary.keys():
    	if dictionary.get(key) % 2 == 1:
    		return key
