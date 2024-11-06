import numpy as np
import pandas as pd
from auto_update_priors import auto_update_priors_dynamic


def classify_defect_type(priors, thresholds=None):
    """
    Classifies defect types based on Bayesian priors for relevant parameters.

    Parameters:
    - priors: dict
        Dictionary of parameter names and their inferred prior values (mean, std).
    - thresholds: dict, optional
        Dictionary defining threshold ranges for defect types.

    Returns:
    - defect_type: str
        Classified defect type based on the thresholds and prior values.
    """
    if thresholds is None:
        thresholds = {
            'porosity': {'aggregate_volume_fraction': (0.6, 0.7), 'fiber_content': (0.02, 0.03),
                         'layer_compaction_rate': (0.5, 0.8), 'water_cement_ratio': (0.45, 0.55)},
            'delamination': {'elastic_modulus': (25000, 40000), 'initial_yield_stress': (800, 1200)},
            'voids': {'aggregate_volume_fraction': (0.5, 0.65), 'fiber_content': (0.01, 0.04)},
            'cracking': {'tensile_strength': (4.5, 6), 'shrinkage_rate': (0.005, 0.02)},
            'interlayer_weakness': {'interlayer_shear_strength': (0.2, 0.4), 'interlayer_tensile_strength': (0.3, 0.5),
                                    'fiber_orientation_anisotropy': (0.5, 0.7), 'aggregate_alignment': (0.7, 1.0)},
            'shrinkage_warping': {'shrinkage_rate': (0.01, 0.02), 'curing_time': (12, 20),
                                  'water_cement_ratio': (0.5, 0.6), 'thermal_expansion_anisotropy': (0.0003, 0.0005)}
        }

    defect_type = "unknown"

    for defect, criteria in thresholds.items():
        match = all(
            criteria[param][0] <= priors.get(param, (0,))[0] <= criteria[param][1]
            for param in criteria
        )
        if match:
            defect_type = defect
            break

    return defect_type


def bayesian_update_with_classification(material_data, process_data, env_data, new_data=None, thresholds=None):
    """
    Initializes Bayesian priors for defect probabilities based on input data, performs Bayesian inference
    for initial defect probabilities, and classifies defect types based on updated priors.

    Parameters:
    - material_data, process_data, env_data: DataFrames containing parameter values and uncertainties.
    - new_data: dict, optional
        Dictionary containing new observations for parameters to update priors.
    - thresholds: dict, optional
        Threshold values for defect classification.

    Returns:
    - results: dict
        Contains updated priors, defect probability, and classified defect type.
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

    # Initialize priors
    priors = {}
    default_value, default_uncertainty = 0.01, 0.1
    for data in [material_data, process_data, env_data]:
        for _, row in data.iterrows():
            param = row['parameter']
            try:
                value = float(row['value'])
                uncertainty = float(row['uncertainty'])
            except ValueError:
                value, uncertainty = default_value, default_uncertainty
            priors[param] = (value, uncertainty)

    # Update priors if new data is provided
    if new_data:
        updated_priors = auto_update_priors_dynamic(priors, new_data)
        priors.update(updated_priors)

    defect_type = classify_defect_type(priors, thresholds=thresholds)

    valid_priors = [abs(priors[key][0]) for key in priors if
                    isinstance(priors[key][0], (int, float)) and not np.isnan(priors[key][0])]
    defect_probability = np.nanmean(valid_priors) / 10000 if valid_priors else 0.0001

    results = {
        'priors': priors,
        'defect_probability': defect_probability,
        'defect_type': defect_type
    }

    return results


# Example usage
if __name__ == "__main__":
    example_material_data = pd.DataFrame({
        'parameter': ['compressive_strength', 'tensile_strength', 'elastic_modulus'],
        'value': [40, 5, 30000],
        'uncertainty': [5, 0.5, 1500]
    })

    example_process_data = pd.DataFrame({
        'parameter': ['layer_height', 'print_speed', 'nozzle_orientation'],
        'value': [0.005, 0.05, 90],
        'uncertainty': [0.001, 0.01, 5]
    })

    example_env_data = pd.DataFrame({
        'parameter': ['temperature', 'humidity', 'wind_speed'],
        'value': [25, 50, 0],
        'uncertainty': [2, 5, 0.1]
    })

    update_results = bayesian_update_with_classification(example_material_data, example_process_data, example_env_data)
    print("Updated Priors:", update_results['priors'])
    print("Defect Probability:", update_results['defect_probability'])
    print("Defect Type:", update_results['defect_type'])
