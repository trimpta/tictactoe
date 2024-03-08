# 14:49 08/03/2024
#Auther: Trimpta
#tictactoe

'''
why not?
'''

class board:

    def __init__(self) -> None:
        self.board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

    def __repr__(self) -> str:

        val = ""
        
        for row in self.board:
            val += " | ".join(row)
            val += "\n_________\n\n"

        return val            

    def is_occupied(self, x:int , y:int) -> str | bool:

        return self.board[x][y] if self.board[x][y]!= " " else False
    
    def place_X(self, x:int, y:int) -> bool:

        if self.is_occupied(x, y):
            return False
        
        self.board[x][y] = "X"
        return True
    
    def place_O(self, x:int, y:int) -> bool:

        if self.is_occupied(x, y):
            return False
        
        self.board[x][y] = "O"
        return True
    
    def check_rows(self) -> str | bool:

        for row in self.board:
            val = ((' ' not in row) and (row[0] and row[1] and row[2]))

            if val:
                return val
        
        return False


    def check_columns(self) -> str:

        for i in range(3):

            val = self.board[0][i] and self.board[1][i] and self.board[2][i]
            if val != " ":
                return val
        
    def check_diagonal(self) -> str:
        b = self.board
        center = b[1][1]

        if center != ' ':
            val = (b[0][0] and b[2][2])
            if val:
                return center
            
            val = (b[0][2] and b[2][0])
            if val:
                return center
       
        return False
    
    def check_winner(self) -> str :
        
        for i in [self.check_rows(), self.check_columns, self.check_diagonal]:
            if i:
                return i
            
        return False
    
    def main(self):

        raise NotImplementedError("WIP")


        while True:
            winner = self.check_winner()
            print(self)

            if winner:
                while not self.place_O(*eval(input("O:(x,y)"))):
                    break
                while not self.place_X(*eval(input("X:(x,y)"))):
                    break
            else:
                break
                
            




if __name__ == "__main__":
    b = board()
    b.main()
