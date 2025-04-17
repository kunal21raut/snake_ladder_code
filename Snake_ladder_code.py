import random
import pandas as pd

N  = int(input("Enter the board size : "))

end_pos = N * N

players = ["p1","p2","p3"]
positions = {player: 0 for player in players}
coordinate = {player : (0,0) for player in players}
winner = None 
turn = 0

history = []

def two_d(pos):
    if pos == 0:
        return (0, 0)  

    pos -= 1 
    row = pos // N  
    col_in_row = pos % N

    y_pos = row  
    x_posa = col_in_row if row % 2 == 0 else (N - 1 - col_in_row) 

    return (x_posa, y_pos)



while winner is None:
    for player in players:
        if winner:
            break 

        turn +=1 
        dice_roll = random.randint(1,6)
        new_pos = positions[player] + dice_roll
       
        if new_pos > end_pos:
            new_pos = positions[player]
           
        print(f"{player} rolled a {dice_roll} and moved at {new_pos}")
       
        new_cord = two_d(new_pos)
       
       
        for other in players:
            if ( other != player and coordinate[other] == new_cord  and new_pos != 0):
                print(f"Collision {player} landed on {other} spot and goes to (0,0)")
                positions[other] = 0
               
                coordinate[other] = (0,0)
                
        positions[player]=  new_pos
        coordinate[player] = new_cord
               
        win_status = ""
        
        if new_pos == end_pos:
            winner = player
            win_status = "Winner"
            print(f"{player} WINS..")
        
        
        history.append({
                "Turn":turn,
                "Player":player,
                "Dice Roll":dice_roll,
                "position hist":new_pos,
                "New_pos_2d":new_cord,
                "win status":win_status,
            })
       
# print(history)
df = pd.DataFrame(history)
print(df)
