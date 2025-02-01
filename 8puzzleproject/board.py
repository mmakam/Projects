#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        count=0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                self.tiles[i][j] = digitstr[count]
                if digitstr[count]== '0':
                    self.blank_c =j
                    self.blank_r = i
                count+=1
                


    ### Add your other method definitions below. ###
    def __repr__(self):
        result=''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j]=='0':
                    result += '_ '
                else:
                    result += self.tiles[i][j] + ' '
            result+='\n'
        return result
            
        
    def  move_blank(self, direction):
        ''' moves the blank in the direction specified'''
        if direction not in ['right', 'left', 'up', 'down']:
            return False
        elif direction =='up':
            if self.blank_r==0:
                return False
            else:
                temp = self.tiles[self.blank_r][self.blank_c]
                temp2 = self.tiles[self.blank_r - 1][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = temp2
                self.tiles[self.blank_r - 1][self.blank_c] = temp
                self.blank_r-=1
                return True
        elif direction == 'down':
            if self.blank_r==len(self.tiles)-1:
                return False
            else:
                temp = self.tiles[self.blank_r][self.blank_c]
                temp2 = self.tiles[self.blank_r + 1][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = temp2
                self.tiles[self.blank_r + 1][self.blank_c] = temp
                self.blank_r+=1
                return True
        elif direction=='right':
            if self.blank_c==len(self.tiles[0])-1:
                return False
            else:
                temp = self.tiles[self.blank_r][self.blank_c]
                temp2 = self.tiles[self.blank_r][self.blank_c +1]
                self.tiles[self.blank_r][self.blank_c] = temp2
                self.tiles[self.blank_r][self.blank_c +1] = temp
                self.blank_c+=1
                return True
        elif direction=='left':
            if self.blank_c==0:
                return False
            else:
                temp = self.tiles[self.blank_r][self.blank_c]
                temp2 = self.tiles[self.blank_r][self.blank_c -1]
                self.tiles[self.blank_r][self.blank_c] = temp2
                self.tiles[self.blank_r][self.blank_c -1] = temp
                self.blank_c-=1
                return True
            
    def digit_string(self):
        '''returns a String representation of the tiles'''
        result=''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                result+=self.tiles[i][j]
        return result
    
    def copy(self):
        '''returns a deep copy of the board object'''
        return Board(self.digit_string())
    
    def num_misplaced(self):
        '''returns the number of tiles that arent in the goal state'''
        result=0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j]=='0':
                    result+=0
                elif self.tiles[i][j]!= GOAL_TILES[i][j]:
                    result+=1

        return result
    
    def __eq__(self, other):
        '''checks whether self object is equal to the other object'''
        if self.tiles==other.tiles:
            return True
        else:
            return False
                    
        
                    
            
            

        
        
            
            
            
            
        