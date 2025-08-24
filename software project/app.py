from flask import Flask, request, jsonify
import numpy as np
from scipy.optimize import minimize
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# Your MPT functions and any other imports or setups go here
# For example, portfolio_performance and optimize_portfolio functions

@app.route('/analyze', methods=['GET'])
def analyze():
    symbols = request.args.get('symbols')
    # Assume symbols are passed as a comma-separated list
    symbols = symbols.split(',')

    # Implement your logic to fetch stock data for these symbols,
    # calculate returns, variances, and covariances, and then find the optimal weights.
    # For this example, let's just return some dummy data:
    dummy_weights = np.random.random(len(symbols)).tolist()
    return jsonify(weights=dummy_weights)

if __name__ == '__main__':
    app.run(debug=True)
