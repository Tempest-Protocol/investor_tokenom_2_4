# investor_tokenom_2_4

# Introduction
This is an iteration of a cadCAD model for the interaction between investors,
solvers, team, and retail investors and those interactions’ effects
on the Tempest token price.

# The Token Distribution Mechanism
The driving, or underlying, force of this model is the Tempest network minting
schedule. The minting schedule dictates how many tokens each actor in the
system gets and when. The pre-seed investors, team, and solvers are the actors
considered in this model (the full list includes seed investors and advisors as
well).

Each of these different actors has a set price per token that they pay upfront
and an initial investment multiplier that dictates their incentive to sell, which
varies by actor. For instance, the seed investors may want to multiply their
initial investment by 5, whereas the team members may hold out for up to a
factor of 10.

# The Token Price Model
There are a wealth of methods to predict price in an economic model using
supply and demand or something equivalent. For this iteration of the model, we choose to
make the definition

P = N_d/N_T(1)

where Nd and NT are the number of dollars and tokens in the system, respec-
tively. This is not dissimilar to that of an xy = k AMM price curve definition (P = y/x).
It also captures the behavior of supply and demand in a straightforward man-
ner. When dollars come into the system this means demand has gone up and
so price goes up, whereas when tokens come into the system (before they are
purchased) price goes down.

At the beginning of each time cycle, which for this model is one day, the
number of tokens minted to each actor is calculated and given to those actors.
After that, each actor makes a choice to sell or buy tokens. The team, solvers,
and investors can only sell and the retail users can only buy according to this
model. The team sells if price reaches 10 times their initial investment, investors
sell if price reaches 5 times their initial investment, and solvers sell at random.
Each of these actors, we assume, will only sell up to 1% of their total holdings at a time (per day). The retail purchasers will buy at random each timestep, and buy a random percent (in the neighborhood of 1%) of amount of tokens on the market including the tokens
sold by other actors and those tokens from the BCO.
The tokens bought and sold are then exchanged to form new values of Nd
and NT and the a new P is calculated. The cycle begins over again at the next time step.


