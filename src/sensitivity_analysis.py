import numpy as np
import matplotlib.pyplot as plt

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

    # Plot and save sensitivity scores
    plt.figure(figsize=(10, 6))
    plt.bar(sorted_sensitivities.keys(), sorted_sensitivities.values(), color='seagreen')
    plt.xticks(rotation=45)
    plt.title("Top 10 Sensitivity Scores for Print Parameters")
    plt.xlabel("Parameter")
    plt.ylabel("Sensitivity Score")
    plt.tight_layout()
    plt.savefig("../results/sensitivity_scores.png")
    plt.close()

    print("Top 10 Sensitivity Analysis Results:", sorted_sensitivities)
    return sorted_sensitivities
