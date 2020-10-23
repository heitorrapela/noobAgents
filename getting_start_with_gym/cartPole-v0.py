import gym

debug = False
env_number = 0
choose_env = ["CartPole-v0", "MountainCar-v0", "MsPacman-v0", "Hopper-v1"]

env = gym.make(choose_env[env_number])

print(env.action_space)

print(env.observation_space)

print(env.observation_space.high)
print(env.observation_space.low)

for i_episode in range(20):
	observation = env.reset()

	for t in range(100):
		env.render()
		observation, reward, done, info = env.step(env.action_space.sample())
		
		if debug:
			print("Observation: ", observation)
			print("Reward: ", reward)
			print("Done: ", done)
			print("Info: ", info)

		if done:
			print("Episode finished after {} timesteps".format(t+1))
			break

env.close()


