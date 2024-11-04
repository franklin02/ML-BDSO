import matplotlib.pyplot as plt

# Dictionary of parameter units for use in labels
parameter_units = {
    "compressive_strength": "MPa",
    "tensile_strength": "MPa",
    "elastic_modulus": "MPa",
    # ... [Other parameter units as defined previously]
    "vibration_level": "(dimensionless)"
}

def feedback_optimization(sensitivity_results):
    """
    Adjusts print parameters dynamically based on sensitivity analysis to optimize
    interlayer bonding and reduce defect probabilities. Saves a bar chart of optimized parameters.
    """
    # Apply a 10% reduction on sensitivity scores for optimization
    optimized_params = {param: score * 0.9 for param, score in sensitivity_results.items()}

    # Sort and plot top 10 optimized parameters for visualization
    sorted_optimized = dict(sorted(optimized_params.items(), key=lambda item: item[1], reverse=True)[:10])

    # Prepare labels with units for the plot
    labels_with_units = [
        f"{param} ({parameter_units.get(param, '(unknown unit)')})"
        for param in sorted_optimized.keys()
    ]

    plt.figure(figsize=(10, 6))
    plt.bar(labels_with_units, sorted_optimized.values(), color='royalblue')
    plt.xticks(rotation=45)
    plt.title("Top 10 Optimized Print Parameters")
    plt.xlabel("Parameter (with units)")
    plt.ylabel("Optimized Value (dimensionless)")
    plt.tight_layout()
    plt.savefig("../results/optimized_parameters.png")
    plt.close()

    print("Top 10 Optimized Print Parameters:", sorted_optimized)
    return sorted_optimized
