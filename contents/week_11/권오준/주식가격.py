# Level 2

def solution(prices):    
    ans = [i for i in range (len(prices) - 1, -1, -1)]
    stack = [0]

    for i in range (1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans

p = [1, 2, 3, 4, 5, 6, 2, 3]
print(solution(p))