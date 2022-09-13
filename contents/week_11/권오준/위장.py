from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    ans = 1

    for cloth in clothes:
        d[cloth[1]].append(cloth[0])
    
    for v in d.values():
        ans *= len(v) + 1

    return ans - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))