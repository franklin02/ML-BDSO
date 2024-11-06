import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt
from bayesian_inference import bayesian_update_with_classification
from monte_carlo_simulation import run_monte_carlo
from sensitivity_analysis import sensitivity_analysis_by_defect
from feedback_optimization import feedback_optimization_refined
import os

# Ensure the results directory exists
results_dir = '../results/'
os.makedirs(results_dir, exist_ok=True)

# Load initial data from .txt files
def load_extended_data(material_file, process_file, env_file):
    try:
        material_data = pd.read_csv(material_file, sep='\s+', comment='#', header=0)
        process_data = pd.read_csv(process_file, sep='\s+', comment='#', header=0)
        env_data = pd.read_csv(env_file, sep='\s+', comment='#', header=0)

        consolidated_data = {
            "material": material_data,
            "process": process_data,
            "environment": env_data,
        }

        logging.info("Successfully loaded extended input data for material, process, and environment.")
        return consolidated_data

    except Exception as e:
        logging.error(f"Error loading data files: {e}")
        return None

# File paths for input data
material_file = '../data/material_properties.txt'
process_file = '../data/process_parameters.txt'
env_file = '../data/environmental_conditions.txt'
output_file = os.path.join(results_dir, 'output_data.txt')
new_data = {
    "compressive_strength": [42, 41, 39, 40.5],
    "tensile_strength": [4.9, 5.1, 5.0],
}

logging.basicConfig(level=logging.DEBUG)

# Plotting Functions
def plot_defect_probability(priors, defect_probability):
    plt.figure()
    prior_values = [value[0] for value in priors.values() if isinstance(value[0], (int, float))]
    plt.hist(prior_values, bins=15, color='skyblue', edgecolor='black')
    plt.title("Initial Defect Probability Distribution")
    plt.xlabel("Defect Probability (dimensionless)")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(results_dir, "defect_probability_distribution.png"))
    plt.close()

def plot_monte_carlo_distribution(monte_carlo_results):
    probabilities = [np.mean([v for v in run.values() if not np.isnan(v)]) for run in monte_carlo_results]
    plt.figure()
    plt.hist(probabilities, bins=15, color='purple', edgecolor='black')
    plt.title("Monte Carlo Defect Probability Distribution")
    plt.xlabel("Defect Probability")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(results_dir, "monte_carlo_defect_probability_distribution.png"))
    plt.close()

def plot_defect_probability_trend(monte_carlo_results):
    probabilities = [np.mean([v for v in run.values() if not np.isnan(v)]) for run in monte_carlo_results]
    plt.figure()
    plt.plot(range(len(probabilities)), probabilities, color='blue', marker='o')
    plt.title("Defect Probability Trend Over Simulations")
    plt.xlabel("Simulation Iteration")
    plt.ylabel("Defect Probability")
    plt.savefig(os.path.join(results_dir, "defect_probability_trend.png"))
    plt.close()

def plot_sensitivity_results(sensitivity_results, defect_type):
    top_params, scores = zip(*sensitivity_results[defect_type].items())
    plt.figure(figsize=(10, 6))
    plt.bar(top_params, scores, color='orange', edgecolor='black')
    plt.title(f"Top Sensitivity Analysis Results for {defect_type.capitalize()}")
    plt.xlabel("Parameters")
    plt.ylabel("Sensitivity Score (Variance)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, f"sensitivity_{defect_type}.png"))
    plt.close()

def plot_optimized_parameters(optimized_parameters, defect_type):
    plt.figure(figsize=(10, 6))
    plt.bar(optimized_parameters.keys(), optimized_parameters.values(), color='blue', edgecolor='black')
    plt.title(f"Optimized Parameters for {defect_type.capitalize()}")
    plt.xlabel("Parameters")
    plt.ylabel("Optimized Value")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, f"optimized_parameters_{defect_type}.png"))
    plt.close()

def run_ml_bdso(new_data=None):
    with open(output_file, 'w') as f:
        f.write("ML-BDSO Framework Results\n")
        f.write("=" * 40 + "\n")

    data = load_extended_data(material_file, process_file, env_file)
    if data is None:
        logging.error("Data loading failed. Exiting.")
        return

    material_data = data["material"]
    process_data = data["process"]
    env_data = data["environment"]

    # Step 1: Bayesian Inference with Defect Classification
    bayesian_results = bayesian_update_with_classification(material_data, process_data, env_data, new_data=new_data)
    initial_priors = bayesian_results['priors']
    defect_type = bayesian_results['defect_type']
    defect_probability = bayesian_results['defect_probability']

    # Save initial defect probability distribution plot
    plot_defect_probability(initial_priors, defect_probability)

    with open(output_file, 'a') as f:
        f.write("\nBayesian Inference Results:\n")
        f.write(f"Classified Defect Type: {defect_type}\n")
        for key, (mean, std_dev) in initial_priors.items():
            f.write(f"{key}: mean = {mean:.4f}, std_dev = {std_dev:.4f}\n")
        f.write(f"Initial Defect Probability: {defect_probability:.4f}\n")

    if defect_type == 'unknown':
        logging.warning("Defect type could not be classified. Skipping sensitivity analysis and optimization.")
        with open(output_file, 'a') as f:
            f.write("\nDefect type could not be classified. No further analysis will be performed.\n")
        return

    # Step 2: Monte Carlo Simulation
    monte_carlo_results = run_monte_carlo(bayesian_results)
    defect_data = {defect_type: monte_carlo_results}

    # Plot Monte Carlo Defect Probability Distribution and Trend
    plot_monte_carlo_distribution(monte_carlo_results)
    plot_defect_probability_trend(monte_carlo_results)

    # Step 3: Sensitivity Analysis by Defect Type
    sensitivity_results = sensitivity_analysis_by_defect(defect_data, initial_priors, defect_type=defect_type)
    plot_sensitivity_results(sensitivity_results, defect_type)
    with open(output_file, 'a') as f:
        f.write("\nSensitivity Analysis Results:\n")
        f.write(f"Top 10 Sensitivity Analysis Results for {defect_type}:\n")
        for param, score in sensitivity_results[defect_type].items():
            f.write(f"{param}: {score:.4f}\n")

    # Step 4: Feedback-Controlled Optimization
    optimized_parameters = feedback_optimization_refined(sensitivity_results, initial_priors, defect_type=defect_type)
    plot_optimized_parameters(optimized_parameters, defect_type)
    with open(output_file, 'a') as f:
        f.write("\nOptimized Print Parameters:\n")
        f.write(f"Optimized Parameters for {defect_type}:\n")
        for param, value in optimized_parameters.items():
            f.write(f"{param}: {value:.4f}\n")

if __name__ == "__main__":
    run_ml_bdso(new_data=new_data)
