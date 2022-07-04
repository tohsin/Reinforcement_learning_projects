class ENV:
    def __init__(self) -> None:
        self.number_rows = 6
        self.number_columns = 7
        self.board = []
        for _ in self.number_rows:
            self.board.append([0]* self.number_columns )

    def print_board(self):
        print("board")
    def can_play(self,move):
        #if position of move is zero then move is valid else 
        #game is illegal and also lost
        return self.board[0][move] == 0
    def play(self, player_number, move):
        for i in range(len(self.board)):
            if self.board[i][move] !=0:
                self.board[i-1][move] = player_number
                if self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 and self.board[0][3] != 0 and self.board[0][4] != 0 and \
                    self.board[0][5] != 0 and self.board[0][6] != 0:
                    #game is a draw no valid move no valid winner
                    return self.board, 0 , 0 ,  True

                if self.game_over:
                    #game is over current player wins 
                    return self.board, 1, -1, True  # state, reward, done
                else:
                    # game isnt over
                     self.board, 0, 0, False  #stte, rewqrd , done
    def player_wins(self):
        # fouur in a row match of rows

        #four in a row for column

        #four in a row for right to left diagonal

        #four in a roe left to right for diagonal
        pass



