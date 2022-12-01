import numpy as np
import pandas as pd
from initial_states_and_constants import constants

#this stage starts counting from the end of the BCO. Assume BCO
#time is 1 month (30 days). Vesting periods are 1 year from start of
#BCO. Meaning that vesting periods begin at t=365-30=335

"""
User Policies
"""

def p_delta_M_seed(params,substep,state_history,previous_state):
    vest_period     = 2.5
    tokens_received = 300e6
    time            = previous_state['timestep']
    if time<335 or time>(335 + vest_period*365):
        delta_M_seed = 0
    else:
        delta_M_seed = tokens_received/(vest_period*365)
    dM = delta_M_seed
    return {'delta_M_seed': dM}


def p_delta_M_team(params,substep,state_history,previous_state):
    vest_period     = 3
    tokens_received = 750e6
    time            = previous_state['timestep']
    if time<335 or time>(335 + vest_period*365):
        delta_M_team = 0
    else:
        delta_M_team = tokens_received/(vest_period*365)
    dM = delta_M_team
    return {'delta_M_team': dM}


def p_delta_M_retail(params,substep,state_history,previous_state):
    dM = 0
    return {'delta_M_retail': dM}

def p_delta_M_solvers(params,substep,state_history,previous_state):
    k = np.arange(0.5,1,0.01)
    percent_solver_success = float(np.random.choice(k))
    # print(percent_solver_success)
    dM = 250e6/365*percent_solver_success
    return {'delta_M_solvers': dM}

# def p_(params,substep,state_history,previous_state):
#     return {'': }

"""
State Updates
"""
def s_delta_M(params, substep, state_history, previous_state, policy_input):
    dM = policy_input['delta_M_team'] + policy_input['delta_M_seed']
    return ('delta_M', dM)


def s_M(params, substep, state_history, previous_state, policy_input):
    M = previous_state['M'] + policy_input['delta_M_team'] + policy_input['delta_M_seed'] + policy_input['delta_M_solvers']
    return ('M', M)


def s_delta_M_seed(params, substep, state_history, previous_state, policy_input):
    dM = policy_input['delta_M_seed']
    return ('delta_M_seed', dM)


def s_M_seed(params, substep, state_history, previous_state, policy_input):
    M = previous_state['M_seed'] + policy_input['delta_M_seed']
    return ('M_seed', M)


def s_delta_M_team(params, substep, state_history, previous_state, policy_input):
    dM = policy_input['delta_M_team']
    return ('delta_M_team', dM)


def s_M_team(params, substep, state_history, previous_state, policy_input):
    M = previous_state['M_team'] + policy_input['delta_M_team']
    return ('M_team', M)


def s_delta_M_retail(params, substep, state_history, previous_state, policy_input):
    dM = policy_input['delta_M_retail']
    return ('delta_M_retail', dM)


def s_M_retail(params, substep, state_history, previous_state, policy_input):
    M = previous_state['M_retail'] + policy_input['delta_M_retail']
    return ('M_retail', M)


def s_delta_M_solvers(params, substep, state_history, previous_state, policy_input):
    dM = policy_input['delta_M_solvers']
    return ('delta_M_solvers', dM)


def s_M_solvers(params, substep, state_history, previous_state, policy_input):
    M = previous_state['M_solvers'] + policy_input['delta_M_solvers']
    return ('M_solvers', M)



# def s_(params, substep, state_history, previous_state, policy_input):
    
#     return ('', )


#########################################################################################################################






# def s_N_seed(params, substep, state_history, previous_state, policy_input):
#     A = policy_input['A_p_seed']
#     desired_investment_multiplier = 3
#     if previous_state['P']/constants['P_0_seed'] > desired_investment_multiplier:
#         delta = 0.1
#     else:
#         delta = 0.0  
#     H = A - delta*previous_state['H_seed']    
#     return ('H_seed', H)

# def s_N_team(params, substep, state_history, previous_state, policy_input):
#     A = policy_input['A_p_team']
#     desired_investment_multiplier = 10
#     if previous_state['P']/constants['P_0_team'] > desired_investment_multiplier:
#         delta = 0.1
#     else:
#         delta = 0.0  
#     H = A - delta*previous_state['H_team']    
#     return ('H_team', H)

# def s_N_reat






























