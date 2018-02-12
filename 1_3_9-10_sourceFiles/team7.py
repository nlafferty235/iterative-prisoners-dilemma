from __future__ import print_function
import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Mr McD\'s Revenge' # Only 10 chars displayed.
strategy_name = 'Betray probe, betray if behind or >5% betray'
strategy_description = 'Probe the first 10 rounds with random choices. Use this information to determine the percentage of betrays continuosly.  If betray more than 5% of the time, betray.  If I fall behind more than 250 pts, betray.'
    
def move(my_history, their_history, my_score, their_score): #do not touch this row
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    This strategy will probe the first 10 rounds with betrays to see how the
    opponent reacts.  Use this information to determine the percentage of 
    betrays continuosly.  If betray more than 5% of the time, betray.  
    If I fall behind more than 250 pts, betray.'
    '''
    
    betrays = 0.
    colludes = 0.
    errors = 0.

    for item in their_history: #examine their entire history
        if item == 'b': #count all betrays
            betrays += 1
        elif item == 'c': #count all colludes
            colludes += 1
        else: #count errors (if any, hopefully not)
            errors += 1

    if(len(their_history)>0): #avoid divide by zero error
        betrayal_percentage = betrays/(len(their_history))
    else:
        betrayal_percentage = 0.
        #print('betrayal_percentage: ', str(betrayal_percentage))
    
    if(len(my_history)<10): #random betray or collude for first 10
        #print('random choice')
        return('b') #probe with betray to see how they react
    elif their_score >= (my_score + 250):
        #print('betray due to score - their_score: ', str(their_score), ', my_score: ', str(my_score))
        return 'b'
    elif betrayal_percentage > .05:
        #print('betray due to percentage')
        return 'b'
    else:
        #sprint('otherwise collude')
        return 'c'

  
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')           