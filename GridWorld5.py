# So this design has 2 main functions to move the agent around, the first one is agent_moving and
# choose_action.With the agent_moving function, the Agent can decide if he wants to eat or not. With the
# other function, choose_action, the agent can move using his "decision making". We have also created a variable
# to count how many foods the Agent is eating, the count works, it displays the correct result but it has a delay of 1 s

# Also the agent_moving function does not stop when it's on Goal, there is no specification saying that, but the
# function choose_action has the ability to stop


# -> Below I'm providing the direction system for the World
#                        North(up) - Bouncy
#    West(left) - Bouncy                      East(right) - Bouncy
#                        South(down) - Bouncy


# Importing the random module to generate random numbers
import random


# Defining the Agent class
class Agent:

    # Initializing the Agent class with a random position, world and goal
    def __init__(self):

        # Generating random numbers for the x and y coordinates
        self.x = random.randint(0, 5)
        self.y = random.randint(0, 3)

        # Creating a list to hold the x and y coordinates
        self.agent_pos = [self.x, self.y]

        # Initializing the world and goal to None
        self.world = None
        self.goal_pos = None

    # Method to set the world for the Agent
    def set_world(self, world):
        self.world = world

    # Method to set the goal for the Agent
    def set_goal(self, goal):
        self.goal_pos = goal

    # Method to move the Agent based on the specified action
    def move(self, action):

        # Check if the Agent should move or not, 50% of the time nothing happens instead. 50% the
        # movement happens.
        if random.random() < 0.5:
            return

        # Update the position of the Agent based on the specified action
        if action == "north":
            self.agent_pos[0] = max(self.agent_pos[0] - 1, 0)
        elif action == "south":
            self.agent_pos[0] = min(self.agent_pos[0] + 1, 5)
        elif action == "west":
            self.agent_pos[1] = max(self.agent_pos[1] - 1, 0)
        elif action == "east":
            self.agent_pos[1] = min(self.agent_pos[1] + 1, 3)
        else:
            # If an invalid action is passed, raise an error.
            raise ValueError("Invalid action: {}".format(action))

    # Method to eat food
    def eat_food(self, action):
        return action

    # Method to check if there is food nearby
    def nearby_food(self):

        # Creating a list of food positions
        food_positions = [
            (self.agent_pos[0], self.agent_pos[1] + 1),
            (self.agent_pos[0], self.agent_pos[1] - 1),
            (self.agent_pos[0] + 1, self.agent_pos[1]),
            (self.agent_pos[0] - 1, self.agent_pos[1]),
            (self.agent_pos[0], self.agent_pos[1]),
        ]

        # Checking if there is food nearby
        for x, y in food_positions:
            if 0 <= x <= 5 and 0 <= y <= 3:
                if self.world[x][y] == "FOOD":
                    return True
        return False

    # Method to check if the Agent is on the goal
    def on_goal(self):

        # Checking if the Agent is on the goal
        if (
            self.world[self.agent_pos[0]][self.agent_pos[1]]
            == self.world[self.goal_pos[0]][self.goal_pos[1]]
        ):
            return True
        else:
            return False


# Define a class called World
class World:

    # Initialize the class with the following attributes
    def __init__(self, agent):

        # Set the eat attribute to None
        self.eat = None

        # Set the empty attribute to "ooooo"
        self.empty = "ooooo"

        # Create a 6x4 world of empty spaces using nested lists
        self.world = [[self.empty for _ in range(4)] for _ in range(6)]

        # Set the agent attribute to the input agent
        self.agent = agent

        # Set the message attribute to an empty string
        self.message = ""

        # Set the length attribute to 0
        self.length = 0

        # Set the agent_str attribute to "AGENT"
        self.agent_str = "AGENT"

        # Set the food_str attribute to "FOOD"
        self.food_str = "FOOD"

        # Set the goal_str attribute to "GOAL"
        self.goal_str = "GOAL"

        # Generate random coordinates for the goal position that are not equal to the agent's starting position
        while True:
            self.goal_x = random.randint(0, 5)
            self.goal_y = random.randint(0, 3)
            if (self.goal_x, self.goal_y) != tuple(self.agent.agent_pos):
                break

        # Set the goal_pos attribute to the generated goal coordinates
        self.goal_pos = [self.goal_x, self.goal_y]

        # Generate a starting position for the agent that is not equal to the goal position
        while True:
            if tuple(self.agent.agent_pos) != tuple(self.goal_pos):
                break

        # Set the agent_pos attribute to the generated agent position
        self.agent_pos = self.agent.agent_pos

        # Update the world with the goal, agent, and food positions
        self.world[self.agent_pos[0]][self.agent_pos[1]] = self.agent_str
        self.world[self.goal_pos[0]][self.goal_pos[1]] = self.goal_str
        self.used_pos = [tuple(self.agent_pos), tuple(self.goal_pos)]
        self.food_pos = []

        # Generate unique positions for 10 food items
        for _ in range(10):
            while True:
                food_x = random.randint(0, 5)
                food_y = random.randint(0, 3)
                if (food_x, food_y) not in self.used_pos:
                    self.used_pos.append((food_x, food_y))
                    self.food_pos.append((food_x, food_y))
                    break

        # Place the 10 food items on the world
        for _, pos in enumerate(self.food_pos):
            self.world[pos[0]][pos[1]] = self.food_str

        # Set the agent's world and goal attributes to the updated world and goal position, respectively
        self.agent.set_world(self.world)
        self.agent.set_goal(self.goal_pos)

    def agent_moving(self, action, eat):

        # Call the eat_food method from the agent class and assign its value to self.eat
        self.eat = self.agent.eat_food(eat)

        # Check if agent eats food
        if self.eat:

            # Check if agent is on a food item
            if tuple(self.agent.agent_pos) in self.food_pos:

                # Increment length, remove food item from food_pos, and update world
                if self.eat:
                    self.length += 1
                    self.food_pos.remove(tuple(self.agent.agent_pos))
                    self.world[self.agent.agent_pos[0]][
                        self.agent.agent_pos[1]
                    ] = self.empty
                    self.agent.move(action)
                    self.world[self.agent.agent_pos[0]][
                        self.agent.agent_pos[1]
                    ] = self.agent_str

            # Agent is not on a food item
            else:

                # Update world with empty space, move agent, and update world again
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.empty
                self.agent.move(action)
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.agent_str

        # Agent does not eat food
        else:

            # Check if agent is on a food item
            if tuple(self.agent.agent_pos) in self.food_pos:

                # Update world with food item, move agent, and update world again
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.food_str
                self.agent.move(action)
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.agent_str

            # Agent is not on a food item
            else:

                # Update world with empty space, move agent, and update world again
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.empty
                self.agent.move(action)
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.agent_str

    def choose_action(self):

        # Loop until agent reaches the goal or there are no more movements
        while True:

            # Define available actions
            actions = ["north", "south", "west", "east"]

            # Call the eat_food method from the agent class and assign its value to self.eat
            self.eat = self.agent.eat_food(True)

            # Check if agent has reached the goal
            if self.agent.on_goal():
                print("No more movements, Agent reached the GOAL !!!")
                break

            # Check if there is nearby food
            if self.agent.nearby_food():

                # Define positions of food items around the agent
                food_positions = [
                    (self.agent.agent_pos[0], self.agent.agent_pos[1] + 1, "east"),
                    (self.agent.agent_pos[0], self.agent.agent_pos[1] - 1, "west"),
                    (self.agent.agent_pos[0] + 1, self.agent.agent_pos[1], "south"),
                    (self.agent.agent_pos[0] - 1, self.agent.agent_pos[1], "north"),
                ]

                # Loop through the food positions
                for x, y, direction in food_positions:

                    # Check if position is valid and has a food item
                    if 0 <= x <= 5 and 0 <= y <= 3:
                        if self.world[x][y] == "FOOD":

                            # Move agent to the food item and update eat variable
                            self.agent_moving(direction, True)
                            self.eat = True
                            break
            else:

                # Choose a random action and update the world
                self.agent_moving(random.choice(actions), True)

            # Display the updated world
            self.display_grid()

    def display_grid(self):
        """
        This function prints the current state of the grid and the current position of the agent and the food
        """
        # loop through each row in the grid
        for row in self.world:
            # join the elements of each row and separate them with a space
            print(" ".join(row))
        print("count: ", self.length)
        print("Eat :", self.eat)
        print("agent pos: ", self.agent.agent_pos)
        print("food pos: ", self.food_pos)
        print("Nearby food: ", self.agent.nearby_food())
        print("Is it on Goal: ", self.agent.on_goal())
        print("", self.message, "\n")


a = Agent()
w = World(a)
w.display_grid()
# Test 1 -> Decision making, comment Test 2
w.choose_action()

# Test 2 -> Agent using the function agent_move showing it's choice to eat or not the food, comment Test 1
# for i in range(7):
#     w.agent_moving("north", True)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("west", True)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("east", True)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("south", False)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("north", False)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("west", False)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("south", False)
#     w.display_grid()
# for i in range(7):
#     w.agent_moving("east", True)
#     w.display_grid()
