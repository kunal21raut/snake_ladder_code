import random

def roll_dice():
    return random.randint(1,6)
    
    
def move_player(player,position,total_cells):
    roll = roll_dice()
    print(f"Player {player} rolled: {roll}")
    
    new_position = position[player] + roll
    if new_position > total_cells:
        # position[player] = new_position
        new_position = position[player]
        
    for other_player, pos in position.items():
        if other_player!= player and pos == new_position:
            print(f"player {other_player} was already at {new_position}.. Sent back to start")
            position[other_player] = 0
            break
        
    position[player] = new_position
    
    print(f"Player {player} is now at position {position[player]}\n")
    
    return position[player] == total_cells
    
    
def play_game(board_size, player_count):
    total_cells = board_size * board_size
    position = {player: 0 for player in range(1,player_count+1)}
    

    while True:
        for player in range(1, player_count + 1):
            input(f"Player {player}, press enter to roll dice.")
            
            if move_player(player,position,total_cells):
                print(f"Player {player} WINS..")
                
                return
    
    

board_size = int(input("board size to play snake and ladder game without snakes and ladder : "))
# board_size = 4

player_count = 3 

play_game(board_size,player_count)