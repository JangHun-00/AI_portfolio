print("""
==============================
        ** 369 게임 **

 숫자를 차례대로 입력하면서
 숫자에 3, 6, 9가 들어가면
 들어간 갯수 만큼 '짝'을 쓰면
 되는 게임! 재밌게 해봐요~

 ex) 2번째 >> 2
     3번째 >> 짝
     59번째 >> 짝
     323번째 >> 짝짝
     396번째 >> 짝짝짝
     128745번째 >> 128745
     
==============================
""")

list = []
players = int(input('플레이어의 수를 정해주세요. 숫자만 입력하세요! >> '))

for player in range(1, players+1):
    list.append('{}P'.format(player))


def game():
    for i in range(0, 9999999):
        if i >= len(list):
            n = (i + len(list)) % len(list)
        elif i < len(list):
            n = i

        num = input('{} 차례! >> '.format(list[int(n)]))
        
        if i == 9999999:
            print('어떻게 천 만번째까지 이 게임을 안 끝낼 수 있죠...? 여러분 모두의 승리입니다!')
        
        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 0:
            if num == str(i+1):
                pass
            else:
                return '숫자를 틀렸습니다! {}의 패배!'.format(list[int(i)])
                
        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 1:
            if num == "짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 하나 있는데... 짝을 한 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 2:
            if num == "짝짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 두 개 있는데... 짝을 두 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 3:
            if num == "짝짝짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 세 개 있는데... 짝을 세 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 4:
            if num == "짝짝짝짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 네 개 있는데... 짝을 네 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 5:
            if num == "짝짝짝짝짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 다섯 개 있는데... 짝을 다섯 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 6:
            if num == "짝짝짝짝짝짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 여섯 개 있는데... 짝을 여섯 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        elif str(i+1).count("3") + str(i+1).count("6") + str(i+1).count("9") == 7:
            if num == "짝짝짝짝짝짝짝":
                pass
            else:
                return '3, 6, 9가 숫자 안에 일곱 개 있는데... 짝을 일곱 번 쳐야죠! {}의 패배!'.format(list[int(n)])

        else:
            print('오류가 발생했습니다.')

print(game())
                                    
