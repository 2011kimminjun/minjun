print()



import random

칸_수 = 30
player1 = 1
player2 = 1
def board():
    print("*" * (player1 - 1) + "1" + "*" * ((칸_수) - player1) + "도착")
    print("*" * (player2 - 1) + "2" + "*" * ((칸_수) - player2) + "도착")

print("주사위 게임 시작!")
board()
while True:
    input("엔터를 누르면 말이 움직입니다")
    player1 = player1 + random.randint(1, 6)
    player2 = player2 + random.randint(1, 6)
    if player1 > 30:
        player1 = 30
    elif player2 > 30:
        player2 = 30
    
    if player1 >= 30 or player2 >= 30:
        if player1 > player2:
            print("player1 승리!")
            break
        elif player1 < player2:
            print("player2 승리!")
            break
        else:
            print("무승부")
            break
    board()



print()