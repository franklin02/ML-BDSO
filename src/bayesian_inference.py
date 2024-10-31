import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def bayesian_update(material_data, process_data, env_data):
    """
    Initializes Bayesian priors for defect probabilities based on input data and performs initial
    Bayesian inference to estimate initial defect probabilities. Visualizes each parameter's prior
    distribution, separately displaying elastic modulus, and overall initial defect probability
    distribution.
    """
    # Initialize priors based on material, process, and environmental data
    priors = {}
    for data in [material_data, process_data, env_data]:
        for index, row in data.iterrows():
            try:
                # Handle categorical parameters and standard float parameters
                if row['parameter'] == 'aggregate_shape':
                    value = 1 if row['value'] == 'angular' else 0.5
                elif row['parameter'] == 'aggregate_alignment':
                    value = 1 if row['value'] == 'random' else 0.75
                else:
                    value = float(row['value'])
                uncertainty = float(row['uncertainty'])
                priors[row['parameter']] = np.random.normal(value, uncertainty)
            except ValueError:
                print(f"Skipping non-numeric row: {row['parameter']}")

    # Calculate and scale down the initial defect probability
    defect_probability = np.mean([abs(priors[key]) for key in priors if isinstance(priors[key], float)]) / 10000
    print("Initial defect probability:", defect_probability)

    # Separate elastic modulus from other parameters
    elastic_modulus_value = priors.pop('elastic_modulus', None)

    # Visualize the elastic modulus on its own plot
    plt.figure(figsize=(5, 5))
    plt.bar(['Elastic Modulus'], [elastic_modulus_value], color='lightcoral')
    plt.text(0, elastic_modulus_value, f"{elastic_modulus_value:.2f}", ha='center', va='bottom')
    plt.title("Elastic Modulus")
    plt.ylabel("Inferred Prior Value")
    plt.tight_layout()
    plt.savefig("../results/elastic_modulus.png")
    plt.close()

    # Visualize each remaining parameter's inferred prior distribution
    plt.figure(figsize=(12, 8))
    param_names = list(priors.keys())
    prior_values = list(priors.values())
    bars = plt.bar(param_names, prior_values, color='skyblue', alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.title("Bayesian Inference Results for Parameters (Excluding Elastic Modulus)")
    plt.xlabel("Parameters")
    plt.ylabel("Inferred Prior Value")

    # Annotate each bar with its exact value
    for bar, value in zip(bars, prior_values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{value:.2f}", ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig("../results/bayesian_inference_results.png")
    plt.close()

    # Plot and save initial defect probability distribution with more bins for spread
    plt.figure(figsize=(10, 6))
    plt.hist([abs(priors[key]) for key in priors if isinstance(priors[key], float)], bins=15, color='lightblue',
             edgecolor='black')
    plt.title("Initial Defect Probability Distribution (Scaled)")
    plt.xlabel("Defect Probability")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("../results/initial_defect_probability_distribution.png")
    plt.close()

    # Return updated priors as Bayesian results
    bayesian_results = {
        'priors': priors,
        'defect_probability': defect_probability
    }
    return bayesian_results
