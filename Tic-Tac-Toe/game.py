import ai



def new_board():
    return {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
 


# update and draw the board on the terminal
def draw_board(board): 
    print("_____________")
    print("| "+board['1']+ " | "+board['2']+" | "+board['3']+" |")
    print("-------------")
    print("| "+board['4']+ " | "+board['5']+" | "+board['6']+" |")
    print("-------------")
    print("| "+board['7']+ " | "+board['8']+" | "+board['9']+" |")
    print("-------------")


# This function will return a list of
# possible moves on the current board
def get_possible_move(board):
    result = []
    for key in board:
        if board[key]==' ':
            result.append(key)
    return result



def game():
    board = new_board()
    ai_first = False #first move
    ai_turn = False
    #get all available moves
    available = get_possible_move(board)
    while True:
        # Here, I want the AI always 
        # to make the first move
        # and the first move will 
        # be tile number 1
        if ai_first:
            ai_move = '1'
            board[ai_move] = 'O'
            print("AI's move: ", ai_move)
            ai_first = False
            available.remove(ai_move)
        
        else:
            if ai_turn:
                # call the best_move() function
                # to let the AI decide a move
                ai_move = ai.best_move(board)
                print("AI's move: ", ai_move)
                board[ai_move] = 'O'
                available.remove(ai_move)
                ai_turn =False
        
        draw_board(board)
        winner = ai.check_winner(board)
        if winner:
            if winner == 'Tie':
                print(winner)
            else:
                print(winner + ' WON!')
            break
        
        while True:
            try:
                move = input("Make a move: ")
                if board[move] == ' ':
                    board[move]  = 'X'
                    available.remove(move)
                    break
                else:
                    print("Invalid move!")
                draw_board(board)
                
            except:
                print("Invalid move! ")

        ai_turn = True

        draw_board(board)
        
        winner = ai.check_winner(board)
        if winner:
            if winner == 'Tie':
                print(winner)
            else:
                print(winner + ' WON!')
            break
        

def main():
    game()


if __name__ == "__main__":
    main()