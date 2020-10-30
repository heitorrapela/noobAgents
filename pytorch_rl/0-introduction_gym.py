import matplotlib.pyplot as plt
import numpy as np
import gym

print(gym.__version__)

all_envs = gym.envs.registry.all()
envs_ids = [env.id for env in all_envs]

print(f'There are {len(envs_ids)} gym environments. Such as {envs_ids[:12]}')

env = gym.make("CartPole-v1")

print("observation space is: ", env.observation_space)

print("is observation space discrete?", isinstance(env.observation_space, gym.spaces.Discrete))
print("is observation space continuous?", isinstance(env.observation_space, gym.spaces.Box))

print("observation space shape: ", env.observation_space.shape)

print("observation space high values?", env.observation_space.high)
print("observation space low values?", env.observation_space.low)

print("action space is:", env.action_space)

print("is action space discrete?", isinstance(env.action_space, gym.spaces.Discrete))
print("is action space continuous?", isinstance(env.action_space, gym.spaces.Box))

print("action space shape: ", env.action_space.n)

print(env.spec.max_episode_steps)
print(env.spec.reward_threshold)
print(env.spec.nondeterministic)
