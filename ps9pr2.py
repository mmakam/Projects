#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player():
    
    def __init__(self, checker):
        '''Constructs a Player Object'''
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        '''returns a string representing a Player object'''
        return 'Player' + ' '+self.checker
    
    def opponent_checker(self):
        '''returns the checker being used by the opponent'''
        if self.checker=='X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        ''' that accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move. To do this, the method 
        should ask the user to enter a column number that represents where 
        the user wants to place a checker on the board. The method should 
        repeatedly ask for a column number until a valid column number is given.
        Additionally, this method should increment the number of moves that the 
        Player object has made.'''
        nm= int(input('Enter a column: '))
        while(b.can_add_to(nm)!=True):
            print('Try again!')
            nm = int(input('Enter a column: '))
        else:
            self.num_moves+=1
            return nm
        
