import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from auto_update_priors import auto_update_priors

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

    # Convert columns to numeric, handling errors as NaN
    for data in [material_data, process_data, env_data]:
        data['value'] = pd.to_numeric(data['value'], errors='coerce')
        data['uncertainty'] = pd.to_numeric(data['uncertainty'], errors='coerce')

    # Initialize priors with defaults for missing data
    priors = {}
    default_value, default_uncertainty = 0.01, 0.1
    for data in [material_data, process_data, env_data]:
        for _, row in data.iterrows():
            param = row['parameter']
            value = row['value'] if pd.notna(row['value']) else default_value
            uncertainty = row['uncertainty'] if pd.notna(row['uncertainty']) else default_uncertainty
            priors[param] = (value, uncertainty)

    # Update priors if new data is provided
    if new_data:
        updated_priors = auto_update_priors(priors, new_data)
        priors.update(updated_priors)

    # Calculate defect probability
    valid_priors = [abs(priors[key][0]) for key in priors if isinstance(priors[key][0], (int, float)) and not np.isnan(priors[key][0])]
    defect_probability = np.nanmean(valid_priors) / 10000 if valid_priors else 0.0001

    # Plot initial defect probability distribution
    plt.figure(figsize=(10, 6))
    plt.hist(valid_priors, bins=15, color='lightblue', edgecolor='black')
    plt.title("Initial Defect Probability Distribution (Scaled)")
    plt.xlabel("Defect Probability (dimensionless)")
    plt.ylabel("Frequency")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.15)  # Adjust margins
    plt.savefig("../results/initial_defect_probability_distribution.png")
    plt.close()

    # Splitting parameters into multiple parts if needed
    param_names = [param for param in priors if isinstance(priors[param][0], (int, float)) and not np.isnan(priors[param][0])]
    prior_values = [priors[param][0] for param in param_names]
    max_params_per_plot = 15  # Define maximum parameters per plot for clarity

    # Calculate number of parts based on max_params_per_plot
    num_parts = (len(param_names) + max_params_per_plot - 1) // max_params_per_plot

    for part in range(num_parts):
        start = part * max_params_per_plot
        end = min(start + max_params_per_plot, len(param_names))  # Ensure end does not exceed list length
        plt.figure(figsize=(12, 8))
        bars = plt.bar(
            [f"{param_names[i]} ({parameter_units.get(param_names[i], 'unknown unit')})" for i in range(start, end)],
            prior_values[start:end],
            color='skyblue', alpha=0.7)
        plt.xticks(rotation=45, ha="right")
        plt.yscale('log')
        plt.title(f"Bayesian Inference Results for Parameters - Part {part + 1}")
        plt.xlabel("Parameters")
        plt.ylabel("Inferred Prior Value (Log Scale)")
        for bar, value in zip(bars, prior_values[start:end]):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{value:.2f}", ha='center', va='bottom')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)  # Adjust margins to prevent overlap
        plt.savefig(f"../results/bayesian_inference_results_part{part + 1}.png")
        plt.close()

    return {'priors': priors, 'defect_probability': defect_probability}
