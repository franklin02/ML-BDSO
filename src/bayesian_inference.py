import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from auto_update_priors import auto_update_priors  # Importing the new function

def bayesian_update(material_data, process_data, env_data, new_data=None):
    """
    Initializes Bayesian priors for defect probabilities based on input data and performs initial
    Bayesian inference to estimate initial defect probabilities. Optionally updates priors based on new data.

    Parameters:
    - material_data, process_data, env_data: DataFrames containing parameter values and uncertainties.
    - new_data: dict, optional
        Dictionary containing new observations for parameters to update priors.
    """
    # Dictionary of parameter units
    parameter_units = {
        "compressive_strength": "MPa",
        "tensile_strength": "MPa",
        "elastic_modulus": "MPa",
        "fiber_content": "(dimensionless)",
        "aggregate_volume_fraction": "(dimensionless)",
        "fine_aggregate_size": "m",
        "coarse_aggregate_size": "m",
        "aggregate_shape": "(dimensionless)",
        "aggregate_alignment": "(dimensionless)",
        "shrinkage_rate": "(dimensionless)",
        "thermal_conductivity": "W/(m·K)",
        "fresh_concrete_flow_rate": "m³/s",
        "water_cement_ratio": "(dimensionless)",
        "initial_yield_stress": "Pa",
        "plastic_viscosity": "Pa·s",
        "thixotropy_index": "(dimensionless)",
        "structural_build_up_rate": "Pa/s",
        "viscosity_ratio": "(dimensionless)",
        "temperature_sensitivity_of_viscosity": "Pa·s/°C",
        "tensile_adhesion_strength": "MPa",
        "creep_compliance": "(dimensionless)",
        "elastic_recovery": "(dimensionless)",
        "surface_tension": "N/m",
        "rate_of_hydration": "(dimensionless)",
        "sedimentation_rate": "(dimensionless)",
        "interlayer_shear_strength": "MPa",
        "interlayer_cohesion": "(dimensionless)",
        "bond_line_toughness": "J/m²",
        "differential_shrinkage_rate": "(dimensionless)",
        "thermal_expansion_anisotropy": "1/°C",
        "fracture_toughness_parallel": "MPa·m^0.5",
        "fracture_toughness_perpendicular": "MPa·m^0.5",
        "interlayer_porosity": "%",
        "fiber_orientation_anisotropy": "(dimensionless)",
        "micro_interlocking_potential": "(dimensionless)",
        "curing_gradient_across_layers": "(dimensionless)",
        "interlayer_tensile_strength": "MPa",
        "plasticity_index_interface": "(dimensionless)",
        "modulus_gradient_interface": "MPa",
        "interlayer_bonding_energy": "J/m²",
        "interfacial_surface_roughness": "µm",
        "layer_height": "m",
        "print_speed": "m/s",
        "nozzle_orientation": "degrees",
        "curing_time": "hours",
        "extrusion_pressure": "MPa",
        "layer_width": "m",
        "printing_orientation": "degrees",
        "reinforcement_application_timing": "minutes",
        "nozzle_temperature_control": "°C",
        "layer_compaction_rate": "(dimensionless)",
        "waiting_time_between_layers": "minutes",
        "temperature": "°C",
        "humidity": "%",
        "wind_speed": "m/s",
        "ambient_light_exposure": "Lux",
        "vibration_level": "(dimensionless)"
    }

    # Convert 'value' and 'uncertainty' columns to numeric, handling errors as NaN
    material_data['value'] = pd.to_numeric(material_data['value'], errors='coerce')
    material_data['uncertainty'] = pd.to_numeric(material_data['uncertainty'], errors='coerce')
    process_data['value'] = pd.to_numeric(process_data['value'], errors='coerce')
    process_data['uncertainty'] = pd.to_numeric(process_data['uncertainty'], errors='coerce')
    env_data['value'] = pd.to_numeric(env_data['value'], errors='coerce')
    env_data['uncertainty'] = pd.to_numeric(env_data['uncertainty'], errors='coerce')

    # Initialize priors based on input data
    priors = {}
    default_value = 0.01  # Default if parameter data is missing or non-numeric
    default_uncertainty = 0.1  # Default uncertainty if missing

    for data, name in zip([material_data, process_data, env_data], ["Material", "Process", "Environmental"]):
        for index, row in data.iterrows():
            parameter = row['parameter']
            value = row['value']
            uncertainty = row['uncertainty']

            # Handle categorical values with consistent defaults
            if isinstance(value, str):
                if parameter == 'aggregate_shape':
                    value = 1 if value == 'angular' else 0.5
                elif parameter == 'aggregate_alignment':
                    value = 1 if value == 'random' else 0.75
                print(f"Converted categorical value for {parameter}: {value}")

            # Assign default values if value or uncertainty is missing
            if pd.isna(value):
                print(f"Assigning default value for {parameter}")
                value = default_value
            if pd.isna(uncertainty):
                print(f"Assigning default uncertainty for {parameter}")
                uncertainty = default_uncertainty

            # Assign prior with the (value, uncertainty) pair
            priors[parameter] = (value, uncertainty)
            print(f"Assigned Prior for {parameter}: Value={value}, Uncertainty={uncertainty}")

    # Verify if all parameters were assigned priors
    print("\nFinal Priors:", priors)

    # Auto-update priors if new data is provided
    if new_data:
        current_priors = {
            param: (np.mean(priors[param]), max(np.std(priors[param]), 0.01))
            for param in priors if param in new_data and isinstance(priors[param], tuple)
        }
        updated_priors = auto_update_priors(current_priors, new_data)
        if updated_priors:
            priors.update(updated_priors)
            print("Updated Priors with New Data:", priors)

    # Ensure defect_probability has a non-zero initial baseline
    valid_priors = [abs(priors[key][0]) for key in priors if isinstance(priors[key][0], (int, float)) and not np.isnan(priors[key][0])]
    defect_probability = np.nanmean(valid_priors) / 10000 if valid_priors else 0.0001  # Small baseline
    print("Initial defect probability:", defect_probability)

    # Plot initial defect probability distribution
    plt.figure(figsize=(10, 6))
    plt.hist(valid_priors, bins=15, color='lightblue', edgecolor='black')
    plt.title("Initial Defect Probability Distribution (Scaled)")
    plt.xlabel("Defect Probability (dimensionless)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("../results/initial_defect_probability_distribution.png")
    plt.close()

    # Split parameters for two separate plots, ensuring values are numeric
    param_names = [param for param in priors.keys() if isinstance(priors[param][0], (int, float)) and not np.isnan(priors[param][0])]
    prior_values = [priors[param][0] for param in param_names]
    midpoint = len(param_names) // 2

    # First half of parameters
    plt.figure(figsize=(12, 8))
    bars = plt.bar(
        [f"{param_names[i]} ({parameter_units.get(param_names[i], 'unknown unit')})" for i in range(midpoint)],
        prior_values[:midpoint],
        color='skyblue', alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.title("Bayesian Inference Results for Parameters - Part 1")
    plt.xlabel("Parameters")
    plt.ylabel("Inferred Prior Value")
    for bar, value in zip(bars, prior_values[:midpoint]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{value:.2f}", ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig("../results/bayesian_inference_results_part1.png")
    plt.close()

    # Second half of parameters
    plt.figure(figsize=(12, 8))
    bars = plt.bar(
        [f"{param_names[i]} ({parameter_units.get(param_names[i], 'unknown unit')})" for i in range(midpoint, len(param_names))],
        prior_values[midpoint:],
        color='skyblue', alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.title("Bayesian Inference Results for Parameters - Part 2")
    plt.xlabel("Parameters")
    plt.ylabel("Inferred Prior Value")
    for bar, value in zip(bars, prior_values[midpoint:]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{value:.2f}", ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig("../results/bayesian_inference_results_part2.png")
    plt.close()

    # Return updated priors and defect probability
    bayesian_results = {
        'priors': priors,
        'defect_probability': defect_probability
    }
    return bayesian_results
