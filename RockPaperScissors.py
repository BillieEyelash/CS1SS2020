# determine the winner of a round
def determine_winner(player1, player2):
  if player1 == player2:
    result = "tie"
  elif player1 == 'rock' and player2 == 'scissors':
    result = 'player1'
  elif player2 == 'paper' and player1 == 'scissors':
    result = 'player1'
  elif player2 == 'rock' and player1 == 'paper':
    result = 'player1'
  else:
    result = "player2"

  return result

# get a random play from the computer
def get_computer_play():
  from random import choice
  computer_play = choice(["rock", "paper", "scissors"])
  return computer_play

# get player1 input and play 1 game
def play_a_single_game():
  player1 = input('Rock, paper, or scissors? ')
  player2 = get_computer_play()
  winner = determine_winner(player1, player2)
  print(player1, player2, "winner = ", winner)
  return determine_winner(player1, player2)

# ask the user how many games they want to play and keep score
def run():
    numberofgames = int(input('Enter the number of games you want to play: '))
    scores = {'player1': 0, 'player2': 0, 'tie': 0}
    for i in range(numberofgames):
        winner = play_a_single_game()
        scores[winner] += 1

    # print scores and the number of ties
    print('Player1 won', scores['player1'], 'time(s).')
    print('Player2 won', scores['player2'], 'time(s).')
    print('There was', scores['tie'], 'tie(s).')

def test_determine_winner():
    print(determine_winner('rock', 'paper') == 'player2')
    print(determine_winner('paper', 'paper') == 'tie')
    print(determine_winner('rock', 'scissors') == 'player1')

# test_determine_winner()
run()
