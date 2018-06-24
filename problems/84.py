from __future__ import division
import operator
from random import randint, shuffle, choice
from collections import deque


class MonopolyGame():
  """
  Play a monopoly game (limited capabilities). Suited for calculating
  probabilities for ending up on a certain square.
  Define standard monopoly board, community chest and chance cards.
  Only supports cards that order movements.
  """
  
  def __init__(self,sidedness,iterations,top_probs,number_of_dice=2):
    self.sidedness = sidedness
    self.top_probs = top_probs
    self.iterations = iterations
    self.current_square = 0
    self.name = '%s-sided dice game' % self.sidedness
    self.number_of_dice = number_of_dice
    
    self.board = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3',
                 'JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3',
                 'FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3',
                 'G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']
    
    self.cchest_cards = deque(['GO','JAIL',None,None, None,None,None,None,
                        None,None,None,None, None,None,None,None])
    self.chance_cards = deque(['GO','JAIL','C1','E3','H2','R1','NEXT_R','NEXT_R',
                         'NEXT_U','MOVE_-3',None,None,None,None,None,None])
                         
    self.board_length = len(self.board)
    self.square_probs = dict(zip(self.board,[0] * self.board_length))
      
      
  def roll_die(self,n):
    """ Rolls a die n times. """
    return [randint(1,self.sidedness) for t in range(n)]
    
    
  def move_to_next_square(self,card):
    """ Move to next square on picked card from current one. """
    id = None
    location = self.current_square
    
    # While the next square is unknown
    while not id:
      
      if location == self.board_length - 1: 
        # Curl around the board if we reach the end
        location = 0
      else:
        # Move 1 step forward
        location += 1
      
      if self.board[location][:1] == card:
        id = location
        
    self.current_square = id
      
          
  def check_rules(self):
    """ Checks rules to determine next move based on current square. """
    if self.board[self.current_square] in ('CC1','CC2','CC3'):
      # Draw a card from the community chest pile
      picked_card = self.cchest_cards.popleft()
      self.cchest_cards.append(picked_card)
      
      # If card orders movement, execute it
      if picked_card:
        self.current_square = self.board.index(picked_card)
        
    elif self.board[self.current_square] in ('CH1','CH2','CH3'):
      # Draw a card from the chance pile
      picked_card = self.chance_cards.popleft()
      self.chance_cards.append(picked_card)
      
      # If card orders movement, execute it
      if picked_card:
        if picked_card in self.board:
          # Move to new square
          self.current_square = self.board.index(picked_card)
        else:
          # Determine next move
          if picked_card[:4] == 'NEXT':
            self.move_to_next_square(picked_card[5:])
          elif picked_card[:4] == 'MOVE':
            steps = int(picked_card[5:])
            self.current_square += steps
            
    elif self.board[self.current_square] == 'G2J':
      self.current_square = self.board.index('JAIL')
  
  
  def make_a_move(self):
    """ Make a move by rolling the die/dice. """
    self.current_square += sum(self.roll_die(self.number_of_dice))
    self.current_square %= self.board_length - 1
    self.check_rules()
    self.update_visits()

  
  def update_visits(self):
    """ Adjusts probabilities after move. """
    self.square_probs[self.board[self.current_square]] += 1
    
    
  def play(self):
    """ Start a new game. """
    
    # Shuffle community cards
    shuffle(self.cchest_cards)
    shuffle(self.chance_cards)
    
    for game in range(self.iterations):
      self.make_a_move()
    
    self.print_probs(self.top_probs)
    
    
  def print_probs(self,limit):
    """ Prints the probabilities for each square. """
    sorted_probs = sorted(self.square_probs.items(),key=operator.itemgetter(1),reverse=True)
    print '\nPopular squares for %s with %d iterations and %d die/dice:' % (self.name,self.iterations,self.number_of_dice)
    for sq,p in sorted_probs[:limit]:
      print '%s(%s): %.2f' % (sq,self.board.index(sq),(p/self.iterations)*100) 

    
if __name__ == '__main__':
  game = MonopolyGame(4,250000,10)
  game.play()