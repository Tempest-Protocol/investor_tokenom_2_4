

constants = {
    'P_0_seed':float(0.01),
    'P_0_team':float(0.05),
    'N_T_0'   :float(1e9),
    'N_d_0'   :float(0.04*1e9)
}


genesis_states = {
    # initial states of the economy
    'M'                  :float(1e9),
    'M_seed'             :float(0),
    'M_team'             :float(0),
    'M_retail'           :constants['N_T_0'],
    'M_solvers'          :float(0),
    'delta_M_seed'       :float(0),
    'delta_M_team'       :float(0),
    'delta_M_retail'     :float(0),
    'delta_M_solvers'     :float(0),
    'N_seed'             :float(0),
    'N_team'             :float(0),
    'N_retail'           :float(0),#float(1e9),
    'N_solvers'          :float(0),
    'N_seed_previous'    :float(0),
    'N_team_previous'    :float(0),
    'N_retail_previous'  :float(0),
    'N_solvers_previous' :float(0),
    'N_T'       :constants['N_T_0'],
    'N_d'       :constants['N_d_0'],
    'P'         :constants['N_d_0']/constants['N_T_0'],
    'P_previous':constants['N_d_0']/constants['N_T_0'],
    'P_EMA'         :constants['N_d_0']/constants['N_T_0'],
    'P_EMA_previous':constants['N_d_0']/constants['N_T_0'],
    'market_cap':constants['N_d_0']/constants['N_T_0']*constants['N_T_0'],
}



