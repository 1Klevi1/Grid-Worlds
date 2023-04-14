import copy
import random

# Defining the Agent class
class Agent:

    # Initializing the Agent class with a random position, world and goal
    def __init__(self):

        # Generating random numbers for the x and y coordinates
        self.x = random.randint(0, 5)
        self.y = random.randint(0, 3)

        # Setting energy_meter
        self.energy_meter = 4

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

        # Update the position of the Agent based on the specified action, -1 energy_meter for each action taken
        if action == "north":
            self.agent_pos[0] = max(self.agent_pos[0] - 1, 0)
            self.energy_meter -= 1
        elif action == "south":
            self.agent_pos[0] = min(self.agent_pos[0] + 1, 5)
            self.energy_meter -= 1
        elif action == "west":
            self.agent_pos[1] = max(self.agent_pos[1] - 1, 0)
            self.energy_meter -= 1
        elif action == "east":
            self.agent_pos[1] = min(self.agent_pos[1] + 1, 3)
            self.energy_meter -= 1
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


class World:

    # Initialize the class with the following attributes
    def __init__(self, agent):

        # Set the eat attribute to None
        self.eat = None

        # Set the action attribute to ""
        self.action = ""

        # Set the episode_dict attribute to {}
        self.episode_dict = {}

        # Set the states_used attribute to {}
        self.states_used = dict()

        # Set the world_stored attribute to []
        self.world_stored = []

        # Set the count attribute to 0
        self.count = 0

        # Set the count_world attribute to 0
        self.count_world = 0

        # Set the world_stored_copy attribute to []
        self.world_stored_copy = []

        # Set the count_episodes attribute to 0
        self.count_episodes = 0

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
        self.action = action
        # Call the eat_food method from the agent class and assign its value to self.eat
        self.eat = self.agent.eat_food(eat)

        # Check if agent eats food
        if self.eat:

            # Check if agent is on a food item
            if tuple(self.agent.agent_pos) in self.food_pos:
                # Increment length, remove food item from food_pos, and update world
                self.food_pos.remove(tuple(self.agent.agent_pos))
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.empty
                self.agent.move(action)
                self.world[self.agent.agent_pos[0]][
                    self.agent.agent_pos[1]
                ] = self.agent_str

            # Agent is not on food item
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

            # Agent is not on food item
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

        while True:

            # Define available actions
            actions = ["north", "south", "west", "east"]

            # Call the eat_food method from the agent class and assign its value to self.eat
            self.eat = self.agent.eat_food(True)

            # Check if agent has reached the goal
            if self.agent.on_goal():
                print("God said: No more movements, Agent reached the GOAL :D !!!")
                break
            if self.agent.energy_meter == 0:
                print(
                    "God said: No more movements, Agent run out of energy. Is he getting old or what ;) ?! "
                )
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
                            self.action = direction
                            # Move agent to the food item and update eat variable
                            self.length += 1
                            self.agent.energy_meter += 5
                            self.agent_moving(direction, True)
                            self.eat = True
                            break
            else:
                self.action = random.choice(actions)
                # Choose a random action and update the world
                self.agent_moving(self.action, True)
            # Display the updated world
            self.display_grid()

    def reset_world(self):

        # Create a deepcopy of world_stored and assign it to world_stored_copy
        self.world_stored_copy = copy.deepcopy(self.world_stored)

        # Set the length attribute to 0
        self.length = 0

        # Set the count attribute to 0
        self.count = 0

        # Set the agent.energy_meter attribute to 4
        self.agent.energy_meter = 4

        # Set the action attribute to ""
        self.action = ""

        # Set the eat attribute to be the same as the original world
        self.eat = self.world_stored_copy[0]["world0"][0]["Eat :"]

        # Set the world attribute to be the same as the original world
        self.world = [[self.empty for _ in range(4)] for _ in range(6)]

        # Set the agent.agent_pos attribute to be the same as the original world
        self.agent.agent_pos = self.world_stored_copy[0]["world0"][0]["agent pos: "]
        self.agent_pos = self.agent.agent_pos
        self.world[self.agent.agent_pos[0]][self.agent.agent_pos[1]] = self.agent_str
        self.world[self.goal_pos[0]][self.goal_pos[1]] = self.goal_str

        # Set the food_pos attribute to be the same as the original world
        self.food_pos = self.world_stored_copy[0]["world0"][0]["food pos: "]

        # Place the 10 food items on the world
        for _, pos in enumerate(self.food_pos):
            self.world[pos[0]][pos[1]] = self.food_str

        self.agent.set_world(self.world)
        self.agent.set_goal(self.goal_pos)

    def display_grid(self):
        """
        This function prints the current state of the grid and the current position of the agent and the food
        """
        # loop through each row in the grid
        for row in self.world:

            # join the elements of each row and separate them with a space
            print(" ".join(row))

        # a list of keys for the dictionary states_used
        keys = [
            "count: ",
            "Eat :",
            "agent pos: ",
            "food pos: ",
            "Nearby food: ",
            "Is it on Goal: ",
            "Energy meter: ",
            "Agent moved: ",
        ]
        # creating a copy of agent_pos, because we don't want to change
        agent_pos_copy = self.agent_pos.copy()

        # creating a copy of food_pos, because we don't want to change
        food_pos_copy = self.food_pos.copy()

        # a list of values for the dictionary states_used
        values = [
            self.length,
            self.eat,
            agent_pos_copy,
            food_pos_copy,
            self.agent.nearby_food(),
            self.agent.on_goal(),
            self.agent.energy_meter,
            self.action,
        ]

        # Checks if agent is on_goal or energy_meter = 0
        if self.agent.on_goal() or self.agent.energy_meter == 0:

            # store the current episode
            self.episode_dict[self.count] = dict(self.states_used)

            # Storing it in a list, while creating a dictionary inside it for the worlds
            self.world_stored.append(
                {"world" + str(self.count_world): dict(self.episode_dict)}
            )

            # Resetting episode_dict to {}
            self.episode_dict = {}

            # Increasing count_world +1
            self.count_world += 1

            # Resetting count to 0
            self.count = 0
        else:

            # Creates a dictionary out of 2 lists, keys and values
            self.states_used = {k: v for k, v in zip(keys, values)}

            # updating the episode_dict, the key is count and the value is another dictionary states_used
            self.episode_dict[self.count] = dict(self.states_used)

            # Increasing count +1
            self.count += 1

            # count_episodes will store the value of count
            self.count_episodes = self.count

        print("count: ", self.length)
        print("Eat :", self.eat)
        print("agent pos: ", self.agent.agent_pos)
        print("food pos: ", self.food_pos)
        print("Nearby food: ", self.agent.nearby_food())
        print("Is it on Goal: ", self.agent.on_goal())
        print("Energy meter: ", self.agent.energy_meter)
        print("Agent moved: ", self.action)
        print("", self.message, "\n")


a = Agent()
w = World(a)
w.display_grid()
w.choose_action()

# Empty list for the test_runs
test_runs = []

# Temporary dict2 to store the average actions
dict2 = {}

# Dictionary to store the actions for all 10 runs
avg_actions = {}
print("World Dictionary: ", w.world_stored)
# 10 Test run
count_north = 0
count_south = 0
count_west = 0
count_east = 0
for i in range(10):
    print(f"Run: {i}")
    w.reset_world()
    w.display_grid()
    w.choose_action()

    # increases the counts if it finds ["north", "south", "west", "east"]
    for j in range(len(w.world_stored[i + 1]["world" + str(i + 1)])):
        if "Agent moved: " in w.world_stored[i + 1]["world" + str(i + 1)][j]:
            if (
                "north"
                in w.world_stored[i + 1]["world" + str(i + 1)][j]["Agent moved: "]
            ):
                count_north += 1
            if (
                "south"
                in w.world_stored[i + 1]["world" + str(i + 1)][j]["Agent moved: "]
            ):
                count_south += 1
            if (
                "west"
                in w.world_stored[i + 1]["world" + str(i + 1)][j]["Agent moved: "]
            ):
                count_west += 1
            if (
                "east"
                in w.world_stored[i + 1]["world" + str(i + 1)][j]["Agent moved: "]
            ):
                count_east += 1

    avg_north = (w.agent.energy_meter / w.count_episodes) * count_north
    avg_south = (w.agent.energy_meter / w.count_episodes) * count_south
    avg_west = (w.agent.energy_meter / w.count_episodes) * count_west
    avg_east = (w.agent.energy_meter / w.count_episodes) * count_east

    dict2["avg_north"] = avg_north
    dict2["avg_south"] = avg_south
    dict2["avg_west"] = avg_west
    dict2["avg_east"] = avg_east

    # updates avg_actions with a key i, and value another dict dict2
    avg_actions[i] = dict(dict2)

    test_runs.append(
        f"< Run {i} - World{i + 1} - Energy meter: {w.agent.energy_meter} - Is on Goal:"
        f" {w.agent.on_goal()} - Number of episodes: {w.count_episodes} "
        f"- Average Reward: {w.agent.energy_meter / w.count_episodes}"
        f" - north: {count_north} - Avg({(w.agent.energy_meter / w.count_episodes) * count_north}), "
        f"south: {count_south} - Avg({(w.agent.energy_meter / w.count_episodes) * count_south}),"
        f" west: {count_west} - Avg({(w.agent.energy_meter / w.count_episodes) * count_west}), "
        f"east: {count_east} - Avg({(w.agent.energy_meter / w.count_episodes) * count_east}) >"
    )

    # Resets everything to 0
    count_north = 0
    count_south = 0
    count_west = 0
    count_east = 0

print()
print("< 10 Test runs >")
print()
print("\n".join(test_runs))
print()

# create new variable
sum_north = 0
sum_south = 0
sum_west = 0
sum_east = 0

# loop through the dictionary avg_actions
for key in avg_actions:
    sum_north += avg_actions[key]["avg_north"]
    sum_south += avg_actions[key]["avg_south"]
    sum_west += avg_actions[key]["avg_west"]
    sum_east += avg_actions[key]["avg_east"]
print("< Average over all 10 runs >")
print()
print("Sum of avg_north:", sum_north)
print("Sum of avg_south:", sum_south)
print("Sum of avg_west:", sum_west)
print("Sum of avg_east:", sum_east)
print()
print("World Dictionary: ", w.world_stored)
