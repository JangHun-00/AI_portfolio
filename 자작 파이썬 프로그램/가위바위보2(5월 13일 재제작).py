import random

Win = '이겼습니다!'
Draw = '비겼습니다.'
Lose = '졌습니다...'

rock = '바위'
scissors = '가위'
paper = '보'

wintable = { scissors:paper, paper:rock, rock:scissors}
list1 = [rock, scissors, paper]

computer = random.choice(list1)

""""
number = random.randint(0, 2)

if number == 0:
    computer = "가위"
elif number == 1:
    computer = "바위"
else:
    computer = "보"
"""

def game(a, b):
    if a == b:
        return Draw
    elif wintable[a] == b:
        return Win
    else:
        return Lose

mine = None

while True:
    mine = None
    computer = random.choice(list1)
    
    while mine not in list1:
        mine = input("'가위', '바위', '보' 중 하나를 선택하세요! >> ")

    print("당신은 {}, 컴퓨터는 {}, 그러므로 당신은 {}".format(mine, computer, game(mine, computer)))
    print("")
