from collections import deque

def solution(bridge_length, weight, truck_weights):
    q, across = deque(truck_weights), deque()
    time = total = 0
    
    while q or across:
        time += 1
        if across:
            if time - across[0][1] == bridge_length:
                total -= across.popleft()[0]
        if q:
            truck = q.popleft()
            total += truck
            if len(across) < bridge_length and total <= weight:
                across.append((truck, time))
            else:
                q.appendleft(truck)
                total -= truck
    
    return time
    
b = 2
w = 10
t = [7, 4, 5, 6]
print(solution(b, w, t))