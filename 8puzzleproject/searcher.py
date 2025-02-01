#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def  __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.states=[]
        self.num_tested=0
        
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        'adds a state to self.states'
        self.states+=[new_state]
        
    def should_add(self, state):
        'checks if we should add a state or not'
        if self.depth_limit!= -1 and state.num_moves>self.depth_limit:
            return False
        elif state.creates_cycle()==True:
            return False
        else:
            return True
    
    def add_states(self, new_states):
        '''that takes a list State objects called new_states, and that 
        processes the elements of new_states one at a time'''
        for i in range(len(new_states)):
            if self.should_add(new_states[i])==True:
                self.add_state(new_states[i])
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state) :
        self.add_state(init_state)
        while(self.states!=[]):
            s = self.next_state()
            self.num_tested+=1
            if s.is_goal()==True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None 

### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    
    def next_state(self):
        '''overrides nextstate from Searcher'''
        s = self.states[0]
        self.states.remove(s)
        return s  

class DFSearcher(Searcher):
    def next_state(self):
        '''performs depth first search'''
        s = self.states[len(self.states)-1]
        self.states.remove(s)
        return s          


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    return state.board.num_misplaced()

def h2(state):
    '''This heuristic returns sum of distances between a misplaced tile and its target row and column'''
    board = state.board
    
    misplaced = 0
    
    for i in range(3):
        for j in range(3):
            if board.tiles[i][j] != '0':
                target_row = (int(board.tiles[i][j]) - 1) // 3
                target_col = (int(board.tiles[i][j])) % 3
                misplaced += abs(i - target_row) + abs(j - target_col)
    
    return misplaced-3

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        super().__init__(-1)
        self.heuristic=heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        priority = self.priority(state)
        self.states+=[[priority, state]]
    
    def next_state(self):
        lc = max(self.states)
        s = lc[1]
        self.states.remove(lc)
        return s          



### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    
    def priority(self, state):
        return -1 * (self.heuristic(state) + state.num_moves)
    
    def add_state(self, state):
        priority = self.priority(state)
        self.states+=[[priority, state]]
    
    
 
