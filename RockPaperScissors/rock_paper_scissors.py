from random import randint

def play_turn(choice):
	if choice == 1:
		player = 'rock'
	elif choice == 2:
		player = 'paper'
	else:
		player = 'scissors'
	return player

def winner(player1, player2):
	player1_rock_wins = (player1['turn'] == 'rock' and player2['turn'] == 'scissors')
	player1_scissor_wins = (player1['turn'] == 'scissors' and player2['turn'] == 'paper')
	player1_paper_wins = (player1['turn'] == 'paper' and player2['turn'] == 'rock')
	player2_rock_wins = (player2['turn'] == 'rock' and player1['turn'] == 'scissors')
	player2_scissor_wins = (player2['turn'] == 'scissors' and player1['turn'] == 'paper')
	player2_paper_wins = (player2['turn'] == 'paper' and player1['turn'] == 'rock')
	draw = (player1['turn'] == player2['turn'])
	if player1_rock_wins:
		return player1['name'] + ' wins as rock blunts scissors'
	elif player1_scissor_wins:
		return player1['name'] + ' wins as scissors cut paper'
	elif player1_paper_wins:
		return player1['name'] + ' wins as paper covers rock'
	elif player2_rock_wins:
		return player2['name'] + ' wins as rock blunts scissors'
	elif player2_scissor_wins:
		return player2['name'] + ' wins as scissors cut paper'
	elif player2_paper_wins:
		return player2['name'] + ' wins as paper covers rock'
	else:
		return 'It is a draw'

if __name__ == "__main__":
	while True:
		choice = int(input('\nChoose either of the following options:\n1. Rock\n2. Paper\n3. Scissors\nMake your choice:'))
		user = {'name': 'User', 'turn': play_turn(choice)}
		print(user['name'] + " chose " + user['turn'])
		choice = randint(1, 3)
		computer = {'name': 'Computer', 'turn': play_turn(choice)}
		print(computer['name'] + " chose " + computer['turn'])
		print(winner(user, computer))
		answer = input("Do you wish to play again? (y/n)")
		if answer == 'n':
			break
		else:
			continue
	print("End of the game.")