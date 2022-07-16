import imp
from re import L
import sys
from turtle import down


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

    n_games = 50
    cache = []
    for i in range(n_games):
        observation = env.reset()
        done = False
        # lets randomly make a first move to make the game as random as possible
        import random
        random_first_move = random.randint(0,1)
        player_number = 1
        if random_first_move == 1: # we should randomise  and not use model
            move = random.randint(0,6)
            #then we take the move
            observation, reward1 , reward2 ,done = env.play(player_number = 1, move = move)
            player_number = 2

            # we also decide if we should use secound model
            random_secound_move = random.randint(0,1)

            if random_secound_move == 1:
                move = random.randint(0,6)
                observation, reward1 , reward2 ,done = env.play(player_number = 1, move = move)
                player_number = 1


        

        while not done:
            action , prob, val = agent.choose_action(observation = observation)
            new_observation, reward1 , reward2 ,done  = env.play(player_number = player_number, move = action)
            player_number = flip_flop(player_number)
            
            cache.append(Mem(state = observation, prob = prob, val = val,\
                 action = action, reward = reward1, done = done))

            if reward1 != 0 and len(cache)>=2:
                cache[-2].reward = reward2
                cache[-2].done = done
            observation = new_observation
        # append the memory here to use
        for m in cache:
            agent.remember(state = m.state,  action = m.action, \
                probs = m.prob, vals = m.val, reward= m.reward, done = m.done)
        agent.learn()
    agent.save_models()

        # agent.remember(observation,  action, prob, val, reward1, done)

        # play the old model now
           
        