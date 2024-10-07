import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

# Step 1: Create the CartPole environment
env = gym.make('CartPole-v1')
nb_actions = env.action_space.n  # number of actions (left or right)

# Step 2: Build a deep Q-network (DQN) model
def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

# Step 3: Define the agent's policy, memory, and DQN agent
def build_agent(model, actions):
    policy = EpsGreedyQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

states = env.observation_space.shape[0]
actions = env.action_space.n

model = build_model(states, actions)
dqn = build_agent(model, actions)

# Step 4: Compile the DQN agent
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# Step 5: Train the DQN agent
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

# Step 6: Test the trained agent
dqn.test(env, nb_episodes=5, visualize=True)