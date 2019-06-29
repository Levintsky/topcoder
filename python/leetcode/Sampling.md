## Random Sampling Shuffle

# Random shuffling
- LC-384: Shuffle an Array
	- fisher-Yates shuffle: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

# Reservoir Sampling
- get an old one (k times now), given a new one, accept and replace with probability 1/k+1
- LC-398: Random Pick Index

## Sampling with Blacklist
- LC-519: Random Flip Matrix
- LC-710: Random Pick with Blacklist

# http://www.cnblogs.com/xbinworld/p/4266146.html

# Monte Carlo
- sample a lot of x, to estimate E(f(x)), E(f) = 1/N sum f(x_i)
- MC integration
	- to integrate f(x)
	- sample n samples from a distribution q(x)
	- compute sum (f(x)/q(x)) * q(x)

# Box-Muller

# Acceptance-Rejection Sampling
to sample from p(x)
have a distribution q(x), suppose q(x) * k >= p(x), k>=1
sample x_i, accept with probability
p(x)/kq(x)

# Importance Sampling
E = sum f(z) p(z) dz
  = sum f(z) p(z)/q(z) q(z) dz
p(z)/q(z): importance weight

# Markov Chain
pi* P = pi (stationary distribution)

# detailed balance condition
pi_i P_ij = pi_j P_ji for all i,j 
Generally, not satisfied for general transition matrix P_ij and pi_i
So, sample from q and reject with alpha = min(1, p(j)q(j,i)/p(i)q(i,j))

# MCMC-- Metropolis-Hasting
generates a random walk using a proposal density and a method for rejecting some of the proposed moves.

# MCMC-- Gibbs Sampling
Requires all the conditional distributions of the target distribution to be sampled exactly.
x_t = (x0_t, x1_t, x2_t, ..., xn_t)
step 0: x0_t+1, given x1_t, x2_t, ...
step 1: x1_t+1, given x0_t+1, x2_t, ...
...
step n: xn_t+1, given x0_t+1, x2_t+1, ...
return x_t+1
