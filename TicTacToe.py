print("Let's play Tic-Tac-Toe.")
a = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for i in range(3):
    for ii in range(3):
        a[i][ii] = " "
for i in range(3):
    print("|".join(a[i]))

print("Choose any number where you want to place.")
x = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for i in range(3):
    print("|".join(x[i]))
    
#player 1 is o and player 2 is x.
player1 = input("Player 1: ")
player2 = input("Player 2: ")

while True:
     p1_choice = input(f"{player1}'s turn. Where do you want to place? : ")
     for i in range(3):
         for ii in range(3):
             if p1_choice == x[i][ii]:
                 a[i][ii] = "o"
                 x[i][ii] = "o"
                 for i in range(3):
                     print("|".join(a[i]))

     if x[1][1] == x[0][0] == x[2][2]:
          print(f"{player1} is a winner!")
          break
     elif x[1][1] == x[2][0] == x[0][2]:
          print(f"{player1} is a winner!")
          break
     elif x[1][1] == x[0][1] == x[2][1]:
          print(f"{player1} is a winner!")
          break
     elif x[1][1] == x[1][0] == x[1][2]:
          print(f"{player1} is a winner!")
          break
     elif x[0][0] == x[0][1] == x[0][2]:
          print(f"{player1} is a winner!")
          break
     elif x[0][0] == x[1][0] == x[2][0]:
          print(f"{player1} is a winner!")
          break
     elif x[2][2] == x[2][0] == x[2][1]:
          print(f"{player1} is a winner!")
          break
     elif x[2][2] == x[1][2] == x[0][2]:
          print(f"{player1} is a winner!")
          break
     elif " " not in (a[0] and a[1] and a[2]):
          print("It is a draw!")
          break

     p2_choice = input(f"{player2}'s turn. Where do you want to place? : ")
     for i in range(3):
         for ii in range(3):
             if p2_choice == x[i][ii]:
                 a[i][ii] = "x"
                 x[i][ii] = "x"
                 for i in range(3):
                     print("|".join(a[i]))

     if x[1][1] == x[0][0] == x[2][2]:
          print(f"{player2} is a winner!")
          break
     elif x[1][1] == x[2][0] == x[0][2]:
          print(f"{player2} is a winner!")
          break
     elif x[1][1] == x[0][1] == x[2][1]:
          print(f"{player2} is a winner!")
          break
     elif x[1][1] == x[1][0] == x[1][2]:
          print(f"{player2} is a winner!")
          break
     elif x[0][0] == x[0][1] == x[0][2]:
          print(f"{player2} is a winner!")
          break
     elif x[0][0] == x[1][0] == x[2][0]:
          print(f"{player2} is a winner!")
          break
     elif x[2][2] == x[2][0] == x[2][1]:
          print(f"{player2} is a winner!")
          break
     elif x[2][2] == x[1][2] == x[0][2]:
          print(f"{player2} is a winner!")
          break
     elif " " not in (a[0] and a[1] and a[2]):
          print("It is a draw!")
          break
