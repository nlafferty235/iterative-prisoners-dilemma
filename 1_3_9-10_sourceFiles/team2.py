####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    

    
# If the other player has betrayed within last 6 rounds, 

#if there history is bbbbb

 # Betray 25%. 

#return c 

 #if my history is ccccc

#return betray

#if there history is ccc

# return betray
#if there history is bbb
# return c

 # Betray 25% if b isnt in there last six moves

#first round return 'c'

#if we both put c

#return c

#if they have more b than c return b

def test_move(my_history, their_history, my_score, their_score, result):

    '''calls move(my_history, their_history, my_score, their_score)

    from this module. Prints error if return value != result.

    Returns True or False, dpending on whether result was as expected.

    '''

    if 'b' in their_history[-6:]: # If the other player has betrayed within last 6 rounds, 

        return 'b'<0.25               # Betray 25%. 

    if my_history[-5:] == 'bbbbb': #if there history is bbbbb

        return 'c' #return collude 

       

        if my_history[-5:] == 'ccccc': #if my history is ccccc

         return 'b'       #return betray

        if their_history[-3:] == 'ccc':     #if there history is ccc

            return 'b' # return betray

             

    if their_history[-3:] == 'bbb': #if there history is bbb

            return 'c' # return conclud

            

            if len(their_histroy)==0:         #first round

                return 'c' #return 'c'
    elif their_history[-1]=='c' and my_history[-1]=='c': #if we both put c

        return 'c' #return c

    elif 'b' > 'c' in their_history: #if their are more b than c 

        return 'b' #return b

    else:

        if random.random()<0.25: # 25% of the other rounds

            return 'b'         # Betray 
        
    
                