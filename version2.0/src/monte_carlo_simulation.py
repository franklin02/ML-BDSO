import numpy as np
import logging

def run_monte_carlo(bayesian_results, n_iterations=100, defect_type=None):
    """
    Runs Monte Carlo simulation with enhanced sampling for porosity-prone conditions if defect_type is 'porosity'.

    Parameters:
    - bayesian_results: dict
    - n_iterations: int
    - defect_type: str, optional

    Returns:
    - monte_carlo_results: list of dicts
    """
    initial_priors = bayesian_results['priors']
    porosity_params = {'aggregate_volume_fraction', 'fiber_content', 'layer_compaction_rate', 'water_cement_ratio'}
    monte_carlo_results = []

    for i in range(n_iterations):
        run_result = {
            param: np.random.normal(mean, std_dev * (1.3 if defect_type == 'porosity' and param in porosity_params else 1.0))
            for param, (mean, std_dev) in initial_priors.items()
        }
        monte_carlo_results.append(run_result)

    return monte_carlo_results

# Example usage
if __name__ == "__main__":
    # Example initial priors from Bayesian inference results
    bayesian_results = {
        "priors": {
            "compressive_strength": (40, 5),
            "tensile_strength": (5, 0.5),
            "elastic_modulus": (30000, 1500),
            "aggregate_volume_fraction": (0.6, 0.05),
            "fine_aggregate_size": (0.002, 0.0005),
            "plastic_viscosity": (50, 10),
            "tensile_adhesion_strength": (0.5, 0.05)
        },
        "defect_probability": 0.002
    }

    # Run Monte Carlo simulation
    monte_carlo_results = run_monte_carlo(bayesian_results, n_iterations=100)
    print("Sample Monte Carlo Result:", monte_carlo_results[0])
