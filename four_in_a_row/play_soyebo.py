import imp
from re import L
import sys
from turtle import down

from numpy import obj2sctype


sys.path.insert(1,'/Users/emma/dev/Reinforcement_learning_projects/')
from PPO.agents import Agent 
from environment import ENV
from PPO.memory import Mem

def flip_flop(player_number):
    if player_number ==1 :
        return  2
    else: return 1
if __name__ == '__main__':
    env = ENV()
    
    player_number = 1
   
    batch_size = 5 
    n_epochs = 2
    alpha = 0.0003

    agent = Agent( n_actions = 7 , batch_size = batch_size, alpha = alpha,\
        model_name_actor = "four_in_row_actor", model_name_critic = "four_in_row_critic",\
        n_epoch = n_epochs, input_dims = (42,))
    agent.load_model()
    observation = env.reset()
    done = False

    
   
    while not done:
            if player_number == 2:
                action  = agent.play_with_model(observation = observation)
                print("action chosen was")
                new_observation, reward1 , reward2 ,done  = env.play(player_number = player_number, move = action)
             
            else:
                move_col = input("the row you wish to play on :")
                move_col = int(move_col)
                new_observation, reward1 , reward2 ,done  = env.play(player_number = player_number, move = move_col)
            env.print_board()
            player_number = flip_flop(player_number)
            

        # agent.remember(observation,  action, prob, val, reward1, done)

        # play the old model now
           
        