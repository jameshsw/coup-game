import colorama
from colorama import Fore, Back, Style
import random
colorama.init()

players = ['Player 1','Player 2']
cards = {'contessa': Fore.RED, 'duke': Fore.CYAN, 'captain': Fore.BLUE, 'ambassador': Fore.GREEN, 'assassin': Fore.BLACK}  
coins = Fore.LIGHTBLACK_EX

print("Dealing cards...")
for player in players:
  print(f"{player} was dealt:", end=" ")
  player_cards = random.sample(list(cards), 2)
  for card in player_cards:
    print(cards[card]+card+Style.RESET_ALL, end=" ")
  print()
  
print(f"The remaining cards were placed in the court {Fore.YELLOW}draw pile{Style.RESET_ALL}")   

print(f"Each player was given {coins}2{Style.RESET_ALL} coins")

current_player = random.choice(players)

while len(players) > 1:

  print(f"{current_player}'s turn:")  

  action = input("Choose an action: ")

  if action == "income":
    print(f"{current_player} chose to collect {coins}1{Style.RESET_ALL} coin from the Treasury")

  elif action == "foreign aid":
    print(f"{current_player} chose foreign aid")
    print(f"{players[1]} used the {cards['duke']}Duke{Style.RESET_ALL} to block it!")

  current_player = players[1] if current_player == players[0] else players[0]

print("Game over! ", current_player, " wins!")