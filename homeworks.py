######## 과제 1 - 맛집 고르기
# 취향 고르기 - 취향별 식당 리스트 작성하기 - 랜덤 초이스로 돌리기

# food = input("한식, 중식, 일식 중 한 가지를 고르세요")
# print(food + "을 고르셨네요.")
#

import random

kfood_list = ["이바돔", "할매보쌈", "김가네", "김밥천국"]
jfood_list = ["쿠우쿠우", "보물섬", "이자카야", "이라샤이"]
cfood_list = ["북회원", "강식당", "홍콩반점", "띵호야"]

user_choice = input("한식, 중식, 일식 중에서 골라주세요:")

if user_choice == "한식":
    choice_result = random.choice(kfood_list)
elif user_choice == "중식":
    choice_result = random.choice(cfood_list)
elif user_choice == "일식":
    choice_result = random.choice(jfood_list)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 합니다.")

if choice_result:
    print("{} 맛집으로 {}을/를 추천합니다".format(
    user_choice, choice_result)
    )


####### 과제 2 - 회사 조직도 만들기

class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

human1 = Human("한별", "32세", "남성" )
human2 = Human("주희", "31세", "여성" )
human3 = Human("유창", "30세", "남성" )
human4 = Human("희경", "32세", "여성" )
human5 = Human("성준", "42세", "남성" )

# print(human1.age)
# print(human5.sex)

class Workplace(Human):
    job = "대리"

human1 = Workplace("한별", "32세", "남성")
print(human1.job)
print(human1.age)
print(human3.job)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Colleague(Person):
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

colleague = Colleague("hanbyul", "20세", "Male", "대리")

# print(colleague.position)
print(colleague.__dict__)
#
# ####### 과제 3 - 가위 바위 보 게임
#
import random

Rock = "바위"
Scissors = '가위'
Paper = '보'
RSP_list = (Rock, Scissors, Paper)

win_score = 0
lose_score = 0

while win_score < 3 and lose_score < 3:
    Usr_choice = input("{}, {}, {}: ".format(
    Scissors, Rock, Paper
    ))
    Com_choice = random.choice(RSP_list)

    if Usr_choice == Com_choice:
        print("비겼습니다.")
    elif ((Usr_choice == Scissors and Com_choice == Rock)
            or (Usr_choice == Rock and Com_choice == Paper)
            or (Usr_choice == Paper and Com_choice == Scissors)):
        lose_score = lose_score + 1
        print("졌습니다.")
    else:
        win_score = win_score + 1
        print("이겼습니다.")

if win_score == 3:
    print("사용자가 최종 승리하였습니다.")
else:
    print("컴퓨터가 최종 승리하였습니다.")


######## 과제 4 - 다이아몬드 그리기

# 00100
# 01110
# 11111
# 01110
# 00100

for a in range(1,6):
    a = a - 3
    if a < 0:
        a = -a
    print(" " * a + "1" * (5 - a * 2) + " " * a)


########## 과제 5 - 에러 나지 않는 구구단

def gugudan():
    try:
        dan = int(input("몇 단을 출력하시겠습니까?"))
        if dan > 1 and dan < 10:
            for number in range(1, 10):
                print("{} * {} = {}".format(dan, number, dan * number))
        else:
            print("2에서 9사이의 숫자만 입력하셔야 합니다!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요")
        gugudan()
    except:
        print("알 수 없는 에러가 발생했습니다.")
        gugudan()

gugudan()
