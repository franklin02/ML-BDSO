import matplotlib.pyplot as plt

def feedback_optimization(sensitivity_results):
    """
    Adjusts print parameters dynamically based on sensitivity analysis to optimize
    interlayer bonding and reduce defect probabilities. Saves a bar chart of optimized parameters.
    """
    optimized_params = {param: score * 0.9 for param, score in sensitivity_results.items()}

    # Sort and plot top 10 optimized parameters
    sorted_optimized = dict(sorted(optimized_params.items(), key=lambda item: item[1], reverse=True)[:10])

    plt.figure(figsize=(10, 6))
    plt.bar(sorted_optimized.keys(), sorted_optimized.values(), color='royalblue')
    plt.xticks(rotation=45)
    plt.title("Top 10 Optimized Print Parameters")
    plt.xlabel("Parameter")
    plt.ylabel("Optimized Value")
    plt.tight_layout()
    plt.savefig("../results/optimized_parameters.png")
    plt.close()

    print("Top 10 Optimized Print Parameters:", sorted_optimized)
    return sorted_optimized
