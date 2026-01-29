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


def check_horizontal(board):
    
    vorheriges_symbol = "a"
    counter = 1
    gewonnen = 0
    
    for zeile in board:
        for kaestchen in zeile:
            if kaestchen != "":
                if kaestchen == vorheriges_symbol:
                    counter = counter + 1

                else:
                    vorheriges_symbol = kaestchen
                    counter = 1

            else:
                counter = 1
            
            if counter >= 4:
                gewonnen = 1
        
    return gewonnen


def check_vertical(board):

    counter_horizontal = 0
    counter_vertical = 0
    counter = 1
    gewonnen = 0

    for zeile in board:
        for kaestchen in zeile:
            if kaestchen != "":
                if counter_horizontal < 3:
                    kaestchen_symbol = kaestchen

                    if kaestchen_symbol == board[counter_horizontal + 1][counter_vertical ]:
                        counter = counter + 1
                
                        if kaestchen_symbol == board[counter_horizontal + 2][counter_vertical ]:
                            counter = counter + 1

                            if kaestchen_symbol == board[counter_horizontal + 3][counter_vertical ]:
                                counter = counter + 1

            if counter >= 4:
                gewonnen = 1
                return gewonnen

            counter = 1            
            counter_vertical = counter_vertical + 1

        counter_vertical = 0
        counter_horizontal = counter_horizontal + 1

    return gewonnen


def check_diagonal(board):

    #Diagonal für \ Richtung

    counter_horizontal = 0
    counter_vertical = 0
    counter = 1
    gewonnen = 0


    for zeile in board:
        for kaestchen in zeile:
            if kaestchen != "":
                if counter_vertical < 4:
                    if counter_horizontal < 3:
                        kaestchen_symbol = kaestchen
                        if kaestchen_symbol == board[counter_horizontal + 1][counter_vertical + 1]:
                            counter = counter + 1
                            if kaestchen_symbol == board[counter_horizontal + 2][counter_vertical + 2]:
                                counter = counter + 1
                                if kaestchen_symbol == board[counter_horizontal + 3][counter_vertical + 3]:
                                    counter = counter + 1

            if counter >= 4:
                gewonnen = 1
                return gewonnen

            counter = 1
            counter_vertical = counter_vertical + 1

        counter_vertical = 0
        counter_horizontal = counter_horizontal + 1

    #überprüfe / Richtung

    for zeile in board:
        for kaestchen in zeile:
            if kaestchen != "":
                if counter_vertical > 2:
                    if counter_horizontal < 3:
                        kaestchen_symbol = kaestchen
                        if kaestchen_symbol == board[counter_horizontal + 1][counter_vertical - 1]:
                            counter = counter + 1
                            if kaestchen_symbol == board[counter_horizontal + 2][counter_vertical - 2]:
                                counter = counter + 1
                                if kaestchen_symbol == board[counter_horizontal + 3][counter_vertical - 3]:
                                    counter = counter + 1

            if counter >= 4:
                gewonnen = 1
                return gewonnen

            counter = 1
            counter_vertical = counter_vertical + 1

        counter_vertical = 0
        counter_horizontal = counter_horizontal + 1

    return gewonnen





        
        

            
            


    