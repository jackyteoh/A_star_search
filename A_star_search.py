# Jacky Teoh
# GRAPH-SEARCH Algorithm with A* Search strategy for the 8-puzzle problem

# Find manhattan sums of up/down/left/right of current and do it again
# Tie?? Do all ties? Pick least manhattan_sum of those ties?
# while manhattan_sum != 0: depth+=1, up down left right?
# recursive? While loop? figure it out
# add onto sequence of actions

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
unique_matrices = []

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
			#print(array[x][y], ", Manhattan Distance = ", manhattan_distance)
			manhattan_sum += manhattan_distance
	#print("Manhattan sum:", manhattan_sum)
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
	return new_matrix

def moveUp(matrix):
	global number_of_nodes_generated
	direction = "Up"
	new_matrix = [list(i) for i in matrix]
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_x != 2:	
		position_of_move_x = position_of_zero[0] + 1
		position_of_move_y = position_of_zero[1]
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		#print(number_of_nodes_generated)
		#print(new_matrix)
		return new_matrix, direction

def moveDown(matrix):
	global number_of_nodes_generated
	direction = "Down"
	new_matrix = [list(i) for i in matrix]
	#position_of_move = []
	position_of_zero = find_position_of_zero(new_matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_x != 0:	
		position_of_move_x = position_of_zero[0] - 1
		position_of_move_y = position_of_zero[1]
		#position_of_move.append(position_of_move_x)
		#position_of_move.append(position_of_move_y)
		new_matrix = swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		#print(number_of_nodes_generated)
		#print(new_matrix)
		return new_matrix, direction

def moveLeft(matrix):
	global number_of_nodes_generated
	direction = "Left"
	new_matrix = [list(i) for i in matrix]
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_y != 2:
		position_of_move_x = position_of_zero[0]
		position_of_move_y = position_of_zero[1] + 1
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		#print(number_of_nodes_generated)
		#print(new_matrix)
		return new_matrix, direction

def moveRight(matrix):
	global number_of_nodes_generated
	direction = "Right"
	new_matrix = [list(i) for i in matrix]
	#position_of_move = []
	position_of_zero = find_position_of_zero(matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_y != 0:	
		position_of_move_x = position_of_zero[0] 
		position_of_move_y = position_of_zero[1] - 1
		#position_of_move.append(position_of_move_x)
		#position_of_move.append(position_of_move_y)
		swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		#print(number_of_nodes_generated)
		#print(new_matrix)
		return new_matrix, direction

def search(matrix):
	global depth_level
	global number_of_nodes_generated
	global sequence_of_actions
	global manhattan_sum
	global unique_matrices

	manhattan_sum = find_manhattan_sum(matrix)

	if manhattan_sum == 0:
		print("Wow you got it!")
		complete = open("goal.txt", "w")
		for i in got_lines:
			complete.write(i)
		complete.write("\n\n" + str(depth_level))
		complete.write("\n" + str(number_of_nodes_generated))
		complete.write("\n" + str(sequence_of_actions))
		return complete
		complete.close()

	while manhattan_sum != 0:
		depth_level += 1
		manhattan_sum_up = None
		manhattan_sum_down = None
		manhattan_sum_left = None
		manhattan_sum_right = None

		up = moveUp(matrix)
		if up:
			manhattan_sum_up = find_manhattan_sum(up[0])
		down = moveDown(matrix)
		if down:
			manhattan_sum_down = find_manhattan_sum(down[0])
		left = moveLeft(matrix)
		if left:
			manhattan_sum_left = find_manhattan_sum(left[0])
		right = moveRight(matrix)
		if right:
			manhattan_sum_right = find_manhattan_sum(right[0])

		mins = [] 
		mins.append(manhattan_sum_up)
		mins.append(manhattan_sum_down)
		mins.append(manhattan_sum_right)
		mins.append(manhattan_sum_left)

		minimum_manhattan_sum = min(x for x in mins if x is not None)
		#if up is not None:
		#	up_tuple = (tuple(i) for i in up[0])
		#	#print(tuple(up_tuple))
		#if down is not None:
		#	down_tuple = (tuple(i) for i in down[0])
		#	#print(tuple(down_tuple))
		#if right is not None:
		#	right_tuple = (tuple(i) for i in right[0])
		#	#print(tuple(right_tuple))
		#if left is not None:
		#	left_tuple = (tuple(i) for i in left[0])
		#	#print(tuple(left_tuple))

		#if manhattan_sum_up is not None:
		if minimum_manhattan_sum == manhattan_sum_up:
				#up_tuple = (tuple(i) for i in up[0])
				#if up_tuple not in unique_matrices:
				#	unique_matrices.add(tuple(up_tuple))
			if up[0] not in unique_matrices:
				unique_matrices.append(up[0])
				sequence_of_actions.append(up[1])
				print(sequence_of_actions)
				return search(up[0])
			elif up[0] in unique_matrices:
				pass
			pass
		#elif manhattan_sum_down is not None:
		elif minimum_manhattan_sum == manhattan_sum_down:
				#down_tuple = (tuple(i) for i in down[0])
				#if down_tuple not in unique_matrices:
				#	unique_matrices.add(tuple(down_tuple))
			if down[0] not in unique_matrices:
				unique_matrices.append(down[0])
				sequence_of_actions.append(down[1])
				print(sequence_of_actions)
				return search(down[0])
			elif down[0] in unique_matrices:
				pass
			pass
		#elif manhattan_sum_right is not None:
		elif minimum_manhattan_sum == manhattan_sum_right:
				#right_tuple = (tuple(i) for i in right[0])
				#if right_tuple not in unique_matrices:
				#	unique_matrices.add(tuple(right_tuple))
			if right[0] not in unique_matrices:
				unique_matrices.append(right[0])
				sequence_of_actions.append(right[1])
				print(sequence_of_actions)
				return search(right[0])
			elif right[0] in unique_matrices:
				pass
			pass
		#elif manhattan_sum_left is not None:
		elif minimum_manhattan_sum == manhattan_sum_left:
			#left_tuple = (tuple(i) for i in left[0])
			#if left_tuple not in unique_matrices:
			#	unique_matrices.add(tuple(left_tuple))
			if left[0] not in unique_matrices:
				unique_matrices.append(left[0])
				sequence_of_actions.append(left[1])
				print(sequence_of_actions)
				return search(left[0])
			elif left[0] in unique_matrices:
				pass
			pass


	print(depth_level)
	print(number_of_nodes_generated)
	print(sequence_of_actions)

search(puzzle)

initial.close()

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
