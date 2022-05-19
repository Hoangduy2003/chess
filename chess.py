import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))

SQUARE_SIZE = 80
GREEN = (0,150,0)
WHITE = (255,255,255)
BROWN = (80,42,42)
YELLOW = (255,255,0)
BLACK = (0,0,0)
RED = (255,0,0)

X_POSITION = 30
Y_POSITION = 30

CHESS_SIZE = 80

chess_board = [['BR','BP','  ','  ','  ','  ','WP','WR'],
			   ['BN','BP','  ','  ','  ','  ','WP','WN'],
			   ['BB','BP','  ','  ','  ','  ','WP','WB'],
			   ['BQ','BP','  ','  ','  ','  ','WP','WQ'],
			   ['BK','BP','  ','  ','  ','  ','WP','WK'],
			   ['BB','BP','  ','  ','  ','  ','WP','WB'],
			   ['BN','BP','  ','  ','  ','  ','WP','WN'],
			   ['BR','BP','  ','  ','  ','  ','WP','WR']]

font = pygame.font.SysFont('sans',20)
big_font = pygame.font.SysFont('sans',40)
white_pawn_image = pygame.image.load("white_pawn.png")
black_pawn_image = pygame.image.load("black_pawn.png")
white_rock_image = pygame.image.load("white_rock.png")
black_rock_image = pygame.image.load("black_rock.png")
white_knight_image = pygame.image.load("white_knight.png")
black_knight_image = pygame.image.load("black_knight.png")
white_bishop_image = pygame.image.load("white_bishop.png")
black_bishop_image = pygame.image.load("black_bishop.png")
white_queen_image = pygame.image.load("white_queen.png")
black_queen_image = pygame.image.load("black_queen.png")
white_king_image = pygame.image.load("white_king.png")
black_king_image = pygame.image.load("black_king.png")

white_pawn_image = pygame.transform.scale(white_pawn_image,(CHESS_SIZE,CHESS_SIZE))
black_pawn_image = pygame.transform.scale(black_pawn_image,(CHESS_SIZE,CHESS_SIZE))
white_rock_image = pygame.transform.scale(white_rock_image,(CHESS_SIZE,CHESS_SIZE))
black_rock_image = pygame.transform.scale(black_rock_image,(CHESS_SIZE,CHESS_SIZE))
white_knight_image = pygame.transform.scale(white_knight_image,(CHESS_SIZE,CHESS_SIZE))
black_knight_image = pygame.transform.scale(black_knight_image,(CHESS_SIZE,CHESS_SIZE))
white_bishop_image = pygame.transform.scale(white_bishop_image,(CHESS_SIZE,CHESS_SIZE))
black_bishop_image = pygame.transform.scale(black_bishop_image,(CHESS_SIZE,CHESS_SIZE))
white_queen_image = pygame.transform.scale(white_queen_image,(CHESS_SIZE,CHESS_SIZE))
black_queen_image = pygame.transform.scale(black_queen_image,(CHESS_SIZE,CHESS_SIZE))
white_king_image = pygame.transform.scale(white_king_image,(CHESS_SIZE,CHESS_SIZE))
black_king_image = pygame.transform.scale(black_king_image,(CHESS_SIZE,CHESS_SIZE))

running = True
hold_chess = False
get_x = 0
get_y = 0
index_x = 0
index_y = 0
start_x = 0
start_y = 0 
white_turn = True
black_turn = False
end_turn = False
white_promotion = False
black_promotion = False
white_king_x = 4
white_king_y = 7
black_king_x = 4
black_king_y = 0
white_king_moving = False
black_king_moving = False
white_rock1_moving = False
black_rock1_moving = False
white_rock2_moving = False
black_rock2_moving = False
white_pawn_2_grid_move_x = -1
white_pawn_2_grid_move_y = -1
black_pawn_2_grid_move_x = -1
black_pawn_2_grid_move_y = -1
white_pawn_2_grid = False
black_pawn_2_grid = False
white_pawn_special_move = False
black_pawn_special_move = False
repeated_moves = []

clock = pygame.time.Clock()




def white_pawn_control(pawn_x, pawn_y, index_x, index_y):
	if abs(index_x - pawn_x) == 1 and pawn_y == index_y + 1:
		return True



def black_pawn_control(pawn_x, pawn_y, index_x, index_y):
	if abs(index_x - pawn_x) == 1 and pawn_y == index_y - 1:
		return True



def knight_control(knight_x, knight_y, index_x, index_y):
	if (abs(index_x - knight_x) == 2 and abs(index_y - knight_y) == 1) or (abs(index_x - knight_x) == 1 and abs(index_y - knight_y) == 2):
		return True



def rock_control(rock_x, rock_y, index_x, index_y):
	if index_x == rock_x:
		if rock_y < index_y:
			check = rock_y + 1
			while chess_board[index_x][check] == '  ' and check < index_y:
				check += 1
			if check == index_y:
				return True

		if rock_y > index_y:
			check = rock_y - 1
			while chess_board[index_x][check] == '  ' and check > index_y:
				check -= 1
			if check == index_y:
				return True

	if index_y == rock_y:
		if rock_x < index_x:
			check = rock_x + 1
			while chess_board[check][index_y] == '  ' and check < index_x:
				check += 1
			if check == index_x:
				return True

		if rock_x > index_x:
			check = rock_x - 1
			while chess_board[check][index_y] == '  ' and check > index_x:
				check -= 1
			if check == index_x:
				return True



def bishop_control(bishop_x, bishop_y, index_x, index_y):
	if abs(index_x - bishop_x) == abs(index_y - bishop_y):
		if bishop_x < index_x:
			check_x = bishop_x + 1

			if bishop_y < index_y:
				check_y = bishop_y + 1
				while chess_board[check_x][check_y] == '  ' and check_x < index_x:
					check_x += 1
					check_y += 1
				if check_x == index_x:
					return True

			if bishop_y > index_y:
				check_y = bishop_y - 1
				while chess_board[check_x][check_y] == '  ' and check_x < index_x:
					check_x += 1
					check_y -= 1
				if check_x == index_x:
					return True

		if bishop_x > index_x:
			check_x = bishop_x - 1

			if bishop_y < index_y:
				check_y = bishop_y + 1
				while chess_board[check_x][check_y] == '  ' and check_x > index_x:
					check_x -= 1
					check_y += 1
				if check_x == index_x:
					return True

			if bishop_y > index_y:
				check_y = bishop_y - 1
				while chess_board[check_x][check_y] == '  ' and check_x > index_x:
					check_x -= 1
					check_y -= 1
				if check_x == index_x:
					return True



def queen_control(queen_x, queen_y, index_x, index_y):
	if rock_control(queen_x, queen_y, index_x, index_y) or bishop_control(queen_x, queen_y, index_x, index_y):
		return True



def king_control(king_x, king_y, index_x, index_y):
	if abs(index_x - king_x) <= 1 and abs(index_y - king_y) <= 1:
		return True




def safe_for_white(king_x, king_y):
	for i in range(8):
		for j in range(8):
			if i != king_x or j != king_y:
				if chess_board[i][j] == 'BP' and black_pawn_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'BN' and knight_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'BR' and rock_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'BB' and bishop_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'BQ' and queen_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'BK' and king_control(i, j, king_x, king_y):
					return False
	return True



def safe_for_black(king_x, king_y):
	for i in range(8):
		for j in range(8):
			if i != king_x or j != king_y:
				if chess_board[i][j] == 'WP' and white_pawn_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'WN' and knight_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'WR' and rock_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'WB' and bishop_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'WQ' and queen_control(i, j, king_x, king_y):
					return False
				if chess_board[i][j] == 'WK' and king_control(i, j, king_x, king_y):
					return False
	return True





def white_pawn_move(start_x, start_y, index_x, index_y):
	#go straight 2 grids at first
	if start_y == 6:
		if index_x == start_x and index_y == start_y-2:
			if chess_board[start_x][start_y-1] == '  ' and chess_board[index_x][index_y] == '  ':
				global white_pawn_2_grid_move_x
				global white_pawn_2_grid_move_y
				global white_pawn_2_grid
				white_pawn_2_grid_move_x = index_x
				white_pawn_2_grid_move_y = index_y
				white_pawn_2_grid = True
				return True

	#go straight 1 grid
	if index_x == start_x and index_y == start_y-1:
		if chess_board[index_x][index_y] == '  ':
			return True

	#catch piece
	if white_pawn_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] == 'B':
			return True

	#special move
	if chess_board[index_x][index_y] == '  ' and index_x == black_pawn_2_grid_move_x and index_y == black_pawn_2_grid_move_y - 1:
		if abs(black_pawn_2_grid_move_x - start_x) == 1 and start_y == 3 and black_pawn_2_grid_move_y == 3 and black_pawn_2_grid:
			global white_pawn_special_move
			white_pawn_special_move = True
			return True




def black_pawn_move(start_x, start_y, index_x, index_y):
	#go straight 2 grids at first
	if start_y == 1:
		if index_x == start_x and index_y == start_y+2:
			if chess_board[start_x][start_y+1] == '  ' and chess_board[index_x][index_y] == '  ':
				global black_pawn_2_grid_move_x 
				global black_pawn_2_grid_move_y
				global black_pawn_2_grid
				black_pawn_2_grid_move_x = index_x
				black_pawn_2_grid_move_y = index_y
				black_pawn_2_grid = True
				return True

	#go straight 1 grid
	if index_x == start_x and index_y == start_y+1:
		if chess_board[index_x][index_y] == '  ':
			return True

	#catch piece
	if black_pawn_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] == 'W':
			return True

	#special move
	if chess_board[index_x][index_y] == '  ' and index_x == white_pawn_2_grid_move_x and index_y == white_pawn_2_grid_move_y + 1:
		if abs(white_pawn_2_grid_move_x - start_x) == 1 and start_y == 4 and white_pawn_2_grid_move_y == 4 and white_pawn_2_grid:
			global black_pawn_special_move
			black_pawn_special_move = True
			return True



def knight_move(start_x, start_y, index_x, index_y):
	if knight_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] != chess_board[start_x][start_y][0]:
			return True



def rock_move(start_x, start_y, index_x, index_y):
	if rock_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] != chess_board[start_x][start_y][0]:
			return True 



def bishop_move(start_x, start_y, index_x, index_y):
	if bishop_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] != chess_board[start_x][start_y][0]:
			return True 



def queen_move(start_x, start_y, index_x, index_y):
	if queen_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] != chess_board[start_x][start_y][0]:
			return True



def king_move(start_x, start_y, index_x, index_y):
	if king_control(start_x, start_y, index_x, index_y):
		if chess_board[index_x][index_y][0] != chess_board[start_x][start_y][0]:
			if chess_board[start_x][start_y][0] == 'W' and safe_for_white(index_x, index_y):
				return True
			if chess_board[start_x][start_y][0] == 'B' and safe_for_black(index_x, index_y):
				return True


	#castle
	elif chess_board[start_x][start_y] == 'WK':
		if index_x == 2 and index_y == 7:
			if chess_board[1][7] == '  ' and chess_board[2][7] == '  ' and chess_board[3][7] == '  ':
				global white_rock1_moving
				if white_king_moving == False and white_rock1_moving == False:
					if safe_for_white(4,7) and safe_for_white(3,7) and safe_for_white(2,7):
						chess_board[3][7] = 'WR'
						chess_board[0][7] = '  '
						white_rock1_moving = True
						return True

		if index_x == 6 and index_y == 7:
			if chess_board[5][7] == '  ' and chess_board[6][7] == '  ':
				global white_rock2_moving
				if white_king_moving == False and white_rock2_moving == False:
					if safe_for_white(4,7) and safe_for_white(5,7) and safe_for_white(6,7):
						chess_board[5][7] = 'WR'
						chess_board[7][7] = '  '
						white_rock2_moving = True
						return True

	elif chess_board[start_x][start_y] == 'BK':
		if index_x == 2 and index_y == 0:
			if chess_board[1][0] == '  ' and chess_board[2][0] == '  ' and chess_board[3][0] == '  ':
				global black_rock1_moving
				if black_king_moving == False and black_rock1_moving == False:
					if safe_for_black(4,0) and safe_for_black(3,0) and safe_for_black(2,0):
						chess_board[3][0] = 'BR'
						chess_board[0][0] = '  '
						black_rock1_moving = True
						return True	

		if index_x == 6 and index_y == 0:
			if chess_board[5][0] == '  ' and chess_board[6][0] == '  ':
				global black_rock2_moving
				if black_king_moving == False and black_rock2_moving == False:
					if safe_for_black(4,0) and safe_for_black(5,0) and safe_for_black(6,0):
						chess_board[5][0] = 'BR'
						chess_board[7][0] = '  '
						black_rock2_moving = True
						return True



def safe_move(start_x, start_y, index_x, index_y):

	global white_king_x
	global white_king_y
	global black_king_x
	global black_king_y
	global white_pawn_special_move
	global black_pawn_special_move

	if white_pawn_special_move:
		white_pawn_special_move = False
		chess_board[index_x][index_y] = 'WP'
		chess_board[start_x][start_y] = '  '
		chess_board[index_x][index_y+1] = '  '
		if safe_for_white(white_king_x, white_king_y):
			return True
		else:
			chess_board[start_x][start_y] = 'WP'
			chess_board[index_x][index_y] = '  '
			chess_board[index_x][index_y+1] = 'BP'
			return False

	if black_pawn_special_move:
		black_pawn_special_move = False
		chess_board[index_x][index_y] = 'BP'
		chess_board[start_x][start_y] = '  '
		chess_board[index_x][index_y-1] = '  '
		if safe_for_black(black_king_x, black_king_y):
			return True
		else:
			chess_board[start_x][start_y] = 'BP'
			chess_board[index_x][index_y] = '  '
			chess_board[index_x][index_y-1] = 'WP'
			return False

	else:
		tem = chess_board[index_x][index_y]
		chess_board[index_x][index_y] = chess_board[start_x][start_y]
		chess_board[start_x][start_y] = '  '

		if chess_board[index_x][index_y] == 'WK':
			white_king_x = index_x
			white_king_y = index_y
		elif chess_board[index_x][index_y] == 'BK':
			black_king_x = index_x
			black_king_y = index_y


		if chess_board[index_x][index_y][0] == 'W' and safe_for_white(white_king_x, white_king_y):
			return True
		elif chess_board[index_x][index_y][0] == 'B' and safe_for_black(black_king_x, black_king_y):
			return True
		else:
			if chess_board[index_x][index_y] == 'WK':
				white_king_x = start_x
				white_king_y = start_y
			if chess_board[index_x][index_y] == 'BK':
				black_king_x = start_x
				black_king_y = start_y
			chess_board[start_x][start_y] = chess_board[index_x][index_y]
			chess_board[index_x][index_y] = tem
			return False




def end_game_for_white():

	for i in range(8):
		for j in range(8):

			if chess_board[i][j] == 'WP':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						global white_pawn_special_move
						global white_pawn_2_grid
						
						if white_pawn_move(i, j, x, y):
							if white_pawn_special_move and safe_move(i, j, x, y):
								chess_board[i][j] = 'WP'
								chess_board[x][y] = '  '
								chess_board[x][y+1] = 'BP'
								white_pawn_special_move = False
								white_pawn_2_grid = False
								return "UNKNOWN"
							elif safe_move(i, j, x, y):
								chess_board[i][j] = chess_board[x][y]
								chess_board[x][y] = tem
								white_pawn_special_move = False
								white_pawn_2_grid = False
								return "UNKNOWN"

			elif chess_board[i][j] == 'WR':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if rock_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'WN':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if knight_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'WB':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if bishop_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'WQ':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if queen_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'WK':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if king_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							global white_king_x
							global white_king_y
							white_king_x = i
							white_king_y = j
							return "UNKNOWN"

	if safe_for_white(white_king_x, white_king_y):
		return "DRAW"
	else:
		return "LOSE"





def end_game_for_black():

	for i in range(8):
		for j in range(8):

			if chess_board[i][j] == 'BP':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						global black_pawn_special_move
						global black_pawn_2_grid

						if black_pawn_move(i, j, x, y):
							if black_pawn_special_move and safe_move(i, j, x, y):
								chess_board[i][j] = 'BP'
								chess_board[x][y] = '  '
								chess_board[x][y-1] = 'WP'
								black_pawn_special_move = False
								black_pawn_2_grid = False
								return "UNKNOWN"
							elif safe_move(i, j, x, y):
								chess_board[i][j] = chess_board[x][y]
								chess_board[x][y] = tem
								black_pawn_special_move = False
								black_pawn_2_grid = False
								return "UNKNOWN"

			elif chess_board[i][j] == 'BR':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if rock_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'BN':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if knight_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'BB':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if bishop_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'BQ':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if queen_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							return "UNKNOWN"

			elif chess_board[i][j] == 'BK':
				for x in range(8):
					for y in range(8):
						tem = chess_board[x][y]
						if king_move(i, j, x, y) and safe_move(i, j, x, y):
							chess_board[i][j] = chess_board[x][y]
							chess_board[x][y] = tem
							global black_king_x
							global black_king_y
							black_king_x = i
							black_king_y = j
							return "UNKNOWN"

	if safe_for_black(black_king_x, black_king_y):
		return "DRAW"
	else:
		return "LOSE"



def special_draw_case():
	count_white_bishop = 0
	count_white_knight = 0
	count_black_bishop = 0 
	count_black_knight = 0 

	for i in range(8):
		for j in range(8):
			if chess_board[i][j][1] == 'P':
				return "UNKNOWN"
			if chess_board[i][j][1] == 'Q':
				return "UNKNOWN"
			if chess_board[i][j][1] == 'R':
				return "UNKNOWN"
			if chess_board[i][j] == 'WB':
				count_white_bishop += 1
			if chess_board[i][j] == 'WN':
				count_white_knight += 1
			if chess_board[i][j] == 'BB':
				count_black_bishop += 1
			if chess_board[i][j] == 'BN':
				count_black_knight += 1

	if count_white_bishop + count_white_knight <=1 and count_black_bishop + count_black_knight <=1:
		return "DRAW"
	else:
		return "UNKNOWN"


def end_game():
	
	if white_turn and end_game_for_white() == "LOSE":
		return "BLACK WIN"
	if white_turn and end_game_for_white() == "DRAW":
		return "DRAW"
	if black_turn and end_game_for_black() == "LOSE":
		return "WHITE WIN"
	if black_turn and end_game_for_black() == "DRAW":
		return "DRAW"
	if len(repeated_moves) == 9 and repeated_moves[0] == repeated_moves[4] and repeated_moves[4] == repeated_moves[8]:
		return "DRAW"
	if special_draw_case() == "DRAW":
		return "DRAW"
	else:
		return "UNKNOWN"


while running:

	clock.tick(60)
	screen.fill(BROWN)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	#draw chessboard
	for i in range(8):
		for j in range(8):

			if (i-j)%2 == 0:
				pygame.draw.rect(screen,WHITE,(SQUARE_SIZE*(i+1) - 50, SQUARE_SIZE*(j+1) - 50, SQUARE_SIZE, SQUARE_SIZE))
			else:
				pygame.draw.rect(screen,GREEN,(SQUARE_SIZE*(i+1) - 50, SQUARE_SIZE*(j+1) - 50, SQUARE_SIZE, SQUARE_SIZE))

			if safe_for_white(white_king_x, white_king_y) == False:
				pygame.draw.rect(screen,RED,(SQUARE_SIZE*(white_king_x+1) - 50, SQUARE_SIZE*(white_king_y+1) - 50, SQUARE_SIZE, SQUARE_SIZE))

			if safe_for_black(black_king_x, black_king_y) == False:
				pygame.draw.rect(screen,RED,(SQUARE_SIZE*(black_king_x+1) - 50, SQUARE_SIZE*(black_king_y+1) - 50, SQUARE_SIZE, SQUARE_SIZE))

			

	#draw index
	for i in range(8):
		letter = font.render(chr(i+65),True,WHITE)
		screen.blit(letter, (SQUARE_SIZE*(i+1) - 15, 675))
		number = font.render(str(i+1),True,WHITE)
		screen.blit(number,(10, SQUARE_SIZE*(7-i) + 60))


	if hold_chess:
		pygame.draw.rect(screen,YELLOW,(get_x, get_y, SQUARE_SIZE, SQUARE_SIZE))


	#draw chessman
	for i in range(8):
		for j in range(8):
			if chess_board[i][j] == 'BR':
				screen.blit(black_rock_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'BN':
				screen.blit(black_knight_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'BB':
				screen.blit(black_bishop_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'BQ':
				screen.blit(black_queen_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'BK':
				screen.blit(black_king_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'BP':
				screen.blit(black_pawn_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'WR':
				screen.blit(white_rock_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'WN':
				screen.blit(white_knight_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'WB':
				screen.blit(white_bishop_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'WQ':
				screen.blit(white_queen_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'WK':
				screen.blit(white_king_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))
			if chess_board[i][j] == 'WP':
				screen.blit(white_pawn_image,(X_POSITION + SQUARE_SIZE*i, Y_POSITION + SQUARE_SIZE*j))

	if white_promotion:
		pygame.draw.rect(screen,BLACK,(X_POSITION + SQUARE_SIZE*2 - 5, Y_POSITION + SQUARE_SIZE -5, SQUARE_SIZE*4 + 10, SQUARE_SIZE + 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*2 + 5, Y_POSITION + SQUARE_SIZE + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*3 + 5, Y_POSITION + SQUARE_SIZE + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*4 + 5, Y_POSITION + SQUARE_SIZE + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*5 + 5, Y_POSITION + SQUARE_SIZE + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		screen.blit(white_queen_image,(X_POSITION + SQUARE_SIZE*2, Y_POSITION + SQUARE_SIZE))
		screen.blit(white_rock_image,(X_POSITION + SQUARE_SIZE*3, Y_POSITION + SQUARE_SIZE))
		screen.blit(white_bishop_image,(X_POSITION + SQUARE_SIZE*4, Y_POSITION + SQUARE_SIZE))
		screen.blit(white_knight_image,(X_POSITION + SQUARE_SIZE*5, Y_POSITION + SQUARE_SIZE))

	if black_promotion:
		pygame.draw.rect(screen,BLACK,(X_POSITION + SQUARE_SIZE*2 - 5, Y_POSITION + SQUARE_SIZE*6 - 5, SQUARE_SIZE*4 + 10, SQUARE_SIZE + 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*2 + 5, Y_POSITION + SQUARE_SIZE*6 + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*3 + 5, Y_POSITION + SQUARE_SIZE*6 + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*4 + 5, Y_POSITION + SQUARE_SIZE*6 + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		pygame.draw.rect(screen,WHITE,(X_POSITION + SQUARE_SIZE*5 + 5, Y_POSITION + SQUARE_SIZE*6 + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
		screen.blit(black_queen_image,(X_POSITION + SQUARE_SIZE*2, Y_POSITION + SQUARE_SIZE*6))
		screen.blit(black_rock_image,(X_POSITION + SQUARE_SIZE*3, Y_POSITION + SQUARE_SIZE*6))
		screen.blit(black_bishop_image,(X_POSITION + SQUARE_SIZE*4, Y_POSITION + SQUARE_SIZE*6))
		screen.blit(black_knight_image,(X_POSITION + SQUARE_SIZE*5, Y_POSITION + SQUARE_SIZE*6))

	


	if end_game() != "UNKNOWN":
		pygame.draw.rect(screen, BLACK, (200, 200, 300, 280))
		result_txt = big_font.render(end_game(), True, WHITE)

		if end_game() == "DRAW":
			screen.blit(result_txt, (298, 250))
		else:
			screen.blit(result_txt, (260, 250))

		pygame.draw.rect(screen, YELLOW, (250,350,200,80))
		restart_txt = font.render('RESTART', True, BLACK)
		screen.blit(restart_txt, (312, 378))

								

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if end_game() != "UNKNOWN":
					if 250 < mouse_x < 450 and 350 < mouse_y < 430:
						chess_board = [['BR','BP','  ','  ','  ','  ','WP','WR'],
									   ['BN','BP','  ','  ','  ','  ','WP','WN'],
									   ['BB','BP','  ','  ','  ','  ','WP','WB'],
									   ['BQ','BP','  ','  ','  ','  ','WP','WQ'],
									   ['BK','BP','  ','  ','  ','  ','WP','WK'],
									   ['BB','BP','  ','  ','  ','  ','WP','WB'],
									   ['BN','BP','  ','  ','  ','  ','WP','WN'],
									   ['BR','BP','  ','  ','  ','  ','WP','WR']]


						hold_chess = False
						get_x = 0
						get_y = 0
						index_x = 0
						index_y = 0
						start_x = 0
						start_y = 0 
						white_turn = True
						black_turn = False
						end_turn = False
						white_promotion = False
						black_promotion = False
						white_king_x = 4
						white_king_y = 7
						black_king_x = 4
						black_king_y = 0
						white_king_moving = False
						black_king_moving = False
						white_rock1_moving = False
						black_rock1_moving = False
						white_rock2_moving = False
						black_rock2_moving = False
						white_pawn_2_grid_move_x = -1
						white_pawn_2_grid_move_y = -1
						black_pawn_2_grid_move_x = -1
						black_pawn_2_grid_move_y = -1
						white_pawn_2_grid = False
						black_pawn_2_grid = False
						white_pawn_special_move = False
						black_pawn_special_move = False
						repeated_moves = []


				else:
					if X_POSITION < mouse_x < X_POSITION + SQUARE_SIZE*8 and Y_POSITION < mouse_y < Y_POSITION + SQUARE_SIZE*8:
						get_x = int((mouse_x - X_POSITION) / SQUARE_SIZE) * SQUARE_SIZE + X_POSITION
						get_y = int((mouse_y - Y_POSITION) / SQUARE_SIZE) * SQUARE_SIZE + Y_POSITION
						index_x = int((get_x - X_POSITION) / SQUARE_SIZE)
						index_y = int((get_y - Y_POSITION) / SQUARE_SIZE)



						if hold_chess:

							#white pawn
							if chess_board[start_x][start_y] == 'WP':
								if white_pawn_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									end_turn = True

									#promotion
									if index_y == 0:
										white_promotion = True
								

							#black pawn
							if chess_board[start_x][start_y] == 'BP':
								if black_pawn_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									end_turn = True

									#promotion
									if index_y == 7:
										black_promotion = True


							#knight
							if chess_board[start_x][start_y][1] == 'N':
								if knight_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									end_turn = True
		

							#rock
							if chess_board[start_x][start_y][1] == 'R':
								if rock_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									if chess_board[index_x][index_y] == 'WR':
										if start_x == 0 and start_y == 7 and white_rock1_moving == False:
											white_rock1_moving = True
										if start_x == 7 and start_y == 7 and white_rock2_moving == False:
											white_rock2_moving = True

									if chess_board[index_x][index_y] == 'BR':
										if start_x == 0 and start_y == 0 and black_rock1_moving == False:
											black_rock1_moving = True
										if start_x == 7 and start_y == 0 and black_rock2_moving == False:
											black_rock2_moving = True

									end_turn = True


							#bishop
							if chess_board[start_x][start_y][1] == 'B':
								if bishop_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									end_turn = True


							#queen
							if chess_board[start_x][start_y][1] == 'Q':
								if queen_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									end_turn = True


							#king
							if chess_board[start_x][start_y][1] == 'K':
								if king_move(start_x, start_y, index_x, index_y) and safe_move(start_x, start_y, index_x, index_y):
									if chess_board[index_x][index_y] == 'WK':
										white_king_x = index_x
										white_king_y = index_y

										if white_king_moving == False:
											white_king_moving = True

									if chess_board[index_x][index_y] == 'BK':
										black_king_x = index_x
										black_king_y = index_y

										if black_king_moving == False:
											black_king_moving = True

									end_turn = True

		

							if end_turn:
								if black_turn and chess_board[index_x][index_y][0] == 'B':
									if white_pawn_2_grid:
										white_pawn_2_grid = False
									black_turn = False
									white_turn = True

								if white_turn and chess_board[index_x][index_y][0] == 'W':
									if black_pawn_2_grid:
										black_pawn_2_grid = False
									black_turn = True
									white_turn = False

								repeated_moves.append([chess_board[index_x][index_y], index_x, index_y])
								if len(repeated_moves) > 9:
									repeated_moves.pop(0)

								if white_promotion or black_promotion:
									start_x = index_x
									start_y = index_y

								end_turn = False


							hold_chess = False

						else:
							if white_promotion:
								if X_POSITION + SQUARE_SIZE*2 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*3 - 5 and Y_POSITION + SQUARE_SIZE + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*2 - 5:
									chess_board[start_x][start_y] = 'WQ'
									white_promotion = False
								if X_POSITION + SQUARE_SIZE*3 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*4 - 5 and Y_POSITION + SQUARE_SIZE + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*2 - 5:
									chess_board[start_x][start_y] = 'WR'
									white_promotion = False
								if X_POSITION + SQUARE_SIZE*4 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*5 - 5 and Y_POSITION + SQUARE_SIZE + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*2 - 5:
									chess_board[start_x][start_y] = 'WB'
									white_promotion = False
								if X_POSITION + SQUARE_SIZE*5 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*6 - 5 and Y_POSITION + SQUARE_SIZE + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*2 - 5:
									chess_board[start_x][start_y] = 'WN'
									white_promotion = False


							elif black_promotion:
								if X_POSITION + SQUARE_SIZE*2 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*3 - 5 and Y_POSITION + SQUARE_SIZE*6 + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*7 - 5:
									chess_board[start_x][start_y] = 'BQ'
									black_promotion = False
								if X_POSITION + SQUARE_SIZE*3 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*4 - 5 and Y_POSITION + SQUARE_SIZE*6 + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*7 - 5:
									chess_board[start_x][start_y] = 'BR'
									black_promotion = False
								if X_POSITION + SQUARE_SIZE*4 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*5 - 5 and Y_POSITION + SQUARE_SIZE*6 + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*7 - 5:
									chess_board[start_x][start_y] = 'BB'
									black_promotion = False
								if X_POSITION + SQUARE_SIZE*5 + 5 < mouse_x < X_POSITION + SQUARE_SIZE*6 - 5 and Y_POSITION + SQUARE_SIZE*6 + 5 < mouse_y < Y_POSITION + SQUARE_SIZE*7 - 5:
									chess_board[start_x][start_y] = 'BN'
									black_promotion = False


							elif (black_turn and chess_board[index_x][index_y][0] == 'B') or (white_turn and chess_board[index_x][index_y][0] == 'W'):
								start_x = index_x
								start_y = index_y
								hold_chess = True						


	pygame.display.flip()

pygame.quit()
