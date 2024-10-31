import numpy as np
import pandas as pd
from bayesian_inference import bayesian_update
from monte_carlo_simulation import run_monte_carlo
from sensitivity_analysis import sensitivity_analysis
from feedback_optimization import feedback_optimization

# Load initial data from .txt files
material_data = pd.read_csv('../data/material_properties.txt', sep='\s+')
process_data = pd.read_csv('../data/process_parameters.txt', sep='\s+')
env_data = pd.read_csv('../data/environmental_conditions.txt', sep='\s+')

# File path for output data
output_file = '../results/output_data.txt'


def run_ml_bdso():
    with open(output_file, 'w') as f:
        f.write("ML-BDSO Framework Results\n")
        f.write("=" * 40 + "\n")

    # Step 1: Bayesian Inference and Prior Initialization
    bayesian_results = bayesian_update(material_data, process_data, env_data)
    with open(output_file, 'a') as f:
        f.write("\nBayesian Inference Results:\n")
        for key, value in bayesian_results['priors'].items():
            f.write(f"{key}: {value:.4f}\n")
        f.write(f"Initial Defect Probability: {bayesian_results['defect_probability']:.4f}\n")

    # Step 2: Monte Carlo Simulation with Adaptive Sampling
    monte_carlo_results = run_monte_carlo(bayesian_results)

    # Calculate the average defect probability for high-risk cases
    high_risk_probs = [np.mean(list(run.values())) for run in monte_carlo_results if np.mean(list(run.values())) > 0.1]
    avg_high_risk_prob = np.mean(high_risk_probs) if high_risk_probs else 0  # Avoid division by zero
    with open(output_file, 'a') as f:
        f.write("\nMonte Carlo Simulation Results:\n")
        f.write(f"Average High-Risk Defect Probability: {avg_high_risk_prob:.4f}\n")

    # Step 3: Sensitivity Analysis
    sensitivity_results = sensitivity_analysis(monte_carlo_results)
    with open(output_file, 'a') as f:
        f.write("\nSensitivity Analysis Results:\n")
        for param, score in sensitivity_results.items():
            f.write(f"{param}: {score:.4f}\n")

    # Step 4: Feedback-Controlled Optimization
    optimized_parameters = feedback_optimization(sensitivity_results)
    with open(output_file, 'a') as f:
        f.write("\nOptimized Print Parameters:\n")
        for param, value in optimized_parameters.items():
            f.write(f"{param}: {value:.4f}\n")

    print("Final optimized parameters saved to output_data.txt")


if __name__ == "__main__":
    run_ml_bdso()
