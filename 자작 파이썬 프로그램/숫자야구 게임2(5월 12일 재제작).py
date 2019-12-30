print("""
===============================================================
                  ** 숫자야구 게임(3자리) **

 컴퓨터가 생각하는 숫자를 맞추는 게임입니다! 플레이어가 제시한
 숫자 중에서 자릿수는 다르지만 똑같은 숫자가 있다면 볼(Ball),
 자릿수까지 똑같다면 스트라이크(strike)입니다. 한 번 컴퓨터가
 생각한 숫자를 맞춰보세요! 아웃(out)을 세 번 걸리면 게임 패배
 입니다.

 참고로 컴퓨터가 생각하는 숫자는 자릿수마다 중복되는 숫자 없이
 모두 다른 숫자입니다.(ex: 722같이 다른 자릿수에 겹치는 숫자
 는 컴퓨터가 생각하지 않음.)

 ex) 컴퓨터: 247
     016 >> (1~3)번째 아웃!
     026 >> Strike 0개, Ball 1개!
     206 >> Strike 1개, Ball 0개!
     204 >> Strike 1개, Ball 1개!
     247 >> Strike 3개, Ball 0개!(게임 승리)
     
==============================================================
""")
import random

out = 0

answer = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

while (answer[0] == answer[1]) or (answer[0] == answer[2]) or (answer[1] == answer[2]):
    answer = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

#print(answer)

while (out < 3):

    strike = 0
    ball = 0
    
    player = input("답이라고 생각하는 3자리 숫자를 입력하세요: ")

    try:
        test = int(player)
    except:
        print("숫자를 입력하세요!")
        continue

    if len(player) != 3:
        print("3자리 숫자만 입력하세요!")
        continue

    if answer.count(player[0]) == 1: ball += 1
    if answer.count(player[1]) == 1: ball += 1
    if answer.count(player[2]) == 1: ball += 1

    if answer[0] == player[0]:
        strike += 1
        ball -= 1
    if answer[1] == player[1]:
        strike += 1
        ball -= 1
    if answer[2] == player[2]:
        strike += 1
        ball -= 1

    print("Strike {}개, Ball {}개!".format(strike, ball))

    if strike == 3:
        print("정답은 {}였습니다! 게임 승리!".format(answer))
        break
    
    if strike == 0 and ball == 0:
        out += 1
        print("{}번째 아웃!!".format(out))

if out == 3:
    print("삼진 아웃! 게임 패배!")
