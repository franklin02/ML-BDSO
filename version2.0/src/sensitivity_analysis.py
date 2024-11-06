import numpy as np
import logging

def sensitivity_analysis_by_defect(defect_data, initial_priors, defect_type):
    """
    Performs sensitivity analysis specifically for a given defect type, identifying top
    parameters influencing the defect's probability.

    Parameters:
    - defect_data: dict
    - initial_priors: dict
    - defect_type: str

    Returns:
    - defect_sensitivity_results: dict
    """
    defect_sensitivity_results = {}

    if defect_type not in defect_data:
        logging.error(f"Defect type '{defect_type}' not found in defect data.")
        return defect_sensitivity_results

    data = defect_data[defect_type]
    scores = {param: 0 for param in initial_priors.keys()}

    shrinkage_parameters = ['shrinkage_rate', 'curing_time', 'water_cement_ratio', 'thermal_expansion_anisotropy']
    weight_multiplier = 1.7 if defect_type == 'shrinkage_warping' else 1.0  # Increased multiplier for shrinkage parameters

    for param in scores.keys():
        param_data = [entry.get(param, np.nan) for entry in data if isinstance(entry, dict)]
        param_data = [value for value in param_data if not np.isnan(value)]

        if not param_data:
            logging.warning(f"No valid data for parameter '{param}' in defect type '{defect_type}'")
            continue

        sensitivity_score = np.var(param_data)
        if param in shrinkage_parameters:
            sensitivity_score *= weight_multiplier

        scores[param] = sensitivity_score

    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)[:10])
    defect_sensitivity_results[defect_type] = sorted_scores

    return defect_sensitivity_results


# Example usage
if __name__ == "__main__":
    # Example initial priors for sensitivity analysis with more parameters
    initial_priors = {
        "compressive_strength": (40, 5),
        "tensile_strength": (5, 0.5),
        "elastic_modulus": (30000, 1500),
        "aggregate_type": (1, 0.2),
        "fiber_content": (0.03, 0.005),
        "aggregate_volume_fraction": (0.6, 0.05),
        "fine_aggregate_size": (0.002, 0.0005),
        "coarse_aggregate_size": (0.01, 0.001),
        "aggregate_shape": (1, 0.1),
        "aggregate_alignment": (1, 0.15),
        "shrinkage_rate": (0.01, 0.002),
        "thermal_conductivity": (1.5, 0.3),
        "fresh_concrete_flow_rate": (0.05, 0.01),
        "water_cement_ratio": (0.4, 0.05),
        "initial_yield_stress": (1000, 200),
        "plastic_viscosity": (50, 10),
        "thixotropy_index": (1.2, 0.1),
        "structural_build_up_rate": (5, 0.5),
        "viscosity_ratio": (0.8, 0.05),
        "temperature_sensitivity_of_viscosity": (0.02, 0.005),
        "tensile_adhesion_strength": (0.5, 0.05)
    }

    # Comprehensive example defect data structured by defect type
    example_defect_data = {
        "delamination": [
            {"compressive_strength": 41, "tensile_strength": 5, "elastic_modulus": 30000, 
             "aggregate_type": 1, "fiber_content": 0.03, "aggregate_volume_fraction": 0.6},
            {"compressive_strength": 39, "tensile_strength": 4.8, "elastic_modulus": 29000, 
             "aggregate_type": 0.9, "fiber_content": 0.025, "aggregate_volume_fraction": 0.65},
        ],
        "voids": [
            {"compressive_strength": 35, "tensile_strength": 4.5, "elastic_modulus": 28000, 
             "fiber_content": 0.03, "fine_aggregate_size": 0.002, "coarse_aggregate_size": 0.01},
            {"compressive_strength": 36, "tensile_strength": 4.7, "elastic_modulus": 27000, 
             "fiber_content": 0.025, "fine_aggregate_size": 0.0025, "coarse_aggregate_size": 0.009},
        ],
        "cracking": [
            {"compressive_strength": 42, "tensile_strength": 6, "shrinkage_rate": 0.012, 
             "thermal_conductivity": 1.6, "water_cement_ratio": 0.42, "structural_build_up_rate": 5.1},
            {"compressive_strength": 40, "tensile_strength": 5.8, "shrinkage_rate": 0.011, 
             "thermal_conductivity": 1.7, "water_cement_ratio": 0.43, "structural_build_up_rate": 5.0},
        ]
    }

    # Run sensitivity analysis for each defect type
    for defect in example_defect_data.keys():
        sensitivity_results = sensitivity_analysis_by_defect(example_defect_data, initial_priors, defect_type=defect)
        print(f"Sensitivity Results for {defect.capitalize()}: {sensitivity_results}")
