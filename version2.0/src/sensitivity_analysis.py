import numpy as np
import matplotlib.pyplot as plt
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)


# Function for sensitivity analysis
def sensitivity_analysis(defect_data, initial_priors):
    sensitivity_results = {}

    # Ensure the results directory exists
    results_dir = "../results/"
    os.makedirs(results_dir, exist_ok=True)

    for defect_type, data in defect_data.items():
        # Check if data is a list of dictionaries
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            logging.error(f"Data for defect type '{defect_type}' is not in the expected format.")
            continue

        # Confirm data structure and contents
        print(f"Analyzing defect type '{defect_type}' with {len(data)} samples.")

        # Initialize scores dictionary
        scores = {param: 0 for param in initial_priors.keys()}

        for param in scores.keys():
            # Collect parameter values for this defect type
            param_data = [entry.get(param, np.nan) for entry in data if isinstance(entry, dict)]
            param_data = [value for value in param_data if not np.isnan(value)]

            if not param_data:
                logging.warning(f"Parameter {param} has no valid data in defect type {defect_type}")
                continue

            # Calculate variance for sensitivity score
            scores[param] = np.var(param_data)

            # Plot individual predictions for each parameter
            plt.figure(figsize=(8, 5))
            plt.plot(param_data, label=param)
            plt.title(f"{param} Predictions for {defect_type}")
            plt.xlabel("Sample Index")
            plt.ylabel(param)
            plt.legend()
            plt.tight_layout()
            plt.savefig(os.path.join(results_dir, f"{defect_type}_{param}_predictions.png"))
            plt.close()

        # Sort and save top 10 sensitive parameters based on variance
        sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)[:10])
        sensitivity_results[defect_type] = sorted_scores
        logging.debug("Top sensitivities for %s: %s", defect_type, sorted_scores)

        # Plot top sensitivities
        plt.figure(figsize=(10, 6))
        plt.bar(sorted_scores.keys(), sorted_scores.values())
        plt.title(f"Top 10 Sensitivity Analysis for {defect_type}")
        plt.xlabel("Parameters")
        plt.ylabel("Sensitivity Score (Variance)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(results_dir, f"sensitivity_{defect_type}.png"))
        plt.close()

    logging.debug("Final sensitivity results: %s", sensitivity_results)
    return sensitivity_results


# Example initial_priors dictionary (replace with your actual data)
initial_priors = {
    "compressive_strength": 0,
    "tensile_strength": 0,
    "elastic_modulus": 0,
    "aggregate_type": 0,
    "fiber_content": 0,
    "aggregate_volume_fraction": 0,
    "fine_aggregate_size": 0,
    "coarse_aggregate_size": 0,
    "aggregate_shape": 0,
    "aggregate_alignment": 0,
    # Add any other parameters as needed
}

# Placeholder defect_data structure (replace with actual defect data)
defect_data = {
    "defect_probability": [
        {"compressive_strength": 41, "tensile_strength": 5, "elastic_modulus": 30000, "aggregate_type": 0.01},
        {"compressive_strength": 39, "tensile_strength": 4.8, "elastic_modulus": 29000, "aggregate_type": 0.015},
        # Additional data entries for each sample...
    ]
}

# Confirm defect_data structure before running
print("Defect Data Structure:", defect_data)

# Run sensitivity analysis
sensitivity_results = sensitivity_analysis(defect_data, initial_priors)
