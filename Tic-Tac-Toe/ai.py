
#take next available tile
def easy(board):
    for key in board:
        if board[key]==' ':
            return key



def best_move(board):
    best_score = -float('inf') #set best_score to negative infinity
    next_move = None
    for key in board:
        if board[key] == ' ':
            board[key] = 'O' # make a valid move on the board
            # If the AI can win the game by making this move,
            # AI will take this move and skip the minimax() 
            
            if check_winner(board) == 'O': 
               return key
            
            # use minimax() to calculate the score of each move
            # we use False here because we are minimizing 
            # our loss
            score = minimax(board, False)
            #print(key, " max: ", score)
            board[key] = ' ' #revert the move 
            #updating best_score and next_move
            if score > best_score:
                best_score = score
                next_move = key
                
    return next_move
    
    

def minimax(board, isMaximizing):
    # Check if there is a winner
    if check_winner(board)=='O':
        return 1
    winner = check_winner(board)
    if winner:
        if winner == 'O':
            return 1
        elif winner == 'Tie':
            return 0
        else:
            return -1
    
    # Maximizing our gain 
    if isMaximizing:
        best_score = -float('inf')
        for key in board:
            if board[key] == ' ':
                board[key] = 'O'
                # next move will be human player
                # we want to minimize our loss
                # so we pass False into the minimax()
                score = minimax(board,  False)
                #print(key, " min: ", score)
                board[key] = ' '
                
                best_score = max(score, best_score)
        return best_score
    else:
    # minimizing our loss
        best_score = float('inf')
        for key in board:
            if board[key] == ' ':
                board[key] = 'X'
                # next move will be AI player
                # we are maximizing our gain
                # so we pass True into the minimax()
                score = minimax(board,  True)
                #print(key, " min: ", score)
                board[key] = ' '
                
                best_score = min(score, best_score)
        return best_score
        
'''
    Check if there is a winner
    if true, return winner
    if false, check if the board is full,
        if full, return "Tie"
        else return none
'''
def check_winner(board):

    # return the winner if there is one
    if board['1'] == board['2'] == board['3'] != ' ': # across the top             
        return board['1']
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        return board['4']
    elif board['7'] == board['8'] == board['9'] != ' ': # across the bottom
        return board['7']
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        return board['1']
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        return board['2']
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        return board['3']
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        return board['7']
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        return board['1']

    full = True #set full to True

    #if there is an empty tile, change full to False
    for tile in board:
        if board[tile] == ' ':
            full = False
    
    if full: 
        return "Tie"
    else:
        return None
