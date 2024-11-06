import numpy as np
import matplotlib.pyplot as plt

def feedback_optimization(sensitivity_scores, initial_priors):
    """
    Optimizes parameters based on sensitivity scores by adjusting parameter values to minimize defect probabilities.

    Parameters:
    - sensitivity_scores: Dictionary of sensitivity scores for each defect type.
    - initial_priors: Dictionary of initial prior values for each parameter.

    Returns:
    - optimized_parameters: Dictionary of optimized parameter values for defect mitigation.
    """
    optimized_parameters = {}
    print("Starting parameter optimization based on sensitivity results.")

    for defect_type, sensitivities in sensitivity_scores.items():
        print(f"\nOptimizing parameters for defect type: {defect_type}")
        optimized_params_for_defect = {}

        # Ensure sensitivities contain data
        if not sensitivities:
            print(f"Warning: No sensitivities found for defect type '{defect_type}'")
            continue

        for param, sensitivity_score in sensitivities.items():
            if param in initial_priors:
                # Apply a small adjustment based on sensitivity score
                original_value, uncertainty = initial_priors[param]
                adjustment = original_value - (sensitivity_score * 0.1)  # Adjust sensitivity factor as needed
                optimized_value = max(adjustment, 0)  # Ensure non-negative values
                optimized_params_for_defect[param] = optimized_value
                print(f"Optimized value for {param}: {optimized_value}")
            else:
                print(f"Warning: Parameter {param} not found in initial priors.")

        # Store optimized parameters for each defect type
        optimized_parameters[defect_type] = optimized_params_for_defect

        # Plot optimized parameters
        if optimized_params_for_defect:
            plt.figure(figsize=(12, 8))
            plt.bar(optimized_params_for_defect.keys(), optimized_params_for_defect.values(), color='blue', edgecolor='black')
            plt.xticks(rotation=45, ha="right")
            plt.xlabel("Parameters")
            plt.ylabel("Optimized Value")
            plt.title(f"Optimized Parameters for {defect_type.capitalize()}")
            plt.tight_layout()
            output_path = f"../results/optimized_parameters_{defect_type}.png"
            plt.savefig(output_path)
            plt.close()
            print(f"Saved optimization plot for {defect_type} at {output_path}")
        else:
            print(f"No optimized parameters to plot for {defect_type}")

    return optimized_parameters
