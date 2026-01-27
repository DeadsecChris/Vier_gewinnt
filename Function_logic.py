'''
Docstring for Function_logic
Last Changes: CM --> Init File with basic 
'''

import UI



def generate_board():

    board_zeile = ["","a","","","","",""]
    board = []
    counter = 1

    while counter <= 6:
        board.append(board_zeile)
        counter = counter + 1   
    return board



def check_horizontal(board,player):
    for zeile in board:
        
        winner = 1
    return winner

def check_vertical(board,player):
    winner = 1
    return winner

def check_diagonal(boarrd,player):
    winner = 1
    return winner

board = generate_board()
aktuelles_symbol = 
for zeile in board:
    for kaestchen in zeile:
        if kaestchen != "":
            aktuelles_symbol = kaestchen

           
        else:
            print("besetzt!")

            
            

print("")
    