# Level 1

def solution(arr):
    stack = [arr[0]]
    
    for i in arr[1:]:
        if stack[-1] != i:
            stack.append(i)
    
    return stack