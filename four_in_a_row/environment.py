class ENV:
    def __init__(self) -> None:
        self.number_rows = 6
        self.number_columns = 7
        self.board = []
        for _ in range(self.number_rows):
            self.board.append([0]* self.number_columns )
        self.diag_1_cache = {}
        self.diag_2_cache = {}

    def get_observation(self):
        obs = []
        for row in self.board:
            obs.extend(row)
        return obs
    
    def reset(self):
        self.board = [] # reset board state

        for _ in range(self.number_rows):
            self.board.append([0]* self.number_columns ) 
        self.diag_1_cache = {}
        self.diag_2_cache = {}
        return self.get_observation()
        
    def print_board(self):
        print("board")
       
        for i in range(len(self.board)): print(self.board[i])
    
    def can_play(self,move):
        #if position of move is zero then move is valid else 
        #game is illegal and also lost
        return self.board[0][move] == 0
    
    def play(self, player_number, move): # move  is a column

        for i in range(len(self.board)-1, -1 , -1): # loop through rows
            # print(i,move)

            if self.board[i][move] == 0:   # if row , column is not zero

                self.board[i][move] = player_number
                # make changes to diagonals
                diag1_var = i + move # embedding for diagonal 1 y + x
                diag2_var = i - move + 7 # embedding for diagonal 2 y - x + n + 1

                if diag1_var not in self.diag_1_cache: # if embedding doesnt exist add to cache
                    self.diag_1_cache[diag1_var]= []

                if diag2_var not in self.diag_2_cache:
                    self.diag_2_cache[diag2_var] = []

                self.diag_1_cache[diag1_var].append(player_number)
                self.diag_2_cache[diag2_var].append(player_number)

               
                
                if not self.can_play(move=move):
                    print("cant move there")
                    return  self.get_observation(), -1 , 1 ,  True
                if self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 and self.board[0][3] != 0 and \
                    self.board[0][4] != 0 and  self.board[0][5] != 0 and self.board[0][6] != 0: # if all the spots are filled 
                    #game is a draw no valid move no valid winner
                    print("no valid move game over")
                    return self.get_observation(), 0 , 0 ,  True

                if self.game_over(i, move):
                    #game is over current player wins 
                    print("player wins")
                    return self.get_observation(), 1, -1, True  # state, reward, done
                else:
                    # game isnt over
                    return self.get_observation(),0, 0, False  #stte, rewqrd , done

                #if game is over by playing wrong

        
   

    def game_over(self, row , col):
        # return 1 if player wins 0 if player didnt win and 2 is player just played in wrong place and as a 

        #check row tile was played in
        curr_row = self.board[row]
        for i in range(len(curr_row)-4):
            if curr_row[i]==1 and curr_row[i+1]==1 and curr_row[i+2]==1 and curr_row[i+3]==1:
                #user 1 wins
                # print("user one wins by row")
                return True
            if curr_row[i]==2 and curr_row[i+1]==2 and curr_row[i+2]==2 and curr_row[i+3]==2:
                #user 2 wins
                # print("user two wins by row")
                return True

        for i in range(len(self.board)-1,3,-1):
            if self.board[i][col]==1 and self.board[i-1][col]==1 and self.board[i-2][col]==1 and self.board[i-3][col]==1:
                #user 1 wins
                # print("user one wins by col")
                return True
            if self.board[i][col]==2 and self.board[i-1][col]==2 and self.board[i-2][col]==2 and self.board[i-3][col]==2:
                #user 1 wins
                # print("user two wins by col")
                return True


        #check diagonal
        diag1  = self.diag_1_cache[row+col]

        for i in range(len(diag1)-3):
            if diag1[i]==1 and diag1[i+1]==1 and diag1[i+2]==1  and diag1[i+3]==1 :
                # print("player one wins by diagonal")
                return True

            if diag1[i]==2 and diag1[i+1]==2 and diag1[i+2]==2  and diag1[i+3]==2 :
                # print("player two wins by diagonal")
                return True
            

        diag2  = self.diag_2_cache[row - col + 7]
        for i in range(len(diag2)-3):
            if diag2[i]==1 and diag2[i+1]==1 and diag2[i+2]==1  and diag2[i+3]==1 :
                # print("player one wins by diagonal")
                return True

            if diag2[i]==2 and diag2[i+1]==2 and diag2[i+2]==2  and diag2[i+3]==2 :
                # print("player two wins by diagonal")
                return True

        return False