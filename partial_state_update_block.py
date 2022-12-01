from actors_holdings_stage import *
from num_tokens_and_dollars_stage import *
from minting_stage import *
from price_stage import *

partial_state_update_block = {
       'minting_stage':{
          'policies' :{
                      'delta_M_seed'    :p_delta_M_seed,
                      'delta_M_team'    :p_delta_M_team,
                      'detlta_M_retail' :p_delta_M_retail,
                      'detlta_M_solvers':p_delta_M_solvers},
          'variables':{
                      'M'              :s_M,
                      'M_seed'         :s_M_seed,
                      'M_team'         :s_M_team,
                      'M_retail'       :s_M_retail,
                      'M_solvers'      :s_M_solvers,
                      'delta_M'        :s_delta_M,
                      'delta_M_seed'   :s_delta_M_seed,
                      'delta_M_team'   :s_delta_M_team,
                      'delta_M_retail' :s_delta_M_retail,
                      'delta_M_solvers':s_delta_M_solvers}},
     
    'actors_holdings_stage': {
        'policies' :{
                     'sell_seed'   :p_decide_sell_or_hold_seed,
                     'sell_team'   :p_decide_sell_or_hold_team,
                     'sell_solvers':p_decide_sell_or_hold_solvers,
                     'buy_retail'  :p_decide_buy_or_hold_retail,
                     },
        'variables':{
                     'N_seed'            :s_N_seed,
                     'N_seed_previous'   :s_N_seed_previous,
                     'N_team'            :s_N_team,
                     'N_team_previous'   :s_N_team_previous,
                     'N_solvers'         :s_N_solvers,
                     'N_solvers_previous':s_N_solvers_previous,
                     'N_retail'          :s_N_retail,
                     'N_retail_previous' :s_N_retail_previous,
                    }
                                },
    
    'num_tokens_and_dollars_stage': {
        'policies' :{'tokens_sold_to_market'    :p_tokens_sold_to_market,
                     'tokens_bought_from_market':p_tokens_bought_from_market},
        'variables':{
                    'N_T'     :s_N_T,
                    'N_d'     :s_N_d}},
    
    'price_stage':{
        'policies' :{'P_p'           :p_calc_P,
                     'P_EMA_p'       :p_calc_P_EMA},
        'variables':{'P'             :s_P,
                     'P_previous'    :s_P_previous,
                     'P_EMA'         :s_P_EMA,
                     'P_EMA_previous':s_P_EMA_previous,
                     'market_cap'    :s_market_cap}}
}
    

