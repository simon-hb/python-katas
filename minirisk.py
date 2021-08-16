# MiniRisk is not the same as Risk and while it is played on
# a 3x3 board it is also not the same as TicTacToe. You will
# find many Python games on the web. While you are encouraged to do research, make sure you
# provide references to any web sites you borrow ideas from. You must follow the rules in the next
# section, do not invent your own rules, or follow a standard game design like TicTacToe.
# Special Rules for MiniRisk-S21
# MiniRisk-S21 is played on a 3x3 square grid.
# Winning the game: To win the game players try
# to gain control of 3 territories in a row,
# vertically, horizontally or diagonally.
# Winning a battle: Battles are won or lost
# through dice rolls and cash payments. The
# game uses standard 6 sided dice, 2 when
# attacking a territory, 3 when defending. When attacking a territory the player may
# also pay a fixed cost, between $0 and $9 which is added to their attack strength.
# If no money is spent on the attack the player earns $5. The attacker’s strength is
# the sum of 2 random dice rolls plus cash. It must be higher than the defender’s
# strength, which is the sum of 3 random dice rolls, in order to win a battle.
# Controlling a territory: To place your marker on a territory it must be your turn,
# and you must win a battle on an empty territory. If the territory is empty you must
# battle the other player for control. If the other player already controls a
# territory, you must first win a battle to remove them from the territory, and then
# fight a battle for control of the empty territory. When an attacker fails to win a
# battle, nothing changes on the board.
# Going first: The player who goes first starts the game with $14. The player who
# goes second only gets $8 but they also get control of the centre territory.
# Taking turns: Each battle consumes one turn for one player. The game continues
# until a player wins. The human player decides who goes first.


import random

print ("Programming Fundamentals 202120, <Your_Name>, <Your ID, ex: 0007771234>")
print ('Difficulty easy, hard?')
dif = input('e, h>') #this does not do anything yet, will fix if time later

print('Player who goes first gets some extra cash, but loses center position.')
print('Do you want to go first?')
first = input('Y/N >')

human_money=8
cpu_money=8
game_over=False
the_board = {'0': ' ', '1': ' ', '2': ' ',
            '3': ' ', '4': ' ', '5': ' ',
            '6': ' ', '7': ' ', '8': ' '}

if first[0].lower() == 'y':
  human_money+=6
  the_board['4'] = 'C'
  human_turn = True
else:
  cpu_money+=6
  the_board['4'] = 'H'
  human_turn = False

def print_board():
  print(f"""  {the_board['0']} | {the_board['1']} | {the_board['2']} 
  ---------       0 1 2
  {the_board['3']} | {the_board['4']} | {the_board['5']}   ->  3 4 5
  ---------       6 7 8
  {the_board['6']} | {the_board['7']} | {the_board['8']} """)

def print_money():
  print(f"Human = ${human_money} Computer = ${cpu_money}")

def print_game_state():
  print_money()
  print_board()

def attack(attack_cash, attack_territory, territory_status, human_turn):
  attack_roll_1 = random.randint(1,6)
  attack_roll_2 = random.randint(1,6)
  defence_roll_1 = random.randint(1,6)
  defence_roll_2 = random.randint(1,6)
  defence_roll_3 = random.randint(1,6)
  attack_total = attack_roll_1+attack_roll_2+attack_cash
  defence_total = defence_roll_1+defence_roll_2+defence_roll_3

  if human_turn == True:
    print(f"Computer scores: {defence_roll_1} + {defence_roll_2} + {defence_roll_3} = {defence_total}  Human scores: {attack_roll_1} + {attack_roll_2} + ${attack_cash} = {attack_total}")
    if attack_total < defence_total:
      print("Human Loses! Territory remains unchanged.")
    else:
      if territory_status == ' ':
        the_board[attack_territory] = 'H'
        print("Human Wins! Human gets the territory.")
      else:
        the_board[attack_territory] = ' '
        print("Human Wins! Computer occupation removed.")
    if attack_cash == 0:
      print("Human didn't use cash. Earning $5")
  else:
    print(f"Human scores: {defence_roll_1} + {defence_roll_2} + {defence_roll_3} = {defence_total}  Computer scores: {attack_roll_1} + {attack_roll_2} + ${attack_cash} = {attack_total}")
    if attack_total < defence_total:
      print("Computer Loses! Territory remains unchanged.")
    else:
      if territory_status == ' ':
        the_board[attack_territory] = 'C'
        print("Computer Wins! Computer gets the territory.")
      else:
        the_board[attack_territory] = ' '
        print("Computer Wins! Human occupation removed.")
    if attack_cash == 0:
      print("Computer didn't use cash. Earning $5")
  input("press return to continue...")

def check_game_over():
  if the_board['0'] == the_board['1'] == the_board['2'] == 'H' or the_board['3'] == the_board['4'] == the_board['5'] == 'H' or the_board['6'] == the_board['7'] == the_board['8'] == 'H' or the_board['0'] == the_board['3'] == the_board['6'] == 'H'or the_board['1'] == the_board['4'] == the_board['7'] == 'H' or the_board['2'] == the_board['5'] == the_board['8'] == 'H' or the_board['0'] == the_board['4'] == the_board['8'] == 'H' or the_board['6'] == the_board['4'] == the_board['2'] == 'H':
    return "human"
  elif the_board['0'] == the_board['1'] == the_board['2'] == 'C' or the_board['3'] == the_board['4'] == the_board['5'] == 'C' or the_board['6'] == the_board['7'] == the_board['8'] == 'C' or the_board['0'] == the_board['3'] == the_board['6'] == 'C'or the_board['1'] == the_board['4'] == the_board['7'] == 'C' or the_board['2'] == the_board['5'] == the_board['8'] == 'C' or the_board['0'] == the_board['4'] == the_board['8'] == 'C' or the_board['6'] == the_board['4'] == the_board['2'] == 'C':
    return "cpu"
    

while game_over == False:
  print_game_state()
  if human_turn == True:
    territory = input("What territory will you attack?>") #this could cause issues if wrong input, will fix if time remains
    cash = input("How much cash do you want to spend on the attack? ($0 - $9)>") #this could cause issues if wrong input, will fix if time remains
    human_money -= int(cash)
    if int(cash) == 0:
      human_money += 5
  else:
    input("Computer's turn is next, press return to continue ...")
    if the_board['4'] != 'C':
      territory = '4'
    else:
      territory = str(random.randint(0,8)) #this will cause issues if territory is occupied by C, will fix if time remains
    cash = random.randint(0,9) #this will cause issues if cpu_money < 9, will fix if time remains
    cpu_money -= int(cash)
    if int(cash) == 0:
      cpu_money += 5
    print(f"Computer selects territory [{territory}] paying ${cash} extra for attack")
  attack(int(cash), territory, the_board[territory], human_turn)
  human_turn = not human_turn
  if check_game_over() == "human" or check_game_over() == "cpu":
    game_over = True

print_game_state()
if check_game_over() == "human":
  print("Congrats you win!")
else:
  print("Computer wins, better luck next game!")

