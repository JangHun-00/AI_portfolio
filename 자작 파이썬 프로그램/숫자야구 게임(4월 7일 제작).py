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
     016 >> 아웃!
     026 >> 볼 1개, 스트라이크 0개
     206 >> 볼 0개, 스트라이크 1개
     204 >> 볼 1개, 스트라이크 1개
     247 >> 스트라이크 3개(게임 종료)
     
==============================================================
""")
import random

strikecount = 0
ballcount = 0
outcount = 0


com = [str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))]

while com[0] == com[1] or com[1] == com[2] or com[2] == com[0]:
    com = [str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))]

comnum = str("".join(com))

#print(comnum)

playnum = ""

while outcount < 3:

    strikecount = 0
    ballcount = 0
    playnum = ""
    
    playnum = str(input("당신이 생각하는 '3자리' 숫자는? >> "))

    try:
        int(playnum)
    except:
        print('숫자만 입력하세요.')
        continue

    
    if len(playnum) != 3:
        print('3자리 숫자를 입력하세요.')
        continue

    
    play = list(playnum)

    if play[0] in com or play[1] in com or play[2] in com:
        
        if play[0] in com:
            ballcount += 1

        if play[1] in com:
            ballcount += 1

        if play[2] in com:
            ballcount += 1
        
        if play[0] == com[0] or play[1] == com[1] or play[2] == com[2]:
            if play[0] == com[0]:
                ballcount -= 1
                strikecount += 1

            if play[1] == com[1]:
                ballcount -= 1
                strikecount += 1

            if play[2] == com[2]:
                ballcount -= 1
                strikecount += 1

        print('볼 {}개, 스트라이크 {}개'.format(ballcount, strikecount))
            
        if strikecount == 3:
            print('삼진! 정답을 맞추셨습니다. 당신의 승리입니다!')
            break
    
    else:
        print("아웃! {}번째 아웃입니다!".format(outcount+1))
        outcount += 1



if outcount == 3:
    print("쓰리 아웃! 당신의 패배입니다.")

print('게임 종료!')
