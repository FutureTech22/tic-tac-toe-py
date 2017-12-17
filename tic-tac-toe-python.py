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
	if (board[1] == "X" and board[2] == "X" and board[3] == "X") or\
	 	(board[4] == "X" and board[5] == "X" and board[6] == "X") or\
		(board[7] == "X" and board[8] == "X" and board[9] == "X") or\
		(board[1] == "X" and board[4] == "X" and board[7] == "X") or\
		(board[2] == "X" and board[5] == "X" and board[8] == "X") or\
		(board[3] == "X" and board[6] == "X" and board[9] == "X") or\
		(board[1] == "X" and board[5] == "X" and board[9] == "X") or\
		(board[3] == "X" and board[5] == "X" and board[7] == "X"):
		os.system("clear")
		print_header()
		print_board()
		print "X Wins! Congratulations"
		break

	#check for a tie (if board is full)
	isFull = True
	if " " in board:
		isFull = False

	#If the board is full, do something
	if isFull == True:
		print "Tie!"
		break	



#	for index in range(1, 10):
#		if board[index] == " ":
#			isFull = False
#			break

	os.system("clear")
	print_header()
	print_board()

	#get player O input
	choice = raw_input("Please choose an empty space for O:")
	choice = int(choice)

	#choice to see if the space is empty first
	if board[choice] == " ":
		board[choice] = "O"
	else:
		print "Sorry, that space is taken!"
		time.sleep(1)

	#check for O win
	if (board[1] == "O" and board[2] == "O" and board[3] == "O") or\
	 	(board[4] == "O" and board[5] == "O" and board[6] == "O") or\
		(board[7] == "O" and board[8] == "O" and board[9] == "O") or\
		(board[1] == "O" and board[4] == "O" and board[7] == "O") or\
		(board[2] == "O" and board[5] == "O" and board[8] == "O") or\
		(board[3] == "O" and board[6] == "O" and board[9] == "O") or\
		(board[1] == "O" and board[5] == "O" and board[9] == "O") or\
		(board[3] == "O" and board[5] == "O" and board[7] == "O"):
		os.system("clear")
		print_header()
		print_board()
		print "O Wins! Congratulations"
		break
