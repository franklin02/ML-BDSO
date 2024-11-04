import matplotlib.pyplot as plt

"""
feedback_optimization.py

This module provides the function `feedback_optimization` for optimizing parameters based on sensitivity results.
The optimization considers sensitivity scores of parameters for each specific defect type to adjust values
in a way that reduces potential defects.

Function:
    feedback_optimization(sensitivity_results, initial_priors): Optimize parameters based on sensitivity results.

"""

def feedback_optimization(sensitivity_results, initial_priors):
    """
    Optimize parameters based on sensitivity results for different defect types.

    Parameters:
    - sensitivity_results (dict): Sensitivity results for each defect type, containing parameters and their scores.
    - initial_priors (dict): Initial prior values and uncertainties for each parameter.

    Returns:
    - dict: Optimized parameters for each defect type.
    """
    print("Starting parameter optimization based on sensitivity results.")  # Debugging
    optimized_parameters = {}

    for defect_type, sensitivities in sensitivity_results.items():
        print(f"\nOptimizing parameters for defect type: {defect_type}")  # Debugging
        defect_optimized_params = {}

        for param, sensitivity_score in sensitivities.items():
            print(f"Optimizing {param} with sensitivity score: {sensitivity_score}")  # Debugging

            # Modify parameter by a factor related to sensitivity score
            if param in initial_priors:
                current_value, uncertainty = initial_priors[param]
                adjustment = 1 / (1 + sensitivity_score)  # Example adjustment
                optimized_value = current_value * adjustment
                defect_optimized_params[param] = optimized_value
                print(f"Optimized value for {param}: {optimized_value}")  # Debugging
            else:
                print(f"Warning: Parameter {param} not found in initial priors.")  # Debugging

        # Store optimized parameters for this defect type
        optimized_parameters[defect_type] = defect_optimized_params
        print(f"Optimized parameters for {defect_type}: {defect_optimized_params}")  # Debugging

    # Plot optimized parameters if data is available
    if optimized_parameters:
        plt.figure(figsize=(12, 8))
        for defect_type, params in optimized_parameters.items():
            plt.bar(params.keys(), params.values(), label=defect_type)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Parameters")
        plt.ylabel("Optimized Value")
        plt.title("Optimized Parameters for Defect Mitigation")
        plt.legend()
        plt.tight_layout()
        plt.savefig("../results/optimized_parameters.png")
        plt.close()
    else:
        print("No optimized parameters to plot.")

    return optimized_parameters
