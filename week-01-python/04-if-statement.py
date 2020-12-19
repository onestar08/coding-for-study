# 참과 거짓 boolean
# if
# True, False
# and, or, not


a = True
b = False
# A가 참이고 그리고 B가 참이라면 (A와 B가 둘다 참이어야 된다)
print(a and b)
# A가 참이거나 혹은 B가 참이라면 (a나 B 둘 중에 하나라도 침이면 된다)
print(a or b)

# == & =
a = True
print(a == True)
print(a is True)


d = 7
if d > 10:
    print("숫자는 10보다 큽니다")
elif d > 5 and d <= 10 :
    print("숫자는 10보다 작거나 같고, 5보다는 큽니다.")
else :
    print("숫자는 5보다 작거나 같습니다")
