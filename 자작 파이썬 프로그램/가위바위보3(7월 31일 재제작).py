import random

wintable = {"가위":"보", "바위":"가위", "보":"바위"}
rsp = [x for x in wintable.keys()]
win, draw, lose, total = 0, 0, 0, 0

print("컴퓨터와 하는 가위바위보 게임!\n")

while True:
    player = input("가위, 바위, 보 중 하나를 선택하세요(종료: Q): ")

    if player.upper() == "Q":
        print("\n컴퓨터와 총 {}번의 경기 중, {}번 승리, {}번 무승부, {}번 패배했습니다! 또 이용해주세요~".format(total, win, draw, lose))
        break
    
    if player not in rsp:
        print("'가위', '바위', '보' 셋 중 하나만 입력하세요!\n")
        continue
        
    computer = random.choice(rsp)

    print("당신은 {}, 컴퓨터는 {}를 냈으므로 ".format(player, computer), end="")

    if player == computer:
        print("비겼습니다.")
        draw += 1
    elif wintable[player] == computer:
        print("이겼습니다!")
        win += 1
    else:
        print("졌습니다...")
        lose += 1
    total += 1

    print()
