def isSafe(i,j,board):
    for row in range(len(board)):
        for column in range(len(board)):
            #check if in this row, is any queen already present
            if board[row][column] =='q' and row==i and column!=j:
                return False
            #checks if in this column, any queen is already present
            elif board[row][column]=='q' and column==j and row!=i:
                return False
            #checks if in the diagonal any queen is present or not
            elif (i+j == column+row or i-j==row-column) and board[row][column]=='q':
                return False
    return True

def NQueens(r,n,board):
    if r==n:
        return True,board

    for i in range(n):
        if isSafe(r,i,board):
            board[r][i]='q'
            okay,board=NQueens(r+1,n,board)
            if okay:
                return True,board
            board[r][i]='-'

    return False,board

def placeNQueens(n,board):
    return NQueens(0,n,board)[1]

def main():
    n=int(input())
    #for creating the board
    board=[["-" for i in range(n)] for j in range(n)]
    
    qboard=placeNQueens(n,board)
    
    #to format and print the output
    qboard="\n".join(["".join(x) for x in qboard])
    print(qboard)

if __name__=="__main__":
    main()