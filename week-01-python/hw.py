####### 과제 3 - 가위 바위 보 게임

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
