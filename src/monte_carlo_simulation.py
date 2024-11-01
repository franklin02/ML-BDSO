import numpy as np
import matplotlib.pyplot as plt

# Dictionary of parameter units
parameter_units = {
    "compressive_strength": "MPa",
    "tensile_strength": "MPa",
    "elastic_modulus": "MPa",
    # ... [Other parameter units as defined previously]
    "vibration_level": "(dimensionless)"
}

def run_monte_carlo(bayesian_results, num_simulations=1000):
    """
    Runs Monte Carlo simulations using defect probability priors from Bayesian inference.
    Implements adaptive sampling for high-risk zones and saves the defect probability histogram
    and trend line.
    """
    defect_probabilities = []
    for i in range(num_simulations):
        run_result = {param: np.random.normal(mean, 0.01) for param, (mean, _) in bayesian_results['priors'].items()}
        defect_probabilities.append(run_result)

    # Adaptive sampling for high-risk defect probabilities
    high_risk_probs = [
        np.mean([v for v in run.values() if not np.isnan(v)])
        for run in defect_probabilities if np.mean([v for v in run.values() if not np.isnan(v)]) > 0.1
    ]
    avg_high_risk_prob = np.mean(high_risk_probs) if high_risk_probs else 0
    print(f"Average high-risk defect probability: {avg_high_risk_prob:.4f} (dimensionless)")

    # Plot Monte Carlo defect probability distribution
    all_probabilities = [np.mean([v for v in run.values() if not np.isnan(v)]) for run in defect_probabilities]
    plt.figure(figsize=(10, 6))
    plt.hist(all_probabilities, bins=20, color='lightcoral', edgecolor='black')
    plt.title("Monte Carlo Defect Probability Distribution")
    plt.xlabel("Defect Probability (dimensionless)")
    plt.ylabel("Frequency")
    plt.savefig("../results/monte_carlo_defect_probability_distribution.png")
    plt.close()

    # Plot trend of defect probabilities over simulations
    plt.figure(figsize=(10, 6))
    plt.plot(all_probabilities, color='blue', linestyle='-', marker='o', markersize=3)
    plt.title("Defect Probability Trend Over Simulations")
    plt.xlabel("Simulation Run")
    plt.ylabel("Defect Probability (dimensionless)")
    plt.savefig("../results/defect_probability_trend.png")
    plt.close()

    return defect_probabilities
