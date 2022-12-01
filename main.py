import math
from decimal import Decimal
from datetime import timedelta
import numpy as np
from typing import Dict, List
import pandas as pd

# from cadCAD.configuration import append_configs
# from cadCAD.configuration.utils import bound_norm_random, ep_time_step, config_sim
# cadCAD configuration modules
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
# cadCAD simulation engine modules
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor

#auxillary files
from initial_states_and_constants import constants
from initial_states_and_constants import genesis_states
from partial_state_update_block import partial_state_update_block

#plotting
import plotly as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default='browser'
import plotly.express as px


# dummy for parameter sweep
g: Dict[str, List[int]] = {
    'alpha': [1],
}


monteCarloRuns = 1
simulationTimesteps = 10*365

sim_config = config_sim({
    'N': monteCarloRuns,
    # 'N': 1,
    'T': range(simulationTimesteps),
    'M': g,
})

# seeds = {
#     'p': np.random.RandomState(26042019),
# }


from cadCAD import configs
del configs[:] # Clear any prior configs

experiment = Experiment()
experiment.append_configs(
    initial_state = genesis_states,
    partial_state_update_blocks = partial_state_update_block,
    sim_configs = sim_config
)


#run the simulation
exec_context = ExecutionContext()
simulation = Executor(exec_context=exec_context, configs=configs)
(raw_result, tensor_field, sessions) = simulation.execute()

# Get system events and attribute index
simulationResult = pd.DataFrame(raw_result)

# aggregate each monte carlo run by the mean at each 'timestep'
mean_df = simulationResult.groupby('timestep').mean().reset_index()

time = list(range(0,simulationTimesteps+1))
time = np.array(time)


fig = make_subplots(rows = 4, cols = 1)
row = 0
row = row + 1
fig.add_trace(go.Scatter(x=time,y=mean_df.M,name='M'), row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.M_seed,name='M_seed'),row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.M_team,name='M_team'),row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.M_solvers,name='M_solvers'),row = row, col=1)
fig.update_yaxes(title_text='M',row=row,col=1)

row = row + 1
fig.add_trace(go.Scatter(x=time,y=mean_df.N_seed,name='N_seed'),row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.N_team,name='N_team'),row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.N_solvers,name='N_solvers'),row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.N_retail,name='N_retail'),row = row, col=1)
fig.update_yaxes(title_text='N',row=row,col=1)

row = row + 1
fig.add_trace(go.Scatter(x=time,y=mean_df.N_d,name='N_d'),row = row, col=1)
fig.add_trace(go.Scatter(x=time,y=mean_df.N_T,name='N_T'),row = row, col=1)
# fig.add_trace(go.Scatter(x=time,y=mean_df.S_team,name='S_team'),row = row, col=1)
fig.update_yaxes(title_text='N',row=row,col=1)

row = row + 1
fig.add_trace(go.Scatter(x=time,y=mean_df.P,name='P'),row = row, col=1)
fig.update_yaxes(title_text='P',row=row,col=1)


# row = row + 1
# fig.add_trace(go.Scatter(x=time,y=mean_df.N_T + mean_df.N_seed + mean_df.N_team + mean_df.N_solvers + mean_df.N_retail,name='N_sum'),row = row, col=1)
# fig.update_yaxes(title_text='N',row=row,col=1)


# row = row + 1
# fig.add_trace(go.Scatter(x=time,y=(mean_df.P_EMA_previous - mean_df.P_EMA)/mean_df.P_EMA_previous*100,name='P_EMA%'),row = row, col=1)
# fig.update_yaxes(title_text='P',row=row,col=1)

# row = row + 1
# fig.add_trace(go.Scatter(x=time,y=mean_df.market_cap,name='MC'),row = row, col=1)
# fig.update_yaxes(title_text='MC',row=row,col=1)





# row = row + 1
# fig.add_trace(go.Scatter(x=time,y=mean_df.B,name='B'),row = row, col=1)
# fig.update_yaxes(title_text='B',row=row,col=1)
# 


# fig.add_trace(go.Scatter(x=time,y=1/(mean_df.V),name='1/V'),row = 4, col=1)
# fig.update_yaxes(title_text='1/V',row=4,col=1)

# fig.add_trace(go.Scatter(x=time,y=mean_df.B,name='B'),row = 5, col=1)
# fig.update_yaxes(title_text='B',row=5,col=1)

# fig.add_trace(go.Scatter(x=time,y=mean_df.K,name='K'),row = 1, col=2)
# fig.update_yaxes(title_text='K',row=1,col=2)

# fig.add_trace(go.Scatter(x=time,y=mean_df.R,name='R'),row = 2, col=2)
# fig.update_yaxes(title_text='R',row=2,col=2)

# fig.add_trace(go.Scatter(x=time,y=mean_df.delta_D,name='$\Delta D$'),row = 3, col=2)
# fig.add_trace(go.Scatter(x=time,y=mean_df.delta_S,name='$\Delta S$'),row = 3, col=2)
# fig.update_yaxes(title_text='$\Delta D, \Delta S$',row=3,col=2)

# fig.add_trace(go.Scatter(x=time,y=mean_df.lambda_D,name='$\lambda_D$'),row = 4, col=2)
# fig.add_trace(go.Scatter(x=time,y=mean_df.lambda_S,name='$\lambda_S$'),row = 4, col=2)
# fig.update_yaxes(title_text='$\lambda_D, \lambda_S$',row=4,col=2)

# fig.add_trace(go.Scatter(x=time,y=mean_df.P*mean_df.K,name='PK'),row = 5, col=2)
# fig.update_yaxes(title_text='PK',row=5,col=2)


fig.show()





##################################################################################################################



# # plot
# for ii in range(1,monteCarloRuns+1):
#     yRange = simulationResult.query('run == @ii').R
#     fig.add_trace(go.Scatter(x=time,y=yRange),row = 1, col=1)
#     fig.update_yaxes(title_text='R',row=1)


# pf.first_five_plot(simulationResult,'D')

# time = list(range(0,simulationTimesteps+1))

# fig = make_subplots(rows = 4, cols = 1)

# # plot
# for ii in range(1,monteCarloRuns+1):
#     yRange = simulationResult.query('run == @ii').R
#     fig.add_trace(go.Scatter(x=time,y=yRange),row = 1, col=1)
#     fig.update_yaxes(title_text='R',row=1)
# # plot
#     yRange = (simulationResult.query('run == @ii').K)*(simulationResult.query('run == @ii').V)
#     fig.add_trace(go.Scatter(x=time,y=yRange),row = 2, col=1)
#     fig.update_yaxes(title_text='V*K',row=2)
# # plot
#     yRange = simulationResult.query('run == @ii').K
#     fig.add_trace(go.Scatter(x=time,y=yRange),row = 3, col=1)
#     fig.update_yaxes(title_text='K',row=3)    
# # plot
#     yRange = 1/simulationResult.query('run == @ii').V
#     fig.add_trace(go.Scatter(x=time,y=yRange),row = 4, col=1)
#     fig.update_yaxes(title_text='1/V',row=4)    




# fig.show()




