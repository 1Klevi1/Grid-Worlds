# class Grid_World: # creating a main Class
#     def __init__(self, row, column): # main function with 2 parameters: row and column
#         self.grid = [[0 for i in range(column)] for j in range(row)] # creating grid(world) with a nested list comprehension
#         self.grid[2][2] = "Agent" # the position [2][2] is where we can find our Agent
#         self.current_row = 2 # saving the row coordinate of the Agent in the variable current_row
#         self.current_column = 2 #  saving the column coordinate of the Agent in the variable current_column
#
#     def moveAgentWest(self):  # creating a function to move on the West side (left)
#         self.grid[self.current_row][self.current_column] = 0 # updating the stored variables in grid to 0
#         self.current_column = (self.current_column - 1) % len(self.grid[0]) # subtracting column with 1 and using module to wrap it around in the beginning of the column
#         self.grid[self.current_row][self.current_column] = "Agent" # updating the stored variables with Agent
#
#     def moveAgentWestBouncy(self):  # creating a function to move on the West side but it will stop if the column is 0
#         if self.current_column > 0: # checking if the column is greater than 0
#             self.grid[self.current_row][self.current_column] = 0# updating the stored variables in grid to 0
#             self.current_column = self.current_column - 1 # subtracting column with 1
#             self.grid[self.current_row][self.current_column] = "Agent"# updating the stored variables with Agent
#
#     def moveNorthAroundTheWorld(self):  #creating a function to move North and around the world
#         self.grid[self.current_row][self.current_column] = 0 # updating the stored variables in grid to 0
#         self.current_row = (self.current_row - 1) % len(self.grid)# subtracting row with 1 and using module to wrap it around in the beginning of the row
#         self.grid[self.current_row][self.current_column] = "Agent"# updating the stored variables with Agent
#
#     def print_grid(self):#creating a function to print the rows of the grid(world)
#         for row in self.grid: # using a for loop to loop inside the grid(world)
#             print(row, end="\n")# printing row
#         print()
#
# world1 = Grid_World(5, 5) # creating a 5x5 grid(world)
# print(
#     """
# Expected:
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 'Agent', 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# Result:""")
# world1.print_grid()# output the grid
#
# for i in range(2): # looping 2 times world1.moveAgentWest() to get a output
#     world1.moveAgentWest()
# print(
#     """
# Expected:
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# ['Agent', 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# Result:""")
# world1.print_grid()
#
# for i in range(2):# looping 2 times world1.moveAgentWest() to get a output
#     world1.moveAgentWestBouncy()
# print(
#     """
# Expected:
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# ['Agent', 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# Result:""")
# world1.print_grid()
#
# for i in range(3):
#     world1.moveNorthAroundTheWorld()
# print(
# """
# Expected:
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# ['Agent', 0, 0, 0, 0]
# Result:""")
# world1.print_grid()

class Agent:
    def __init__(self):
        self.row = 2
        self.col = 2

    def west(self):
        return self.col - 1

    def east(self):
        return self.col + 1

    def north(self):
        return self.row - 1

    def south(self):
        return self.row + 1

    def agent_position(self):
        return f"The Agent is located at: ({self.row}, {self.col})"


class GridWorld:

    def __init__(self, rows, cols, agent):
        self.grid = [["  0 " for i in range(rows)] for j in range(cols)]
        self.agent = Agent()
        self.Leaf_row = 2
        self.Leaf_col = 3
        self.grid[agent.row][agent.col] = "Agent"
        self.grid[self.Leaf_row][self.Leaf_col] = "leaf"

    def agent_moving_west(self):
        empty = "  0 "
        next_col = self.agent.col - 1
        if next_col >= 0:
            if self.Leaf_row is not None and self.Leaf_col is not None:
                if self.grid[self.agent.row][next_col] == self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = empty
                    self.agent.col = self.agent.west()
                    self.grid[self.agent.row][self.agent.col] = "Agent,leaf"
                elif self.grid[self.agent.row][self.agent.col] == "Agent,leaf":
                    self.grid[self.agent.row][self.agent.col] = "leaf"
                    self.agent.col = self.agent.west()
                    self.grid[self.agent.row][self.agent.col] = "Agent"
            elif self.grid[self.agent.row][next_col] == empty:
                self.grid[self.agent.row][self.agent.col] = empty
                self.agent.col = self.agent.west()
                self.grid[self.agent.row][self.agent.col] = "Agent"

    def agent_moving_east(self):
        if self.agent.col + 1 < len(self.grid):
            if self.Leaf_row is not None and self.Leaf_col is not None:
                if self.agent.col + 1 < len(self.grid) and self.grid[self.agent.row][self.agent.col + 1] == \
                        self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = "  0 "
                    self.agent.col = self.agent.east()
                    self.grid[self.agent.row][self.agent.col] = "Agent,leaf"

                elif self.grid[self.agent.row][self.agent.col] == self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = "leaf"
                    self.agent.col = self.agent.east()
                    self.grid[self.agent.row][self.agent.col] = "Agent"

            elif self.agent.col < 4:
                self.grid[self.agent.row][self.agent.col] = "  0 "
                self.agent.col = self.agent.east()
                self.grid[self.agent.row][self.agent.col] = "Agent"

    def agent_moving_north(self):
        if self.agent.row - 1 >= 0:
            if self.Leaf_row is not None and self.Leaf_col is not None:
                if self.agent.row - 1 < len(self.grid) and self.grid[self.agent.row - 1][self.agent.col] == \
                        self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = "  0 "
                    self.agent.row = self.agent.north()
                    self.grid[self.agent.row][self.agent.col] = "Agent,leaf"

                elif self.grid[self.agent.row][self.agent.col] == self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = "leaf"
                    self.agent.row = self.agent.north()
                    self.grid[self.agent.row][self.agent.col] = "Agent"
            else:
                self.grid[self.agent.row][self.agent.col] = "  0 "
                self.agent.row = self.agent.north() % len(self.grid)
                self.grid[self.agent.row][self.agent.col] = "Agent"

    def agent_moving_south(self):
        if self.agent.row + 1 < len(self.grid):
            if self.Leaf_row is not None and self.Leaf_col is not None:
                if self.agent.row + 1 < len(self.grid) and self.grid[self.agent.row + 1][self.agent.col] == \
                        self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = "  0 "
                    self.agent.row = self.agent.south()
                    self.grid[self.agent.row][self.agent.col] = "Agent,leaf"

                elif self.grid[self.agent.row][self.agent.col] == self.grid[self.Leaf_row][self.Leaf_col]:
                    self.grid[self.agent.row][self.agent.col] = "leaf"
                    self.agent.row = self.agent.south()
                    self.grid[self.agent.row][self.agent.col] = "Agent"
            else:
                self.grid[self.agent.row][self.agent.col] = "  0 "
                self.agent.row = self.agent.south() % len(self.grid)
                self.grid[self.agent.row][self.agent.col] = "Agent"

    def agent_playing_with_leaf_east(self):
        empty = "  0 "
        next_col = self.agent.col + 1
        if next_col < len(self.grid):
            next_cell = self.grid[self.agent.row][next_col]
            if next_cell == "leaf":
                if next_col + 1 < len(self.grid):
                    self.Leaf_col = next_col + 1
                    if self.grid[self.agent.row][next_col + 1] == empty:
                        self.grid[self.agent.row][next_col + 1] = "leaf"
                self.grid[self.agent.row][next_col] = "Agent"
                self.grid[self.agent.row][self.agent.col] = empty
                self.agent.col = next_col
                if next_col + 1 >= len(self.grid):
                    self.Leaf_col = None
                    self.Leaf_row = None

    def agent_playing_with_leaf_west(self):
        empty = "  0 "
        next_col = self.agent.col - 1
        if next_col >= 0:
            next_cell = self.grid[self.agent.row][next_col]
            if next_cell == "leaf":
                if next_col - 1 >= 0:
                    self.Leaf_col = next_col - 1
                    if self.grid[self.agent.row][next_col - 1] == empty:
                        self.grid[self.agent.row][next_col - 1] = "leaf"
                self.grid[self.agent.row][next_col] = "Agent"
                self.grid[self.agent.row][self.agent.col] = empty
                self.agent.col = next_col
                self.Leaf_col = next_col - 1
                if self.Leaf_col < 0:
                    self.Leaf_col = None
                    self.Leaf_row = None

    def agent_playing_with_leaf_south(self):
        empty = "  0 "
        next_row = self.agent.row + 1
        if next_row < len(self.grid):
            next_cell = self.grid[next_row][self.agent.col]
            if next_cell == "leaf":
                if next_row + 1 < len(self.grid):
                    self.Leaf_row = next_row + 1
                    if self.grid[next_row + 1][self.agent.col] == empty:
                        self.grid[next_row + 1][self.agent.col] = "leaf"
                self.grid[next_row][self.agent.col] = "Agent"
                self.grid[self.agent.row][self.agent.col] = empty
                self.agent.row = next_row
                if next_row + 1 >= len(self.grid):
                    self.Leaf_col = None
                    self.Leaf_row = None

    def agent_playing_with_leaf_north(self):
        empty = "  0 "
        next_row = self.agent.row - 1
        if next_row >= 0:
            # try:
            next_cell = self.grid[next_row][self.agent.col]
            if next_cell == "leaf":
                if next_row - 1 >= 0:
                    self.Leaf_row = next_row - 1
                    if self.grid[next_row - 1][self.agent.col] == empty:
                        self.grid[next_row - 1][self.agent.col] = "leaf"
                self.grid[next_row][self.agent.col] = "Agent"
                self.grid[self.agent.row][self.agent.col] = empty
                self.agent.row = next_row
                if next_row - 1 < 0:
                    self.Leaf_col = None
                    self.Leaf_row = None

    def display_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print("\n", self.agent.agent_position())
        print(" The position of the leaf is: ({}, {})".format(self.Leaf_row, self.Leaf_col))

agent = Agent()
g = GridWorld(5, 5, agent)

g.display_grid()

g.agent_moving_south()
g.display_grid()

# # Task 1.
#
# # -> We represent the leaf as a string, "leaf" and we know its location, Leaf_row, Leaf_col.
#
# # -> We call the Agent class in the Grid class.
#
# # -> The Agent will hold its own actions so the 4 base actions (north, south, east, west)
# #    but the World will decide if his actions can be done or not.In our world, all edges are bouncy.
#
# # Task 2.
#
# # -> If we say the leaf is passable, then in my design, if we pass in the location of the leaf, it will look like
# #    this: " Agent,leaf ".
#
# # -> In my design I considered the walls bouncy meaning (North, South, East and West).
#
# # Task 3.
#
# # -> For task 3, by bouncy edges in the world we mean the whole position of it so, North, West, South, East.If the
# #    leaf is in the edge of this position than it disappears, and it's position will be marked down as (None, None)
#
# # -> In my design if the leaf gets pushed over the edge, meaning pushed over the (North, South, East and West) than
# #    it is gone. The location of the Leaf will be described as (None, None) in that case.
#
# # -> To achieve this design, I'll create 4 more functions "agent_playing_with_leaf_(north, south, east, west)" that
# #    will represent this movement. We will use those special functions when the agent is near the Leaf
# #    and if we want to use the other functions meaning the ones for part 2, we can use them to move the Agent around.
#
# # -> Also note that these functions "agent_playing_with_leaf_(north, south, east, west)" are only for PUSHING the leaf
# #    and not for MOVEMENT. If you want to MOVE the Agent around,
# #    use these functions "agent_moving_(north, south, east, west)"
#
# # -> Below I'm providing the direction system for the World
# #                  North(up)
# #    West(left)                   East(right)
# #                  South(down)
#
# class Agent:
#     # Initialize the Agent with a starting position of (2, 2)
#     def __init__(self):
#         self.row = 2
#         self.col = 2
#
#     # Return the column to the left of the agent's current position
#     def west(self):
#         return self.col - 1
#
#     # Return the column to the right of the agent's current position
#     def east(self):
#         return self.col + 1
#
#     # Return the row above the agent's current position
#     def north(self):
#         return self.row - 1
#
#     # Return the row below the agent's current position
#     def south(self):
#         return self.row + 1
#
#     # Return a string indicating the agent's current position
#     def agent_position(self):
#         return f"The Agent is located at: ({self.row}, {self.col})"
#
#
# class GridWorld:
#     # Initialize the grid with specified number of rows and columns, and also place the agent and leaf in their
#     # initial locations
#     def __init__(self, rows, cols, agent):
#         # Initialize the grid with specified number of rows and columns
#         self.grid = [["  0 " for _ in range(rows)] for _ in range(cols)]
#         # Create an instance of the Agent class
#         self.agent = Agent()
#         # Place the leaf at position (2, 3)
#         self.Leaf_row = 2
#         self.Leaf_col = 3
#         # Place the agent in the grid at its initial position
#         self.grid[agent.row][agent.col] = "Agent"
#         # Place the leaf in the grid at its initial position
#         self.grid[self.Leaf_row][self.Leaf_col] = "leaf"
#
#     # Move the agent one step to the west
#     def agent_moving_west(self):
#         # Initialize a variable to represent an empty space in the grid
#         empty = "  0 "
#         # Calculate the column to the left of the agent's current position
#         next_col = self.agent.col - 1
#         # Check if the agent can move to the left (i.e., next_col is within the bounds of the grid)
#         if next_col >= 0:
#             # Check if both the agent and the leaf are present at the current position
#             if self.Leaf_row is not None and self.Leaf_col is not None:
#                 # If both the agent and the leaf are present, check if the next position to the left is the leaf
#                 if self.grid[self.agent.row][next_col] == self.grid[self.Leaf_row][self.Leaf_col]:
#                     # If the next position is the leaf, update the current position to be empty and move the agent and leaf to the left
#                     self.grid[self.agent.row][self.agent.col] = empty
#                     self.agent.col = self.agent.west()
#                     self.grid[self.agent.row][self.agent.col] = "Agent,leaf"
#                 # If the next position is not the leaf, check if the current position is the agent and leaf together
#                 elif self.grid[self.agent.row][self.agent.col] == "Agent,leaf":
#                     # If the current position is the agent and leaf together, update the current position to be the leaf and move the agent to the left
#                     self.grid[self.agent.row][self.agent.col] = "leaf"
#                     self.agent.col = self.agent.west()
#                     self.grid[self.agent.row][self.agent.col] = "Agent"
#             # If the leaf is not present at the current position, check if the next position to the left is empty
#             elif self.grid[self.agent.row][next_col] == empty:
#                 # If the next position is empty, update the current position to be empty and move the agent to the left
#                 self.grid[self.agent.row][self.agent.col] = empty
#                 self.agent.col = self.agent.west()
#                 self.grid[self.agent.row][self.agent.col] = "Agent"
#
#     def agent_moving_east(self):
#         # Check if the agent's column + 1 is within the grid bounds
#         if self.agent.col + 1 < len(self.grid):
#             # Check if the leaf location is defined
#             if self.Leaf_row is not None and self.Leaf_col is not None:
#                 # Check if the next cell in the east direction contains the leaf
#                 if self.agent.col + 1 < len(self.grid) and self.grid[self.agent.row][self.agent.col + 1] == \
#                         self.grid[self.Leaf_row][self.Leaf_col]:
#                     # Update the current cell to be empty
#                     self.grid[self.agent.row][self.agent.col] = "  0 "
#                     # Move the agent to the east
#                     self.agent.col = self.agent.east()
#                     # Update the new cell to contain the agent and the leaf
#                     self.grid[self.agent.row][self.agent.col] = "Agent,leaf"
#                 # Check if the current cell contains the leaf
#                 elif self.grid[self.agent.row][self.agent.col] == self.grid[self.Leaf_row][self.Leaf_col]:
#                     # Update the current cell to be a leaf
#                     self.grid[self.agent.row][self.agent.col] = "leaf"
#                     # Move the agent to the east
#                     self.agent.col = self.agent.east()
#                     # Update the new cell to contain the agent
#                     self.grid[self.agent.row][self.agent.col] = "Agent"
#             # Check if the agent's column is less than 4
#             elif self.agent.col < 4:
#                 # Update the current cell to be empty
#                 self.grid[self.agent.row][self.agent.col] = "  0 "
#                 # Move the agent to the east
#                 self.agent.col = self.agent.east()
#                 # Update the new cell to contain the agent
#                 self.grid[self.agent.row][self.agent.col] = "Agent"
#
#     def agent_moving_north(self):
#         # check if the new position is within the grid boundary
#         if self.agent.row - 1 >= 0:
#             # check if there's a leaf on the grid
#             if self.Leaf_row is not None and self.Leaf_col is not None:
#                 # check if the new position contains a leaf
#                 if self.agent.row - 1 < len(self.grid) and self.grid[self.agent.row - 1][self.agent.col] == \
#                         self.grid[self.Leaf_row][self.Leaf_col]:
#                     # update the current position to "0"
#                     self.grid[self.agent.row][self.agent.col] = "  0 "
#                     # move the agent to the north
#                     self.agent.row = self.agent.north()
#                     # update the new position to "Agent,leaf"
#                     self.grid[self.agent.row][self.agent.col] = "Agent,leaf"
#                 # if the new position doesn't contain a leaf
#                 elif self.grid[self.agent.row][self.agent.col] == self.grid[self.Leaf_row][self.Leaf_col]:
#                     # update the current position to "leaf"
#                     self.grid[self.agent.row][self.agent.col] = "leaf"
#                     # move the agent to the north
#                     self.agent.row = self.agent.north()
#                     # update the new position to "Agent"
#                     self.grid[self.agent.row][self.agent.col] = "Agent"
#             # if there's no leaf on the grid
#             else:
#                 # update the current position to "0"
#                 self.grid[self.agent.row][self.agent.col] = "  0 "
#                 # move the agent to the north
#                 self.agent.row = self.agent.north() % len(self.grid)
#                 # update the new position to "Agent"
#                 self.grid[self.agent.row][self.agent.col] = "Agent"
#
#     def agent_moving_south(self):
#         # If the agent's row + 1 is within the bounds of the grid
#         if self.agent.row + 1 < len(self.grid):
#             # If the Leaf's row and col have a value
#             if self.Leaf_row is not None and self.Leaf_col is not None:
#                 # If the next cell the agent is moving to is the same as the cell containing the Leaf
#                 if self.agent.row + 1 < len(self.grid) and self.grid[self.agent.row + 1][self.agent.col] == \
#                         self.grid[self.Leaf_row][self.Leaf_col]:
#                     # Update the current cell the agent was in to "0"
#                     self.grid[self.agent.row][self.agent.col] = "  0 "
#                     # Move the agent one cell south
#                     self.agent.row = self.agent.south()
#                     # Update the new cell the agent is in to "Agent,leaf"
#                     self.grid[self.agent.row][self.agent.col] = "Agent,leaf"
#                 # If the current cell the agent is in is the same as the cell containing the Leaf
#                 elif self.grid[self.agent.row][self.agent.col] == self.grid[self.Leaf_row][self.Leaf_col]:
#                     # Update the current cell the agent was in to "leaf"
#                     self.grid[self.agent.row][self.agent.col] = "leaf"
#                     # Move the agent one cell south
#                     self.agent.row = self.agent.south()
#                     # Update the new cell the agent is in to "Agent"
#                     self.grid[self.agent.row][self.agent.col] = "Agent"
#             # If the Leaf's row and col are None
#             else:
#                 # Update the current cell the agent was in to "0"
#                 self.grid[self.agent.row][self.agent.col] = "  0 "
#                 # Move the agent one cell south, wrapping around the grid if necessary
#                 self.agent.row = self.agent.south() % len(self.grid)
#                 # Update the new cell the agent is in to "Agent"
#                 self.grid[self.agent.row][self.agent.col] = "Agent"
#
#     def agent_playing_with_leaf_east(self):
#         # Initialize empty string
#         empty = "  0 "
#         # Calculate the next column for the agent
#         next_col = self.agent.col + 1
#         # Check if the next column is within the bounds of the grid
#         if next_col < len(self.grid):
#             # Get the next cell in the grid
#             next_cell = self.grid[self.agent.row][next_col]
#             # Check if the next cell is a leaf
#             if next_cell == "leaf":
#                 # Check if the next-next column is within the bounds of the grid
#                 if next_col + 1 < len(self.grid):
#                     # Update the Leaf's column
#                     self.Leaf_col = next_col + 1
#                     # Check if the next-next cell is empty
#                     if self.grid[self.agent.row][next_col + 1] == empty:
#                         # Update the next-next cell to be a leaf
#                         self.grid[self.agent.row][next_col + 1] = "leaf"
#                 # Update the next cell to be the Agent
#                 self.grid[self.agent.row][next_col] = "Agent"
#                 # Update the current cell to be empty
#                 self.grid[self.agent.row][self.agent.col] = empty
#                 # Update the Agent's column
#                 self.agent.col = next_col
#                 # Check if the next-next column is out of bounds
#                 if next_col + 1 >= len(self.grid):
#                     # Reset the Leaf's column and row
#                     self.Leaf_col = None
#                     self.Leaf_row = None
#
#     def agent_playing_with_leaf_west(self):
#         # Set empty string to "  0 "
#         empty = "  0 "
#         # Get the next column to the west
#         next_col = self.agent.col - 1
#         # Check if the next column is within the grid
#         if next_col >= 0:
#             # Get the next cell in the grid
#             next_cell = self.grid[self.agent.row][next_col]
#             # Check if the next cell is a leaf
#             if next_cell == "leaf":
#                 # Check if there is room to the west of the leaf
#                 if next_col - 1 >= 0:
#                     self.Leaf_col = next_col - 1
#                     # Check if the cell to the west of the leaf is empty
#                     if self.grid[self.agent.row][next_col - 1] == empty:
#                         # Place a leaf in the cell to the west of the leaf
#                         self.grid[self.agent.row][next_col - 1] = "leaf"
#                 # Move the agent to the leaf cell
#                 self.grid[self.agent.row][next_col] = "Agent"
#                 # Set the previous cell of the agent to be empty
#                 self.grid[self.agent.row][self.agent.col] = empty
#                 # Update the column position of the agent
#                 self.agent.col = next_col
#                 # Move the Leaf_col position to the west
#                 self.Leaf_col = next_col - 1
#                 # Check if the Leaf_col position is less than 0
#                 if self.Leaf_col < 0:
#                     # Set Leaf_col and Leaf_row to None
#                     self.Leaf_col = None
#                     self.Leaf_row = None
#
#     def agent_playing_with_leaf_south(self):
#         # The variable "empty" holds a string representation of an empty cell in the grid
#         empty = "  0 "
#         # Calculate the index of the next row
#         next_row = self.agent.row + 1
#         # Check if the next row is within the bounds of the grid
#         if next_row < len(self.grid):
#             # Get the next cell in the grid
#             next_cell = self.grid[next_row][self.agent.col]
#             # Check if the next cell contains a leaf
#             if next_cell == "leaf":
#                 # Calculate the index of the row after the next row
#                 if next_row + 1 < len(self.grid):
#                     # Update the position of the leaf to the next row after the next row
#                     self.Leaf_row = next_row + 1
#                     # Check if the cell after the next row contains an empty cell
#                     if self.grid[next_row + 1][self.agent.col] == empty:
#                         # Update the cell after the next row to contain a leaf
#                         self.grid[next_row + 1][self.agent.col] = "leaf"
#                 # Update the next cell to contain the agent
#                 self.grid[next_row][self.agent.col] = "Agent"
#                 # Update the current cell to be an empty cell
#                 self.grid[self.agent.row][self.agent.col] = empty
#                 # Update the position of the agent to be the next cell
#                 self.agent.row = next_row
#                 # Check if the next row is the last row of the grid
#                 if next_row + 1 >= len(self.grid):
#                     # Reset the position of the leaf to None
#                     self.Leaf_col = None
#                     self.Leaf_row = None
#
#     def agent_playing_with_leaf_north(self):
#         empty = "  0 "
#         next_row = self.agent.row - 1
#         if next_row >= 0:
#             # Check if the next row is within the grid
#             next_cell = self.grid[next_row][self.agent.col]
#             if next_cell == "leaf":
#                 # Check if the cell after the next row is within the grid
#                 if next_row - 1 >= 0:
#                     self.Leaf_row = next_row - 1
#                     # Check if the cell after the next row is empty
#                     if self.grid[next_row - 1][self.agent.col] == empty:
#                         self.grid[next_row - 1][self.agent.col] = "leaf"
#                 self.grid[next_row][self.agent.col] = "Agent"
#                 self.grid[self.agent.row][self.agent.col] = empty
#                 self.agent.row = next_row
#                 if next_row - 1 < 0:
#                     self.Leaf_col = None
#                     self.Leaf_row = None
#
#     def display_grid(self):
#         """
#         This function prints the current state of the grid and the current position of the agent and the leaf.
#         """
#         # loop through each row in the grid
#         for row in self.grid:
#             # join the elements of each row and separate them with a space
#             print(" ".join(row))
#         # print the current position of the agent
#         print("\n", self.agent.agent_position())
#         # print the position of the leaf
#         print(" The position of the leaf is: ({}, {})".format(self.Leaf_row, self.Leaf_col))
#         print()
#
#
# agent1 = Agent()
# grid_world = GridWorld(5, 5, agent1)
#
# grid_world.agent_moving_west()
# grid_world.display_grid()
#
# grid_world.agent_moving_north()
# grid_world.display_grid()
