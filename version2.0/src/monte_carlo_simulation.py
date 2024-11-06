import numpy as np
import logging

def run_monte_carlo(bayesian_results, n_iterations=100):
    initial_priors = bayesian_results['priors']
    monte_carlo_results = []

    for i in range(n_iterations):
        run_result = {param: np.random.normal(mean, std_dev) for param, (mean, std_dev) in initial_priors.items()}
        monte_carlo_results.append(run_result)

    logging.debug("Monte Carlo simulation generated %d results", len(monte_carlo_results))
    if monte_carlo_results:
        logging.debug("Sample result structure from Monte Carlo: %s", monte_carlo_results[0])
    return monte_carlo_results
