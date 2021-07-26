# Input:
#  chessboard: A 2-dimensional array that represents.  Example below.
#  [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0]]
# Returns:
#  True if none of the rooks can attack each other.
#  False if there is at least one pair of rooks that can attack each other.

def rooks_are_safe(chessboard):
  
    rows = len(chessboard);  
    cols = len(chessboard[0]); 

    for i in range(0, rows):  
        sumRow = 0;  
        for j in range(0, cols):  
            sumRow = sumRow + chessboard[i][j];  
            if sumRow > 1:
                    return False
    
    for i in range(0, rows):  
        sumCol = 0;  
        for j in range(0, cols):  
            sumCol = sumCol + chessboard[j][i];  
            if sumCol > 1:
                    return False
    return True