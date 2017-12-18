#tic-tac-toe

#stage 1:
#create the main loop
#print the board
#create your loop
#get the user input
#put the user input in the board


#stage2:
#check for player win

#stage3:
#create the second player
#check for second player win
#check for a full board

#stage4:
#combine stages 2 & 3 into 1 function
#def is winner(board, player):
#create a function to check if the board is full
#def is_board_full(board)

#stage5
#creating our game AI
#def get_computer_move(board,player):
#return random number
#make sure random number is an empty space

#import
import os
import time
import random

#define the board
board = [""," "," "," "," "," "," "," "," "," ",]

#print the header
def print_header():
	print "TIC TAC TOE 3 IN A ROW"

#define the print board function
def print_board():
	print "   |   | "
	print " "+board[1]+" | "+board[2]+" | "+board[3]+" "
	print "   |   |   "
	print "---|---|---"
	print "   |   |   "
	print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
	print "   |   |   "
	print "---|---|---"
	print "   |   |   "
	print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
	print "   |   |   "

#check for winner
def is_winner(board, player):
	if (board[1] == player and board[2] == player and board[3] == player) or\
	 	(board[4] == player and board[5] == player and board[6] == player) or\
		(board[7] == player and board[8] == player and board[9] == player) or\
		(board[1] == player and board[4] == player and board[7] == player) or\
		(board[2] == player and board[5] == player and board[8] == player) or\
		(board[3] == player and board[6] == player and board[9] == player) or\
		(board[1] == player and board[5] == player and board[9] == player) or\
		(board[3] == player and board[5] == player and board[7] == player):
		return True
	else:
		return False

#check for a tie
def is_full(board):
	if " " in board:
		return False
	else:
		return True

def get_computer_move(board,player):

	if board[1] == player and board[4] == player and board[7] == " ":
		return 7
	if board[4] == player and board[7] == player and board[1] == " ":
		return 1
	if board[1] == player and board[7] == player and board[4] == " ":
		return 4
	if board[2] == player and board[5] == player and board[8] == " ":
		return 8
	if board[5] == player and board[8] == player and board[2] == " ":
		return 2
	if board[2] == player and board[8] == player and board[5] == " ":
		return 5
	if board[3] == player and board[6] == player and board[9] == " ":
		return 9
	if board[6] == player and board[9] == player and board[3] == " ":
		return 3
	if board[3] == player and board[9] == player and board[6] == " ":
		return 6
	#if the center square is empty choose that
	if board[5] == " ":
		return 5
	while True:
		move = random.randint(1,9)
		#if space is empty go ahead and return, otherwise try again
		if board[move] == " ":
			return move
			break


while True:
	os.system("clear")
	print_header()
	print_board()

	#get player X input
	choice = raw_input("Please choose an empty space for X:")
	choice = int(choice)

	#choice to see if the space is empty first
	if board[choice] == " ":
		board[choice] = "X"
	else:
		print "Sorry, that space is taken!"
		time.sleep(1)

	#check for X win
	if is_winner(board, "X"):
		os.system("clear")
		print_header()
		print_board()
		print "X Wins! Congratulations"
		break

	#If the board is full, do something
	if is_full(board) == True:
		print "Tie!"
		break	

	os.system("clear")
	print_header()
	print_board()

	#get player O input
	choice = get_computer_move(board, "O")

	#choice to see if the space is empty first
	if board[choice] == " ":
		board[choice] = "O"
	else:
		print "Sorry, that space is taken!"
		time.sleep(1)

	#check for O win
	if is_winner(board, "O"):
		os.system("clear")
		print_header()
		print_board()
		print "O Wins! Congratulations"
		break
