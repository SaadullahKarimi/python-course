# there are three things stone,paper,and scissor for playing game!
print("rok")
print("paper")
print("scisser")
# take input from user 
Player_1 = input("player_1 , make your move : " )
Player_2 = input("player_2 , make your move : " )
# if player1 brings stone and player2 brings scissors, player1 will win!
if Player_1 == "rock" and Player_2 == "scissors":
    print("player_1 wins!....")
# if player1 brings stone and player2 brings paper, player2 will win!
elif Player_1 == "rock" and Player_2 == "paper":
    print("player_2 wins!...")
# if player1 brings paper and player2 brings stone, player1 will win!
elif Player_1 == "paper" and Player_2 == "rock":
    print("player_1 wins!...")
    # if player1 brings paper and player2 brings scissrs, player2 will win!
elif Player_1 == "paper" and Player_2 == "scissors":
    print("player_2 wins!...")
    # if player1 brings scissor and player2 brings paper, player1 will win!
elif Player_1 == "scissors" and Player_2 == "paper":
    print("player_1 wins!...")
    # if player1 brings scissor and player2 brings stone, player1 will win!
elif Player_1 == "scissors" and Player_2 == "rock":
    print("player_2 wins!...")
# if the two players choose the same item, it will write both players are equal
elif Player_1 == Player_2:
    print("thats a tie ...")
# if use insert wrong spell it takes error!
else:
    print("something went wrong ....")
   