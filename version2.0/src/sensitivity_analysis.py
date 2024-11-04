import numpy as np
import matplotlib.pyplot as plt

# Complete dictionary of parameter units for sensitivity analysis
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

def sensitivity_analysis(monte_carlo_results):
    """
    Performs sensitivity analysis on Monte Carlo results to determine the parameters most
    impacting defect probabilities. Plots and saves sensitivity scores.
    """
    sensitivity_scores = {}
    for result in monte_carlo_results:
        for param, defect_prob in result.items():
            if param not in sensitivity_scores:
                sensitivity_scores[param] = []
            sensitivity_scores[param].append(defect_prob)

    # Calculate variance for each parameter as sensitivity score
    final_sensitivity_scores = {param: np.var(probs) for param, probs in sensitivity_scores.items()}

    # Sort and take top 10 scores for visualization
    sorted_sensitivities = dict(sorted(final_sensitivity_scores.items(), key=lambda item: item[1], reverse=True)[:10])

    # Prepare labels with units for the plot
    labels_with_units = [
        f"{param} ({parameter_units.get(param, '(unknown unit)')})"
        for param in sorted_sensitivities.keys()
    ]

    # Plot sensitivity scores with units
    plt.figure(figsize=(10, 6))
    plt.bar(labels_with_units, sorted_sensitivities.values(), color='seagreen')
    plt.xticks(rotation=45)
    plt.title("Top 10 Sensitivity Scores for Print Parameters")
    plt.xlabel("Parameter (with units)")
    plt.ylabel("Sensitivity Score (variance, dimensionless)")
    plt.tight_layout()
    plt.savefig("../results/sensitivity_scores.png")
    plt.close()

    print("Top 10 Sensitivity Analysis Results:", sorted_sensitivities)
    return sorted_sensitivities
