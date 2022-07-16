from bdb import Breakpoint
from environment import ENV
if __name__ == '__main__':
    env = ENV()
    print("                              ")
    env.print_board()
    player_number = 1
    done_ = False
    moves = [1,5,3,2,2,3,3,4,5,5,4,4,4]
    for move in moves:
        print("player", player_number)
        # move_col = input("the row you wish to play on :")

        # move_col = int(move_col)

        
        reward_player1, reward_player2, done = env.play(player_number = player_number, move = move)
        done_ = done
        if done:
            print(reward_player1, reward_player2)
            print("game over")
            env.print_board()
            break
        env.print_board()
        if player_number==1:
            player_number=2
        else:
            player_number=1