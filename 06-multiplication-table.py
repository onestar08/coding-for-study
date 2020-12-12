# 구구단

# x = 2
# y = 3
# print(x * y)

#
# a = 2
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while a < 20:
#     print(a)
#     a = a * b

# x = input(" 몇 단을 출력 하시겠습니까? ")
# for y in range(1,10):
#     print(int(x) * y)

# x = input(" 몇 단을 출력 하시겠습니까? ")
# y = 1
# while y < 10:
#     print(int(x) * y)
#     y = y + 1

# x = int(input(" 몇 단을 출력 하시겠습니까? "))
# for y in range(1,10):
#     print(x * y)

#정답지
x = int(input("몇 단을 출력 하시겠습니까?"))
for y in range(1, 10):
    print("{} * {} = {}".format(x, y, x * y))

# 추가 과제 : 구구단을 2에서 9단까지만 사용자가 입력할 수 있도록 제한

# 내가 짠 코드
x = int(input("몇 단을 출력 하시겠습니까?"))
if x > 9:
    print("2~9사이의 숫자를 입력해주세요")
elif x < 2 :
    print("2~9사이의 숫자를 입력해주세요")
# elif x == " ":
#     print("숫자를 입력해주세요.") # // 문자를 입력하면 안되게 하고 싶음
else :
    for y in range(1, 10):
        print("{} * {} = {}".format(x, y, x * y))


# 강의 정답지 - 역시나 더 간결함
x = int(input(" 몇 단을 출력하시겠습니까?"))
if x > 1 and x < 10:
    for y in range(1, 10):
        print("{} * {} = {}".format(x, y, x * y))
else :
    print("2에서 9사이의 숫자를 입력해주세요")
