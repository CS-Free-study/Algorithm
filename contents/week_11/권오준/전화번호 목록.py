# Level 2

def solution(phone_book):
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""

        for number in phone_number:
            temp += number
            
            if temp in hash_map and temp != phone_number:
                return False

    return True

# 다른 풀이

# def solution(phone_book):
#     phone_book = sorted(phone_book)
    
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         if p2.startswith(p1):
#             return False
    
#     return True