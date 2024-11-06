import matplotlib.pyplot as plt

def feedback_optimization_refined(sensitivity_scores, initial_priors, defect_type=None):
    """
    Optimizes parameters with targeted adjustments and visual feedback for specified defect types.

    Parameters:
    - sensitivity_scores: dict
    - initial_priors: dict
    - defect_type: str, optional

    Returns:
    - optimized_parameters: dict
    """
    optimized_parameters = {}

    print(f"Starting feedback optimization for defect type: {defect_type}")
    if defect_type not in sensitivity_scores:
        print(f"Error: Defect type '{defect_type}' not found in sensitivity scores.")
        return optimized_parameters

    sensitivities = sensitivity_scores[defect_type]
    shrinkage_parameters = ['shrinkage_rate', 'curing_time', 'water_cement_ratio', 'thermal_expansion_anisotropy']

    for param, sensitivity_score in sensitivities.items():
        if param in initial_priors:
            original_value, uncertainty = initial_priors[param]
            adjustment_factor = 0.25 if defect_type == 'shrinkage_warping' and param in shrinkage_parameters else 0.1
            adjustment = original_value - (sensitivity_score * adjustment_factor)
            optimized_value = max(adjustment, 0)
            optimized_parameters[param] = optimized_value
            print(f"Optimized {param} for {defect_type}: {optimized_value}")
        else:
            print(f"Warning: Parameter {param} not found in initial priors.")

    plt.figure(figsize=(10, 6))
    plt.bar(optimized_parameters.keys(), optimized_parameters.values(), color='blue', edgecolor='black')
    plt.title(f"Optimized Parameters for {defect_type.capitalize()}")
    plt.xlabel("Parameters")
    plt.ylabel("Optimized Value")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"../results/optimized_parameters_{defect_type}.png")
    plt.close()

    return optimized_parameters

# Example usage
if __name__ == "__main__":
    # Example initial priors with a selection of parameters
    initial_priors = {
        "compressive_strength": (40, 5),
        "tensile_strength": (5, 0.5),
        "elastic_modulus": (30000, 1500),
        "aggregate_volume_fraction": (0.6, 0.05),
        "fine_aggregate_size": (0.002, 0.0005),
        "water_cement_ratio": (0.4, 0.05),
        "plastic_viscosity": (50, 10),
        "tensile_adhesion_strength": (0.5, 0.05)
    }

    # Example sensitivity scores for defect types
    example_sensitivity_scores = {
        "delamination": {"compressive_strength": 1.0, "tensile_strength": 0.01, "elastic_modulus": 0.5},
        "voids": {"aggregate_volume_fraction": 0.8, "fine_aggregate_size": 0.03},
        "cracking": {"water_cement_ratio": 0.9, "plastic_viscosity": 0.4, "tensile_adhesion_strength": 0.02}
    }

    # Run optimization for each defect type
    for defect in example_sensitivity_scores.keys():
        optimized_params = feedback_optimization_refined(example_sensitivity_scores, initial_priors, defect_type=defect)
        print(f"Optimized Parameters for {defect.capitalize()}: {optimized_params}")
