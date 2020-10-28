import matplotlib.pyplot as plt
import numpy as np
import gym

print(gym.__version__)

all_envs = gym.envs.registry.all()
envs_ids = [env.id for env in all_envs]

print(f'There are {len(envs_ids)} gym environments. Such as {envs_ids[:12]}')
