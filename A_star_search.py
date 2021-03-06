# Jacky Teoh
# GRAPH-SEARCH Algorithm with A* Search strategy for the 8-puzzle problem

# Reading in the file, allowing the user to input which file to search for
print("What is the complete filename you wish to use this A* search for?")
filename = input()
initial = open(filename, "r")
got_lines = initial.readlines()

# Creating empty matrices for both the initial and goal states of the puzzle
# Initializes needed variables: depth_level, number_of_nodes_generated, sequence_of_actions
# manhattan_sum, explored_matrices
puzzle = []
goal = []
depth_level = 0
number_of_nodes_generated = 1
sequence_of_actions = []
manhattan_sum = None
explored_matrices = []

# Making a Priority Queue with popping least manhattan sums to represent the frontier
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 

    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            min = 0
            for i in range(len(self.queue)): 
                if self.queue[i][1] < self.queue[min][1]: 
                    min = i 
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError:
            exit()

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

# Initializing a priority queue, start it with the initial puzzle
search_frontier = PriorityQueue()

# Passes in a value, iterates through the goal matrix and finds the position of that value
# returns x and y as a list of that value in the goal matrix
def check_goal(to_check):
	goal_position = []
	for x in range(0,3):
		for y in range(0,3):
			if to_check == goal[x][y]:
				goal_position.append(x)
				goal_position.append(y)
	return goal_position

# Passed in x position of initial value as initial1, y position of initial value as initial2
# goal_array is the list returned from check_goal
# returns the absolute value of (the diff of x + diff of y)
def find_manhattan_distance(initial1, initial2, goal_array):
	return abs(goal_array[0] - initial1) + abs(goal_array[1] - initial2)

# Passed in a matrix (initial one) iterates through each element in the matrix,
# calls find_manhattan_distance on each element, adds that to the local manhattan_sum
# returns manhattan_sum, which is the sum of Manhattan Distances of all elements
def find_manhattan_sum(array):
	manhattan_sum = 0
	for x in range(0, 3):
		for y in range(0, 3):
			goal_checker = check_goal(array[x][y])
			manhattan_distance = find_manhattan_distance(x, y, goal_checker)
			manhattan_sum += manhattan_distance
	return manhattan_sum

# Passed in a matrix (intiial)
# Iterates through the matrix to find the position of the 0,
# Returns a list with x and y position of the 0 when found
def find_position_of_zero(matrix):
	position_of_zero = []
	for x in range(0, 3):
		for y in range(0, 3):
			if matrix[x][y] == 0:
				position_of_zero.append(x)
				position_of_zero.append(y)
	return position_of_zero

# Passed in x and y positions of the element to be moved, x and y of the zero, and the matrix to move in
# Creates a temp of the to move element to store it, changes the element's old position to 0,
# Change's zero's old position to the temp (where we stored the element), returns the matrix effectively swapped
def swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix):
	temp = new_matrix[position_of_move_x][position_of_move_y]
	new_matrix[position_of_move_x][position_of_move_y] = 0
	new_matrix[position_of_zero_x][position_of_zero_y] = temp
	return new_matrix

# Passed in a matrix, direction variable corresponds to the type of move
# Deep copies the matrix passed in to new_matrix, finds the position of zero and stores the x and y positions
# For every where else the position of 0 CANNOT BE (differs for each move), finds the position of the element to swap,
# swaps positions and stores in new_matrix, increments number_of_nodes_generated, returns new_matrix, direction as a list
def moveUp(matrix):
	global number_of_nodes_generated
	direction = "Up"
	new_matrix = [list(i) for i in matrix]
	position_of_zero = find_position_of_zero(new_matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_x != 2:	
		position_of_move_x = position_of_zero[0] + 1
		position_of_move_y = position_of_zero[1]
		new_matrix = swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		return new_matrix, direction

# Passed in a matrix, direction variable corresponds to the type of move
# Deep copies the matrix passed in to new_matrix, finds the position of zero and stores the x and y positions
# For every where else the position of 0 CANNOT BE (differs for each move), finds the position of the element to swap,
# swaps positions and stores in new_matrix, increments number_of_nodes_generated, returns new_matrix, direction as a list
def moveDown(matrix):
	global number_of_nodes_generated
	direction = "Down"
	new_matrix = [list(i) for i in matrix]
	position_of_zero = find_position_of_zero(new_matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_x != 0:	
		position_of_move_x = position_of_zero[0] - 1
		position_of_move_y = position_of_zero[1]
		new_matrix = swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		return new_matrix, direction

# Passed in a matrix, direction variable corresponds to the type of move
# Deep copies the matrix passed in to new_matrix, finds the position of zero and stores the x and y positions
# For every where else the position of 0 CANNOT BE (differs for each move), finds the position of the element to swap,
# swaps positions and stores in new_matrix, increments number_of_nodes_generated, returns new_matrix, direction as a list
def moveLeft(matrix):
	global number_of_nodes_generated
	direction = "Left"
	new_matrix = [list(i) for i in matrix]
	position_of_zero = find_position_of_zero(new_matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_y != 2:
		position_of_move_x = position_of_zero[0]
		position_of_move_y = position_of_zero[1] + 1
		new_matrix = swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		return new_matrix, direction

# Passed in a matrix, direction variable corresponds to the type of move
# Deep copies the matrix passed in to new_matrix, finds the position of zero and stores the x and y positions
# For every where else the position of 0 CANNOT BE (differs for each move), finds the position of the element to swap,
# swaps positions and stores in new_matrix, increments number_of_nodes_generated, returns new_matrix, direction as a list
def moveRight(matrix):
	global number_of_nodes_generated
	direction = "Right"
	new_matrix = [list(i) for i in matrix]
	position_of_zero = find_position_of_zero(new_matrix)
	position_of_zero_x = position_of_zero[0]
	position_of_zero_y = position_of_zero[1]
	if position_of_zero_y != 0:	
		position_of_move_x = position_of_zero[0] 
		position_of_move_y = position_of_zero[1] - 1
		new_matrix = swap_positions(position_of_move_x, position_of_move_y, position_of_zero_x, position_of_zero_y, new_matrix)
		number_of_nodes_generated+=1
		return new_matrix, direction

# Main search function, passed in a matrix
# gets globals of all needed variables, checks the manhattan_sum to see if it made it to the goal node
# (manhattan_sum == 0), if not, while it != 0, increases depth_level, finds manhattan sum of each move if it exists
def search(matrix):
	global puzzle
	global goal
	global depth_level
	global number_of_nodes_generated
	global sequence_of_actions
	global manhattan_sum
	global explored_matrices
	global search_frontier

	manhattan_sum = find_manhattan_sum(matrix)
	f_n_value = manhattan_sum + depth_level

	while manhattan_sum != 0:
		depth_level += 1
		manhattan_sum_up = None
		manhattan_sum_down = None
		manhattan_sum_left = None
		manhattan_sum_right = None

		# Finds and returns all moves (if possible) of the matrix passed in
		# Finds the manhattan sum of new matrix, and updates the f_n values for corresponding moves
		# By adding manhattan sum + depth level
		# Adds the new matrix, along with f_n value and the direction to the search frontier
		up = moveUp(matrix)
		if up is not None:
			manhattan_sum_up = find_manhattan_sum(up[0])
			f_n_up_value = manhattan_sum_up + depth_level
			search_frontier.insert([up[0], f_n_up_value, up[1]])

		down = moveDown(matrix)
		if down is not None:
			manhattan_sum_down = find_manhattan_sum(down[0])
			f_n_down_value = manhattan_sum_down + depth_level
			search_frontier.insert([down[0], f_n_down_value, down[1]])

		left = moveLeft(matrix)
		if left is not None:
			manhattan_sum_left = find_manhattan_sum(left[0])
			f_n_left_value = manhattan_sum_left + depth_level
			search_frontier.insert([left[0], f_n_left_value, left[1]])

		right = moveRight(matrix)
		if right is not None:
			manhattan_sum_right = find_manhattan_sum(right[0])
			f_n_right_value = manhattan_sum_right + depth_level
			search_frontier.insert([right[0], manhattan_sum_right + depth_level, right[1]])

		# Pops off the search frontier
		# If not explored already, add to explored and add to sequence of actions the action took to get there
		# Call search again
		# If in explored, pop pop and search again
		least_f_n = search_frontier.delete()
		if least_f_n[0] not in explored_matrices:
			explored_matrices.append(least_f_n[0])
			sequence_of_actions.append(least_f_n[2])
			return search((least_f_n[0]))
		elif least_f_n[0] in explored_matrices:
			while least_f_n[0] in explored_matrices:
				least_f_n = search_frontier.delete()
			return search((least_f_n[0]))

	# When manhattan sum is 0, write to the file with depth_levels, number of nodes generated, and sequences of actions
	if manhattan_sum == 0:

		print("Wow you got it!")
		complete = open("output.txt", "w")
		for i in got_lines:
			complete.write(i)
		complete.write("\n\n" + "Depth level is: " + str(depth_level))
		complete.write("\n" + "Number of nodes generated is: " + str(number_of_nodes_generated))
		complete.write("\n" + "Sequence of Actions is: " + str(sequence_of_actions))

		print("Depth level is: " + str(depth_level))
		print("Number of nodes generated is: " + str(number_of_nodes_generated))
		print("Sequence of Actions is: " + str(sequence_of_actions))

		complete.close()
		return

search(puzzle)

initial.close()