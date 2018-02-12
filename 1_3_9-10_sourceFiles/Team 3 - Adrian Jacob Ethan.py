import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
team_name = 'E3'
strategy_name = 'Trust Meter.'
strategy_description = '''Always start with a collude. Next three turns are completly random, no strings attached.
Every 5th turn we collude. If they betray on this turn, our trust meter will have a higher probability of betraying.
Every 5th turn we collude. If they collude on this turn, our trust meter will have a higher probability of colluding.
Trust meter impacts the random choices (after every fifth turn, the following 4 are random.) from this point on.
It will still be random, but depending on the opponents choice, we have a higher chance of betrayal/colluding 
depending on their choice on the every 5th turn.
On the 5th iteration of this loop, trust meter resets the data.'''


def move(my_history, their_history, my_score, their_score): 
    '''Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints. Make my move. 
    Returns c or b.'''
    if my_history <=4:
        random.random['c','b']
 
    c_tally, b_tally, errors = trust_meter(my_history, their_history, my_score, their_score)
    if c_tally > b_tally:
        return 'c'
    else:
        return 'b'

def trust_meter(my_history, their_history, my_score, their_score):
    '''Makes a desicion based on opponent history.'''
    b_count = 0
    c_count = 0
    errors = 0
    for item in their_history[-5]:
        if item == 'b':
            b_count += 1
        elif item == 'c':
           c_count += 1
        else:
            errors += 1

    return b_count,c_count,errors



