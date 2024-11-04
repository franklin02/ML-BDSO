import numpy as np
import matplotlib.pyplot as plt

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

def run_monte_carlo(bayesian_results, num_simulations=1000):
    """
    Runs Monte Carlo simulations using defect probability priors from Bayesian inference.
    Implements adaptive sampling for high-risk zones and saves the defect probability histogram
    and trend line.
    """
    defect_probabilities = []
    for i in range(num_simulations):
        run_result = {
            param: np.random.normal(mean, 0.01) if mean is not None else 0.01
            for param, (mean, _) in bayesian_results['priors'].items()
        }
        defect_probabilities.append(run_result)

    # Adaptive sampling for high-risk defect probabilities
    high_risk_probs = [
        np.mean([v for v in run.values() if not np.isnan(v)])
        for run in defect_probabilities if np.mean([v for v in run.values() if not np.isnan(v)]) > 0.1
    ]
    avg_high_risk_prob = np.mean(high_risk_probs) if high_risk_probs else 0.0001  # Small baseline
    print(f"Average high-risk defect probability: {avg_high_risk_prob:.4f} (dimensionless)")

    # Plot Monte Carlo defect probability distribution
    all_probabilities = [np.mean([v for v in run.values() if not np.isnan(v)]) for run in defect_probabilities]
    plt.figure(figsize=(10, 6))
    plt.hist(all_probabilities, bins=20, color='lightcoral', edgecolor='black')
    plt.title("Monte Carlo Defect Probability Distribution")
    plt.xlabel("Defect Probability (dimensionless)")
    plt.ylabel("Frequency")
    plt.savefig("../results/monte_carlo_defect_probability_distribution.png")
    plt.close()

    # Plot trend of defect probabilities over simulations
    plt.figure(figsize=(10, 6))
    plt.plot(all_probabilities, color='blue', linestyle='-', marker='o', markersize=3)
    plt.title("Defect Probability Trend Over Simulations")
    plt.xlabel("Simulation Run")
    plt.ylabel("Defect Probability (dimensionless)")
    plt.savefig("../results/defect_probability_trend.png")
    plt.close()

    # Organize defect data for specific types (e.g., cracking, delamination, voids) if applicable
    defect_data = {
        "defect_probability": defect_probabilities
        # You may add more specific defect types if desired by filtering parameters
    }

    return defect_data
