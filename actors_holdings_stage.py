import numpy as np
import pandas as pd
from initial_states_and_constants import constants


"""
User Policies
"""
def p_decide_sell_or_hold_seed(params,substep,state_history,previous_state):
    desired_investment_multiplier = 5
    if previous_state['P']/constants['P_0_seed'] > desired_investment_multiplier:
        sell = True
    else:
        sell = False
    return {'sell_seed': sell}


def p_decide_sell_or_hold_team(params,substep,state_history,previous_state):
    desired_investment_multiplier = 10
    if previous_state['P']/constants['P_0_team'] > desired_investment_multiplier:
        sell = True
    else:
        sell = False
    return {'sell_team': sell}


def p_decide_buy_or_hold_retail(params,substep,state_history,previous_state):
    P_EMA_diff         = previous_state['P_EMA_previous'] - previous_state['P_EMA']
    P_EMA_diff_percent = P_EMA_diff/previous_state['P_EMA_previous']*100
    # if abs(P_EMA_diff_percent) > 2:
    if float(np.random.default_rng().normal(1, 0.02, 1)) > 1:
        buy = True
    else:
        buy = False
    return {'buy_retail': buy}


def p_decide_sell_or_hold_solvers(params,substep,state_history,previous_state):
    #let solvers buy and sell be totally random for now.
    if float(np.random.default_rng().normal(1, 0.02, 1)) > 1:
        sell = True
    else:
        sell = False
    return {'sell_solvers': sell}

"""
State Updates
"""
def s_N_seed_previous(params, substep, state_history, previous_state, policy_input):
    N_seed_previous = previous_state['N_seed'] + previous_state['delta_M_seed']
    return ('N_seed_previous', N_seed_previous)


def s_N_seed(params, substep, state_history, previous_state, policy_input):
    if policy_input['sell_seed']:
        delta  = 0.01
        N_seed = previous_state['N_seed'] + previous_state['delta_M_seed'] - delta*previous_state['N_seed']
    else:
        N_seed = previous_state['N_seed'] + previous_state['delta_M_seed']
    return ('N_seed', N_seed)


def s_N_team_previous(params, substep, state_history, previous_state, policy_input):
    N_team_previous = previous_state['N_team'] + previous_state['delta_M_team']
    return ('N_team_previous', N_team_previous)


def s_N_team(params, substep, state_history, previous_state, policy_input):
    if policy_input['sell_team']:
        delta  = 0.01
        N_team = previous_state['N_team'] + previous_state['delta_M_team'] - delta*previous_state['N_team']
    else:
        N_team = previous_state['N_team'] + previous_state['delta_M_team']
    return ('N_team', N_team)


def s_N_retail_previous(params, substep, state_history, previous_state, policy_input):
    N_retail_previous = previous_state['N_retail'] + previous_state['delta_M_retail']
    return ('N_retail_previous', N_retail_previous)


def s_N_retail(params, substep, state_history, previous_state, policy_input):
    if policy_input['buy_retail']:
        s = float(np.random.default_rng().normal(1, 0.02, 1))
        delta  = 0.01*s
        #Recall that retail can only buy from the holdings of private owners according to this model.
        #N_retail = previous_state['N_retail'] + previous_state['delta_M_retail'] + delta*(previous_state['N_T'])
        N_retail = previous_state['N_retail'] + previous_state['delta_M_retail'] + 0.01*(previous_state['N_seed'] + previous_state['N_team'] + previous_state['N_solvers'])
    else:
        N_retail = previous_state['N_retail'] + previous_state['delta_M_retail']
    return ('N_retail', N_retail)


def s_N_solvers_previous(params, substep, state_history, previous_state, policy_input):
    N_solvers_previous = previous_state['N_solvers'] + previous_state['delta_M_solvers']
    return ('N_solvers_previous', N_solvers_previous)


def s_N_solvers(params, substep, state_history, previous_state, policy_input):
    if policy_input['sell_solvers']:
        delta  = 0.01
        N_solvers = previous_state['N_solvers'] + previous_state['delta_M_solvers'] - delta*previous_state['N_solvers']
    else:
        N_solvers = previous_state['N_solvers'] + previous_state['delta_M_solvers']
    return ('N_solvers', N_solvers)



# def s_(params, substep, state_history, previous_state, policy_input):
    
#     return ('', )


#########################################################################################################################




































