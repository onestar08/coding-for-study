# 미니과제 1. 랜덤 뽑기

# 구글링 능력
# 리스트나 튜플에서 임의로 하나의 값을 뽑으려면?
# [1, 2, 3, 4, 5]

import random
num_list = [1, 2, 3, 4, 5]
print(random.choice(num_list))

import secrets
fruit_list = ['apple', 'banana', 'melon', 'orange']
print(secrets.choice(fruit_list))

abc = ['a', 'b', 'c', 'd', 'e', 'f']
random.shuffle(abc)
print(abc)

x = random.randint(1, 5) # 1 <= x <= 5
print(x)
