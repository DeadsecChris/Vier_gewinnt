'''
Docstring for Function_logic
Last Changes: CM --> Init File with basic 
'''

import UI



def generate_board():

    board_zeile = ["","","","","","",""]
    board = []
    counter = 1

    while counter <= 7:
        board.append(board_zeile)
        counter = counter + 1    
    return board


    # ["","x","x","","","",""]
    # ["","x","x","","","",""]
    # ["","x","x","","","",""]
    # ["","","x","","","",""]
    # ["","","","","","",""]
    # ["","","","","","",""]


#Überprüfung vertikal
board = [ ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]
counter_horizontal = 0
counter_vertical = 0
counter = 1
gewonnen = 0

for zeile in board:
    for kaestchen in zeile:
        if kaestchen != "":
            kaestchen_symbol = kaestchen

            if kaestchen_symbol == board[counter_horizontal + 1][counter_vertical ]:
                counter = counter + 1
            
                if kaestchen_symbol == board[counter_horizontal + 2][counter_vertical ]:
                    counter = counter + 1

                    if kaestchen_symbol == board[counter_horizontal + 3][counter_vertical ]:
                        counter = counter + 1

        if counter >= 4:
            gewonnen = 1
            break
            
                
        counter_vertical = counter_vertical + 1

    counter_vertical = 0
    counter_horizontal = counter_horizontal + 1

print(gewonnen)
            

            

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


#Überprüfung Horizontal
# board = generate_board()
# vorheriges_symbol = "a"
# counter = 1
# gewonnen = 0
# for zeile in board:
#     for kaestchen in zeile:
#         if kaestchen != "":
#             if kaestchen == vorheriges_symbol:
#                 counter = counter + 1

#             else:
#                 vorheriges_symbol = kaestchen
#                 counter = 1

#         else:
#             counter = 1
        
#         if counter >= 4:
#             gewonnen = 1
#             break

# print(gewonnen)


# Test vertikal Olli

# board = generate_board()
# gewonnen = 0
# for zeile in range(0,len(board)-1):
#     for kaestchen in range(1,len(board[zeile])-1):
#         board[kaestchen][zeile]
#         if board[kaestchen][zeile] == board[kaestchen-1][zeile]:
#             counter = counter + 1
        
#         else : 
#             counter = 1

#         if counter >= 4:
#             gewonnen = 1
#             break

# print(gewonnen)

        
        

            
            


    