import numpy as np
import pandas as pd
from initial_states_and_constants import constants


"""
User Policies
"""
def p_calc_P(params,substep,state_history,previous_state):

    delta_t = 1 #implicitly in cadCAD
    mu    = float(np.random.normal(loc = 0, scale = 0.01, size=1))
    sigma = 0.01
    Y = float(np.random.normal(loc = 0, scale = 0.001, size=1))
    P1 = previous_state['P'] + mu*delta_t*previous_state['P'] + sigma*np.sqrt(delta_t)*previous_state['P']*Y
    

    P = previous_state['N_d']/previous_state['N_T'] 
    s = float(np.random.default_rng().normal(1, 0.1, 1))
    P2 = P*s
    
    alpha = 0.5
    P     = alpha*P1 + (1-alpha)*P2 
    
    return {'P_p': P}


def p_calc_P_EMA(params,substep,state_history,previous_state):
    smoothing_coeff = 2
    r = 150
    if previous_state['timestep']<r:
        r = previous_state['timestep']
    price_EMA = previous_state['P']*smoothing_coeff/(1+r) + previous_state['P_previous']*(1-smoothing_coeff/(1+r))
    return {'P_EMA_p':price_EMA}

# def p_(params,substep,state_history,previous_state):
#     return {'': }

"""
State Updates
"""

def s_P(params, substep, state_history, previous_state, policy_input):
    P = policy_input['P_p']
    return ('P', P)


def s_P_previous(params, substep, state_history, previous_state, policy_input):
    P_previous = previous_state['P'] 
    return ('P_previous', P_previous)


def s_P_EMA(params, substep, state_history, previous_state, policy_input):
    P_EMA = policy_input['P_EMA_p']
    return ('P_EMA', P_EMA)


def s_P_EMA_previous(params, substep, state_history, previous_state, policy_input):
    P_EMA_previous = previous_state['P_EMA']
    return ('P_EMA_previous', P_EMA_previous)


def s_market_cap(params, substep, state_history, previous_state, policy_input):
    market_cap = policy_input['P_p']*previous_state['N_T']
    return ('market_cap',market_cap)



#########################################################################################################################

