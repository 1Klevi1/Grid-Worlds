#   Legend :
#   A -> Agent
#   L -> Leaf

# 1. So in this design, if the agent perceives the "Goal" and also the other labels in the field

# 2. if the agent goes to the leaf location, it will look like this "A,L" and a message  will be printed like this:
#    "Agent picked up the leaf". If u move the Agent again, the leaf will stay still in her position.

# 3. if you follow the labels then the Agent will achieve the "Goal" and the "Goal" will be still there if you move from
#    its location and go to another field. Note: when the Agent goes to the "Goal", you will only see the "Goal" shown.
#    For task 2/3 we can use the function "mini_controller" and for Task 4 we can use the function "random_walk"
# To move the Agent in the world you would need to type this string element in "LOWERcase" inside the "agent_moving()"
#    function , if it's uppercase it won't work:
#    "north", "south", "east", "west"
# -> Below I'm providing the direction system for the World
#                        North(up) - Bouncy
#    West(left) - Bouncy                      East(right) - Bouncy
#                        South(down) - Bouncy

# To check Task 4, you will need to comment the code for task 3, "g.mini_controller() " or vice versa
# because the Agent would have achieved the "Goal" in that case, so you won't notice if it works or not :)
import random


class Agent:
    # Initializes an instance of the Agent class.
    def __init__(self):
        # Sets the starting position of the agent to [2, 2].
        self.pos = [2, 2]
        # Creates a 2D list representing the world with a goal at the top left.
        self.world_goal = [
            ["Goal", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
        ]
        # Creates a 2D list representing the directions the agent can move in the world.
        self.world_direction = [
            ["", "west", "west", "west", "west"],
            ["north", "west", "west", "east", "north"],
            ["north", "east", "north", "west", "north"],
            ["north", "east", "east", "south", "north"],
            ["north", "west", "west", "east", "north"],
        ]

    # Returns the goal at the current position of the agent.
    def perceive_goal(self):
        return self.world_goal[self.pos[0]][self.pos[1]]

    # Returns the direction the agent can move at the current position.
    def perceive_direction(self):
        return self.world_direction[self.pos[0]][self.pos[1]]

    # Returns a tuple containing the goal and direction at the current position.
    def perceive(self):
        return self.perceive_goal(), self.perceive_direction()

    # Updates the position of the agent based on the specified action and returns the new perception.
    def move(self, action):
        # Updates the position of the agent based on the specified action.
        if action == "north":
            self.pos[0] = max(self.pos[0] - 1, 0)
        elif action == "south":
            self.pos[0] = min(self.pos[0] + 1, 4)
        elif action == "west":
            self.pos[1] = max(self.pos[1] - 1, 0)
        elif action == "east":
            self.pos[1] = min(self.pos[1] + 1, 4)
        # Returns the new perception at the updated position.
        return self.perceive()


class World:
    def __init__(self, agent):
        # Define the empty string
        self.empty = "  0 "
        # Define a message variable
        self.message = ""
        # Save the agent as an instance variable
        self.agent = agent
        # Define strings to represent the agent, leaf, goal and both agent and leaf
        self.agent_str = "  A "
        self.leaf_str = "  L "
        self.goal_str = "Goal"
        self.agent_and_leaf = "A,L"
        # Create a 5x5 grid with empty strings
        self.grid = [[self.empty for _ in range(5)] for _ in range(5)]
        # Set the initial row and column for the leaf
        self.Leaf_row = 2
        self.Leaf_col = 3
        # Place the goal in the top-left corner of the grid
        self.grid[0][0] = self.goal_str
        # Place the agent in the grid at its initial position
        self.grid[self.agent.pos[0]][self.agent.pos[1]] = self.agent_str
        # Place the leaf in the grid at its initial position
        self.grid[self.Leaf_row][self.Leaf_col] = self.leaf_str

    def agent_moving(self, action):
        # Clear the current position of the agent in the grid
        self.grid[self.agent.pos[0]][self.agent.pos[1]] = self.empty

        # Move the agent based on the given action and perceive its new state
        percept = self.agent.move(action)

        # If the agent reaches the goal, update the grid and message accordingly
        if percept[0] == self.goal_str:
            self.grid[self.agent.pos[0]][self.agent.pos[1]] = self.goal_str
            self.message = "Agent achieved the goal!"

        # If the agent doesn't reach the goal, update the grid with its new position
        else:
            # Update the grid with the new position of the agent
            self.grid[self.agent.pos[0]][self.agent.pos[1]] = self.agent_str

            # Place the leaf in the grid, in her position again
            self.grid[self.Leaf_row][self.Leaf_col] = self.leaf_str

            # Place the Goal in the grid, in her position again
            self.grid[0][0] = self.goal_str
            self.message = ""

            # If the agent picks up the leaf, update the grid and message accordingly
            if (
                self.grid[self.agent.pos[0]][self.agent.pos[1]]
                == self.grid[self.Leaf_row][self.Leaf_col]
            ):
                self.grid[self.agent.pos[0]][self.agent.pos[1]] = self.agent_and_leaf
                self.message = "Agent picked up the leaf"

    # Task 2 and 3 -> Using labels
    def mini_controller(self):
        # Print statement to indicate starting of function
        print("Starting mini_controller", "\n")

        # While loop to keep running the controller until goal is achieved
        while self.agent.perceive_goal() != "Goal":
            # Perceive the current state of the agent
            label = self.agent.perceive()

            # Check if agent has reached the goal
            if label[0] == self.goal_str:
                # Update message and display the grid
                self.message = "Agent achieved the goal!"
                self.display_grid()

            # If goal not achieved, move the agent and update the grid
            else:
                self.agent_moving(label[1])
                self.display_grid()

    # Task 4 Random Walk
    def random_walk(self):
        # Print statement to indicate starting of function
        print("Starting random walk", "\n")

        # List of possible movements for the agent
        movement_list = ["east", "south", "north", "west"]

        # While loop to keep running random walk until goal is achieved
        while self.agent.perceive_goal() != "Goal":
            # Perceive the current state of the agent
            label = self.agent.perceive()
            # Check if agent has reached the goal
            if label[0] == self.goal_str:
                # Update message and display the grid
                self.message = "Agent achieved the goal!"
                self.display_grid()

            # If goal not achieved, move the agent randomly and update the grid
            else:
                self.agent_moving(random.choice(movement_list))
                self.display_grid()

    def display_grid(self):
        """
        This function prints the current state of the grid and the current position of the agent and the leaf.
        """
        # loop through each row in the grid
        for row in self.grid:
            # join the elements of each row and separate them with a space
            print(" ".join(row))
        # print the field label
        print("\n", "The field label that agents see is: ", self.agent.perceive())
        # print the position of the leaf
        print("", self.message, "\n")


# Create a new agent instance and a new world instance with the agent
agent = Agent()
g = World(agent)

# Display the initial state of the world grid
g.display_grid()

# Move the agent east and then south, updating and displaying the grid after each move
g.agent_moving("east")
g.display_grid()

g.agent_moving("south")
g.display_grid()

# Task 2 and 3 -> Using labels
g.mini_controller()
# # Task 4 -> Random Walk
g.random_walk()
