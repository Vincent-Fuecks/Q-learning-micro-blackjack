import numpy as np
import pandas as pd
import enviroment
import matplotlib.pyplot as plt

HM_EPISODES = 600_000
epsilon = 0.99
EPS_DECAY = 0.99999
SHOW_EVERY = 10_000 

LEARNING_RATE = 0.001
DISCOUNT = 0.95

# q-table initialization
q_table = {}
for i in range(6):
        q_table[(i)] = [np.random.uniform(-5, 0) for i in range(2)]

episode_rewards = []

for episode in range(HM_EPISODES):
    agent = enviroment.Micro_Blackjack()

    # Shows every SHOW_EVERY episodes the epsilon value
    #if episode % SHOW_EVERY == 0:
    #    print(f"on episode {episode}, epsilon is {epsilon}")

    episode_reward = 0

    for i in range(3):
        current_state = agent.state

        if np.random.random() > epsilon:
            action = np.argmax(q_table[current_state])
        else:
            action = np.random.choice([0,1])

        reward = agent.action(action)

        # Shows every SHOW_EVERY episodes the chosen action.
        # if episode % SHOW_EVERY == 0:
        #     print(action)

        max_future_q = np.max(q_table[agent.state])
        current_q = q_table[current_state][action]

        if episode_reward == 5:
            new_q = 5
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

        q_table[current_state][action] = new_q
        episode_reward += reward

        if reward < 0 or action == 0:
            break

    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY


#################
# Visualisation #
#################
print(pd.DataFrame([[i,np.max(q_table[i][0]), np.max(q_table[i][1]), np.argmax(q_table[i])]  for i in range(5)],
                   columns = ['State', 'q-value-stopp', 'q-value-draw', 'optimal action']))

mean_of = 10_000
if not HM_EPISODES % mean_of:
    mean = [np.mean(episode_rewards[i*mean_of: (i+1)*mean_of]) for i in range(HM_EPISODES // mean_of-1)]
    x = [mean_of*i for i in range(1,HM_EPISODES // mean_of)]
    plt.title('Average reward for every 10.000 epochs')
    plt.xlabel('epochs')
    plt.ylabel('reward')
    plt.plot(x, mean)
    plt.show()
