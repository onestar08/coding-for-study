# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hello, {}".format(name))

name1 = "hanbyul"
name2 = "juhee"
name3 = "jiyoon"
name4 = 'onestar'
name5 = "hanbyul"
name6 = "juhee"
name7 = "jiyoon"
name8 = 'onestar'

# print("hi, {}".format(name1))
# print("hi, {}".format(name2))
# print("hi, {}".format(name3))
# print("hi, {}".format(name4))
# print("hi, {}".format(name5))
# print("hi, {}".format(name6))
# print("hi, {}".format(name7))
# print("hi, {}".format(name8))

wow = hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 입력값 o, 반환값 o
def sum(a, b):
    return a + b

# 입력값 o, 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))

# 입력값 x, 반환값 o
def return_1():
    return 1

# 입력값 x, 반환값 x
def hello_world():
    print("hello_world")

num_1 = return_1()
print(num_1)
print(wow)
