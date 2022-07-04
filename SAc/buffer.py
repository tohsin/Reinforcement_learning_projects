import numpy as np
from numpy.core.defchararray import index
class ReplayBuffer:
    def __init_(self,max_size,input_shape,n_actions):
        self.mem_size=max_size
        self.mem_cntr=0
        self.state_memory=np.zeros((self.mem_size,*input_shape))
        self.new_state_memory=np.zeros((self.mem_size,*input_shape))
        self.action_memory=np.zeros((self.mem_size,n_actions))
        self.reward_memory=np.zeros(self.mem_size)
        self.terminal_memory=np.zeros(self.mem_size,dtype=np.bool)
        
    def store_transactions(self,state,action,reward,state_,done):
        index=self.mem_cntr%self.mem_size
        
        self.state_memory[index]=state
        self.new_state_memory[index]=state_
        self.action_memory[index]=action
        self.reward_memory[index]=reward
        self.terminal_memory[index]=done
        
        self.mem_cntr+=1
    def sample_buffer(self,batch_size):
        max_men=min(self.mem_cntr,self.mem_size) 
         #sample randomly from 0 to max_men of size batch_size   
        batch=np.random.choice(max_men,batch_size)   
        state=self.new
        
        
    