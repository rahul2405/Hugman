# Visit pyGuru on youTube
# Tic Tac Toe Game

import random


def displayBoard(board):
	""" This will display board after updating the board """
	# print('\n'*25)
	print(board[1],'|',board[2],'|',board[3])
	print('-'*10)
	print(board[4],'|',board[5],'|',board[6])
	print('-'*10)
	print(board[7],'|',board[8],'|',board[9])

def playerInput():
	"""This function will take input for choosing the first player"""
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('player 1 : choose X or O : ')

	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')

# player1_marker,player2_marker = playerInput()

def place_marker(board,marker,position):
	"""This function will update the board position with
	   the given marker """

	board[position] = marker

def checkWin(board,mark):
	"""This function will check if someone has won the game """

	return ((board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[7] == board[4] == board[1] == mark) or
	(board[8] == board[5] == board[2] == mark) or
	(board[9] == board[6] == board[3] == mark) or 
	(board[1] == board[5] == board[9] == mark) or
	(board[3] == board[5] == board[7] == mark))

def chooseFirst():
	"""Randomly chooses who plays first"""

	flip = random.randint(0,2)

	if flip == 0:
		return 'player 1'
	else:
		return 'player2'

def checkSpace(board,position):
	"""This function will check whether there is a space available
	   on the board """

	return board[position] == ' '

def checkFull(board):
	"""This function will check whether the board is full or not """

	for i in range(1,10):
		if checkSpace(board,i):
			# There is a space at i position
			return False

def playerChoice(board,turn):
	"""This function will ask for user position """
	pos = 0
	while pos not in [1,2,3,4,5,6,7,8,9] or not checkSpace(board,pos):
		pos = int(input(f'\n{turn} Enter position [1-9] : '))

	return pos

def replay():
	"""Checks whether player wants to play again or not"""
	choice = ''
	choice == input("Want to play again or not Yes/No : ")

	if choice == 'Yes':
		return True
	else:
		return False

# ---------------------------------------------------------------------

print('\tWelcome to Tic Tac Toe')

while True:
	the_board = test_input = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	player1_marker,player2_marker = playerInput()
	turn = chooseFirst()
	print(turn,'will go first')

	play_game = input('Ready to play ? y or n : ')
	if play_game.lower() == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'player 1':
			# show the board
			displayBoard(the_board)
			# choose a position
			position = playerChoice(the_board,turn)
			# place the marker on the board
			place_marker(the_board,player1_marker,position)

			# Checking for Result

			if checkWin(the_board,player1_marker):
				displayBoard(the_board)
				print('Player 1 has won')
				game_on = False
			else:
				if checkFull(the_board):
					displayBoard(the_board)
					print('Game Draw')
					game_on = False
				else:
					turn = 'player 2'

		else:
			displayBoard(the_board)
			position = playerChoice(the_board,turn)
			place_marker(the_board,player2_marker,position)

			# Checking for Result

			if checkWin(the_board,player2_marker):
				displayBoard(the_board)
				print('Player 2 has won')
				game_on = False
			else:
				if checkFull(the_board):
					displayBoard(the_board)
					print('Game Draw')
					game_on = False
				else:
					turn = 'player 1'


	if not replay():
		break
