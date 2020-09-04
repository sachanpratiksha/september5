def print_horiz_line(board_size):
    print(" --- " * board_size)

def print_vert_line(board_size):
    print("|   " * (board_size + 1))

def enterchice(game,userinpur):
    x_input=input("Player X turn,enter your input ")
    p=x_input[0]
    q=x_input[1]
    game[p][q]= userinpur


def line_match(game):
	for i in range(3):
		set_r = set(game[i])
		if len(set_r) == 1 and game[i][0] != 0:
			return game[i][0]
	return 0
#transposed column function for future use
#def column(game):
#	trans = numpy.transpose(game)
#	for i in range(3):
#		set_r = set(trans[i])
#		if len(set_r) == 1 and trans[i][0] != 0:
#			return list(set_r)[0]

def diagonal_match(game):
	if game[1][1] != 0:
		if game[1][1] == game[0][0] == game[2][2]:
			return game[1][1]
		elif game[1][1] == game[0][2] == game[2][0]:
			return game[1][1]
	return 0

if __name__ == "__main__":
    board_size = int(input("What size of game board? "))
    for index in range(board_size):
        print_horiz_line(board_size)
        print_vert_line(board_size)


    print_horiz_line(board_size)