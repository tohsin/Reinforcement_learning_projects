from turtle import shape
import gym
import numpy as np
from agents import Agent
from actor import ActorNetwork
from critic import CriticNetwork
from utils import plot_learning_curve
if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    N = 20
    batch_size = 5 
    n_epochs = 4 
    alpha = 0.0003
    shape_ = env.observation_space.shape
    print("shape")

    print(shape_)
    
    # agent = Agent( n_actions=env.action_space.n, batch_size=batch_size, alpha=alpha,\
    #     n_epoch= n_epochs, input_dims = env.observation_space.shape)
    # n_games = 300
    # figure_file = 'PPO_algorithm/plots/cartpole.png'
    # best_score = env.reward_range[0]
    # score_history = []
    # n_steps = 0
    # learn_iters = 0
    # avg_score = 0

    # for i in range(n_games):
    #     observation = env.reset()
    #     done = False
    #     score = 0
    #     while not done:
    #         action, prob, val = agent.choose_action(observation)
            
    #         observation_, reward, done, info = env.step(action)
    #         n_steps+=1
    #         score+=reward
    #         agent.remember(observation,  action, prob,val, reward, done)
    #         if n_steps%N ==0:
    #             agent.learn()
    #             learn_iters+=1
    #         observation = observation_
    #     score_history.append(score)
    #     avg_score = np.mean(score_history[-100:])

    #     if avg_score>best_score:
    #         best_score= avg_score
    #         agent.save_models()
    #     print('episode', i , 'score %.1f', 'avg_score %.1f' %avg_score,
    #     'time_steps',n_steps, 'learning_steps', learn_iters)

    # x = [i+1 for i in range(len(score_history))]
    # plot_learning_curve(x, score_history,figure_file)