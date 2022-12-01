import numpy as np
import pandas as pd
from initial_states_and_constants import constants


"""
User Policies
"""
def p_tokens_sold_to_market(params,substep,state_history,previous_state):
    #recall that an actor selling tokens adds those tokens to N_T
    num_tokens_sold_by_seed      = previous_state['N_seed_previous']    - previous_state['N_seed']
    num_tokens_sold_by_team      = previous_state['N_team_previous']    - previous_state['N_team']
    num_tokens_sold_by_solvers   = previous_state['N_solvers_previous'] - previous_state['N_solvers']
    sold = num_tokens_sold_by_seed + num_tokens_sold_by_team + num_tokens_sold_by_solvers
    return {'tokens_sold_to_market': sold}


def p_tokens_bought_from_market(params,substep,state_history,previous_state):
    #an actor buying tokens removes them from N_T
    num_tokens_bought_by_retail = previous_state['N_retail'] - previous_state['N_retail_previous'] 
    bought = num_tokens_bought_by_retail #+...
    return {'tokens_bought_from_market': bought}


# def p_(params,substep,state_history,previous_state):
#     return {'': }

"""
State Updates
"""

def s_N_T(params, substep, state_history, previous_state, policy_input):
    #add to prev N_T; tokens sold enter N_T, bought leaves.
    N_T = previous_state['N_T'] + policy_input['tokens_sold_to_market'] - policy_input['tokens_bought_from_market']
    return ('N_T', N_T)


def s_N_d(params, substep, state_history, previous_state, policy_input):
    #convert num tokens to dollars. Tokens in/out makes dollars out/in
    num_dollars_added = previous_state['P']*(policy_input['tokens_bought_from_market'] - policy_input['tokens_sold_to_market'])
    
    #add to prev N_d
    N_d = previous_state['N_d'] + num_dollars_added
    return ('N_d', N_d)



#########################################################################################################################


