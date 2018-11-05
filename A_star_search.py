# Jacky Teoh
# GRAPH-SEARCH Algorithm with A* Search strategy for the 8-puzzle problem

# Find manhattan sums of up/down/left/right of current and do it again
# Tie?? Do all ties? Pick least manhattan_sum of those ties?
# while manhattan_sum != 0: depth+=1, up down left right?
# recursive? While loop? figure it out
# add onto sequence of actions
# def search(matrix, things need to print out) <-- UNLESS I CAN ACCESS THINGS TO PRINT OUT WITHOUT PASSING IN

# Search function, performs the actions
#def search(x):
#move function should return matrix and direction

#Reading in the file, allowing the user to select which file to search for
print("What is the complete filename you wish to use this A* search for?")
filename = input()
initial = open(filename, "r")
got_lines = initial.readlines()

# Creating empty matrices for both the initial and goal states of the puzzle
puzzle = []
goal = []
depth_level = 0
number_of_nodes_generated = 1
sequence_of_actions = []
manhattan_sum = None
# Creating arrays to hold positions of the tiles in both initial and goal states of puzzle.
initialPosition = []
#goal_position = []

# Puts initial into a matrix: puzzle
for i in range(3):
	line = got_lines[i]
	matrix_line = []
	for x in line:
		if x.isdigit():
			matrix_line.append(int(x))
	puzzle.append(matrix_line)

# Puts goal into a matrix: goal
for j in range (4,7):
	line = got_lines[j]
	matrix_line = []
	for y in line:
		if y.isdigit():
			matrix_line.append(int(y))
	goal.append(matrix_line)

def check_goal(to_check):
	goal_position = []
	for x in range(0,3):
		for y in range(0,3):
			if to_check == goal[x][y]:
				goal_position.append(x)
				goal_position.append(y)
	return goal_position

def find_manhattan_distance(initial1, initial2, goal_array):
	return abs(goal_array[0] - initial1) + abs(goal_array[1] - initial2)


def find_manhattan_sum(array):
	manhattan_sum = 0
	for x in range(0, 3):
		for y in range(0, 3):
			goal_checker = check_goal(array[x][y])
			manhattan_distance = find_manhattan_distance(x, y, goal_checker)
			print(array[x][y], ", Manhattan Distance = ", manhattan_distance)
			manhattan_sum += manhattan_distance
	print(manhattan_sum)
	return manhattan_sum

def find_position_of_zero(matrix):
	position_of_zero = []
	for x in range(0, 3):
		for y in range(0, 3):
			if matrix[x][y] == 0:
				position_of_zero.append(x)
				position_of_zero.append(y)
	return position_of_zero

def swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix):
	temp = new_matrix[position_of_move_x][position_of_move_y]
	new_matrix[position_of_move_x][position_of_move_y] = 0
	new_matrix[position_of_zero_x][position_of_zero_y] = temp

def moveUp(matrix):
	global number_of_nodes_generated
	direction = "Up"
	new_matrix = matrix
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_x != 2:	
		position_of_move_x = position_of_zero[0] + 1
		position_of_move_y = position_of_zero[1]
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		print(number_of_nodes_generated)
		print(new_matrix)
		return new_matrix, direction

def moveDown(matrix):
	global number_of_nodes_generated
	direction = "Down"
	new_matrix = matrix
	position_of_move = []
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_x != 0:	
		position_of_move_x = position_of_zero[0] - 1
		position_of_move_y = position_of_zero[1]
		position_of_move.append(position_of_move_x)
		position_of_move.append(position_of_move_y)
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		print(number_of_nodes_generated)
		print(new_matrix)
		return new_matrix, direction

def moveLeft(matrix):
	global number_of_nodes_generated
	direction = "Left"
	new_matrix = matrix
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_y != 2:
		position_of_move_x = position_of_zero[0]
		position_of_move_y = position_of_zero[1] + 1
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		print(number_of_nodes_generated)
		print(new_matrix)
		return new_matrix, direction

def moveRight(matrix):
	global number_of_nodes_generated
	direction = "Right"
	new_matrix = matrix
	position_of_move = []
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_y != 0:	
		position_of_move_x = position_of_zero[0] 
		position_of_move_y = position_of_zero[1] - 1
		position_of_move.append(position_of_move_x)
		position_of_move.append(position_of_move_y)
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		print(number_of_nodes_generated)
		print(new_matrix)
		return new_matrix, direction

#find_position_of_zero(puzzle)	
def search(puzzle):
	global depth_level
	global number_of_nodes_generated
	global sequence_of_actions
	global manhattan_sum

	left = moveLeft(puzzle)
	if left:
		sequence_of_actions.append(left[1])

	#left = moveLeft(puzzle)
	#if left:
	#	sequence_of_actions.append(left[1])

	right = moveRight(left[0])
	if right:
		sequence_of_actions.append(right[1])

	down = moveDown(right[0])
	if down:
		sequence_of_actions.append(down[1])

	#up = moveUp(right)
	#if up:
	#	sequence_of_actions.append(up[1])

	print(number_of_nodes_generated)
	print(sequence_of_actions)
#up[1]

search(puzzle)

# Writing to the output file, Complete, the initial state, the goal state, 
# the depth level, the # of nodes generated, and the sequence of actions taken to reach the goal
#if puzzle == goal:
#	print("Wow you got it!")
#	complete = open("goal.txt", "wr")
#	for i in got_lines:
#		complete.write(i)
#	complete.write("/n", depth_level)
#	complete.write("/n", number_of_nodes_generated)
#	complete.write("/n", sequence_of_actions)
#	complete.close()
#else:
#	print("This isn't complete yet!")

#initial.close()
