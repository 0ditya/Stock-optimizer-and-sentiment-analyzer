import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Simulate some data (replace this with your actual data loading logic)
np.random.seed(42)
num_assets = 4
num_portfolios = 10000
returns = np.random.randn(num_assets, 250) * 0.01  # Simulated daily returns

# Calculate mean returns and covariance matrix
mean_returns = returns.mean(axis=1)
cov_matrix = np.cov(returns)

def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns * weights) * 252
    std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std_dev, returns

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    p_var, p_ret = portfolio_performance(weights, mean_returns, cov_matrix)
    return -(p_ret - risk_free_rate) / p_var

def optimize_portfolio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(num_assets))
    result = minimize(negative_sharpe_ratio, weights, args=(mean_returns, cov_matrix, risk_free_rate),
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result

init_guess = num_assets * [1. / num_assets,]
opt_result = optimize_portfolio(init_guess, mean_returns, cov_matrix)
opt_weights = opt_result.x

# Print optimized weights
print("Optimized Portfolio Weights:", opt_weights)
