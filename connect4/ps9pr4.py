#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead= lookahead
        
    def __repr__(self):
        return 'Player ' + self.checker + ' ('+self.tiebreak+', '+ str(self.lookahead)+')'
    
    def max_score_column(self, scores):
        maxm= max(scores)
        lc=[]
        for i in range(len(scores)):
            if scores[i]==maxm:
                lc+=[i]
        if self.tiebreak=='LEFT':
            return lc[0]
        elif self.tiebreak=='RIGHT':
            return lc[-1]
        elif self.tiebreak== 'RANDOM':
            return random.choice(lc)
            
    def scores_for(self, b):
        scores = [50] * b.width
        for i in range(b.width):
            if b.can_add_to(i)==False:
                scores[i]=-1
            elif b.is_win_for(self.checker)==True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker())==True:
                scores[i]=0
            elif self.lookahead==0:
                scores[i]=50
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:  # If opponent wins
                        scores[i] = 0
                elif 0 < max(opp_scores) < 100:  # If opponent doesn't win but AIPlayer doesn't win either
                        scores[i] = 50
                else:  # AIPlayer wins in future moves
                        scores[i] = 100
                b.remove_checker(i)
        return scores
    
    def next_move(self, b):
        moves = self.scores_for(b)
        self.num_moves+=1
        return self.max_score_column(moves)