import numpy as np
import pandas as pd
from bayesian_inference import bayesian_update
from monte_carlo_simulation import run_monte_carlo
from sensitivity_analysis import sensitivity_analysis
from feedback_optimization import feedback_optimization

# Load initial data from .txt files
material_data = pd.read_csv('../data/material_properties.txt', sep='\s+', comment='#', header=0)
process_data = pd.read_csv('../data/process_parameters.txt', sep='\s+', comment='#', header=0)
env_data = pd.read_csv('../data/environmental_conditions.txt', sep='\s+', comment='#', header=0)

print("Material Data Columns:", material_data.columns)
print("Process Data Columns:", process_data.columns)
print("Environmental Data Columns:", env_data.columns)

# File path for output data
output_file = '../results/output_data.txt'

# Define initial new_data for adaptive updates
new_data = {
    "compressive_strength": [42, 41, 39, 40.5],  # Example observed values
    "tensile_strength": [4.9, 5.1, 5.0],  # Update as needed
    # Add more parameters based on actual observed data
}


def run_ml_bdso(new_data=None):
    with open(output_file, 'w') as f:
        f.write("ML-BDSO Framework Results\n")
        f.write("=" * 40 + "\n")

    # Step 1: Bayesian Inference with optional prior update using new_data
    bayesian_results = bayesian_update(material_data, process_data, env_data, new_data=new_data)
    initial_priors = bayesian_results['priors']
    with open(output_file, 'a') as f:
        f.write("\nBayesian Inference Results:\n")
        for key, (mean, std_dev) in bayesian_results['priors'].items():
            f.write(f"{key}: mean = {mean:.4f}, std_dev = {std_dev:.4f}\n")
        f.write(f"Initial Defect Probability: {bayesian_results['defect_probability']:.4f}\n")

    # Step 2: Monte Carlo Simulation with Adaptive Sampling
    monte_carlo_results = run_monte_carlo(bayesian_results)

    # Check structure and type of monte_carlo_results
    print("Monte Carlo Results Structure:", type(monte_carlo_results))
    if isinstance(monte_carlo_results, list):
        print("Monte Carlo Results (first few entries):", monte_carlo_results[:5])
    else:
        print("Monte Carlo Results:", monte_carlo_results)

    # Calculate the average defect probability for high-risk cases
    high_risk_probs = []
    for run in monte_carlo_results:
        if isinstance(run, dict):  # Ensure run is a dictionary as expected
            avg_prob = np.mean([v for v in run.values() if not np.isnan(v)])
            if avg_prob > 0.1:
                high_risk_probs.append(avg_prob)
        else:
            print("Unexpected structure in monte_carlo_results:", run)  # Debugging unexpected structure
    avg_high_risk_prob = np.mean(high_risk_probs) if high_risk_probs else 0  # Avoid division by zero
    with open(output_file, 'a') as f:
        f.write("\nMonte Carlo Simulation Results:\n")
        f.write(f"Average High-Risk Defect Probability: {avg_high_risk_prob:.4f}\n")

    # Use Monte Carlo results to create defect_data for sensitivity analysis
    defect_data = {"defect_probability": monte_carlo_results}

    # Step 3: Sensitivity Analysis
    sensitivity_results = sensitivity_analysis(defect_data)
    with open(output_file, 'a') as f:
        f.write("\nSensitivity Analysis Results:\n")
        for defect_type, sensitivities in sensitivity_results.items():
            f.write(f"Top 10 Sensitivity Analysis Results for {defect_type}:\n")
            sorted_sensitivities = sorted(sensitivities.items(), key=lambda item: item[1], reverse=True)[:10]
            for param, score in sorted_sensitivities:
                f.write(f"{param}: {score:.4f}\n")
            f.write("\n")

    # Step 4: Feedback-Controlled Optimization
    optimized_parameters = feedback_optimization(sensitivity_results, initial_priors)
    with open(output_file, 'a') as f:
        f.write("\nOptimized Print Parameters:\n")
        for defect_type, params in optimized_parameters.items():
            f.write(f"Optimized Parameters for {defect_type}:\n")
            for param, value in params.items():
                f.write(f"{param}: {value:.4f}\n")
            f.write("\n")

    print("Final optimized parameters saved to output_data.txt")


if __name__ == "__main__":
    run_ml_bdso(new_data=new_data)
