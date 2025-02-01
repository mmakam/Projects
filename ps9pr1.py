#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        for i in range(2*self.width + 1):
            s+= '-'
        s+='\n'
        for i in range(self.width):
            s+= ' '+str(i%10)
        s+='\n'
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        count = 0
        for i in range(len(self.slots)):
            for j in range(len(self.slots[0])):
                if j==col and count ==0:
                    if i == len(self.slots)-1:
                        self.slots[i][j] = checker
                        count+=1
                    elif self.slots[i+1][j] != ' ':
                        self.slots[i][j] = checker
                        count+=1

    
    ### add your reset method here ###
    def reset(self):
        '''reset the Board object on which it is called by setting all slots to contain a space character.'''
        for i in range(len(self.slots)):
            for j in range(len(self.slots[0])):
                self.slots[i][j]=' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
### add your remaining methods here    
    def can_add_to(self, col):
        '''returns True if it is valid to place a checker in the column col on
        \the calling Board object. Otherwise, it should return False.'''
        for i in range(len(self.slots)):
            for j in range(len(self.slots[0])):
                if col<0 or col>len(self.slots[0])-1:
                    return False
                elif self.slots[0][col]!=' ':
                    return False
        return True
    
    def is_full(self):
        '''returns True if the called Board object is completely full of 
        checkers, and returns False otherwise.'''
        for i in range(self.width):
            if self.can_add_to(i)==True:
                return False
        return True
    
    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board 
        object. If the column is empty, then the method should do nothing.'''
        count=0
        for i in range(len(self.slots)):
            for j in range(len(self.slots[0])):
                if j==col and count==0 and self.slots[i][j]!=' ':
                    self.slots[i][j]=' '
                    count+=1
                    
    def is_horizontal_win(self, checker):
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
    
    def is_vertical_win(self, checker):
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
    
    def is_diagonal_win(self, checker):
        for row in range(self.height-3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
                elif self.slots[row][col+3] == checker and \
                self.slots[row+1][col+2] == checker and \
                self.slots[row+2][col+1] == checker and \
                self.slots[row+3][col] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_diagonal_win(checker)==True or self.is_horizontal_win(checker)==True \
            or self.is_vertical_win(checker)==True:
                return True
        else:
            return False
                        
