import numpy as np
import matplotlib.pyplot as plt

def sensitivity_analysis(defect_data):
    """
    Conducts sensitivity analysis on the defect data by calculating sensitivity scores
    for each parameter's contribution to specific defect probabilities.

    Parameters:
    - defect_data: Dictionary containing defect types as keys and defect-related parameters as sub-dictionaries.

    Returns:
    - sensitivity_scores: Dictionary of sensitivity scores for each defect type, sorted in descending order.
    """
    sensitivity_scores = {}
    print("Starting sensitivity analysis with defect data:")
    print(defect_data)  # Debugging statement to check input structure

    # Ensure defect_data has the correct structure for analysis
    if isinstance(defect_data, list):
        defect_data_dict = {"defect_probability": defect_data}
        defect_data = defect_data_dict

    # Calculate sensitivity scores for each defect type
    for defect_type, parameters in defect_data.items():
        print(f"Analyzing defect type: {defect_type}")
        sensitivities = {}

        # Check if parameters are correctly structured
        if not isinstance(parameters, list) or len(parameters) == 0:
            print(f"Warning: No parameter data found for defect type '{defect_type}'")
            continue

        # Calculate sensitivity scores for each parameter
        for param, defect_prob in parameters[0].items():
            print(f"Processing parameter: {param}, Defect Probability: {defect_prob}")
            try:
                # Calculate the sensitivity score based on the difference from the mean
                sensitivity_score = np.abs(defect_prob - np.mean([run.get(param, 0) for run in parameters if param in run]))
                sensitivities[param] = sensitivity_score
                print(f"Sensitivity score for {param}: {sensitivity_score}")  # Debugging line
            except Exception as e:
                print(f"Error calculating sensitivity for {param}: {e}")
                continue

        # Sort and store the top sensitivities
        sorted_sensitivities = dict(sorted(sensitivities.items(), key=lambda item: item[1], reverse=True)[:10])
        sensitivity_scores[defect_type] = sorted_sensitivities
        print(f"Top 10 sensitivities for {defect_type}: {sorted_sensitivities}")

        # Plot sensitivity scores if data is non-empty
        if sorted_sensitivities:
            plt.figure(figsize=(12, 8))
            plt.bar(sorted_sensitivities.keys(), sorted_sensitivities.values(), color='purple', edgecolor='black')
            plt.xticks(rotation=45, ha="right")
            plt.xlabel("Parameters")
            plt.ylabel("Sensitivity Score")
            plt.title(f"Sensitivity Analysis for {defect_type.capitalize()}")
            plt.subplots_adjust(bottom=0.3)  # Adjust bottom margin for label space
            output_path = f"../results/sensitivity_scores_{defect_type}.png"
            plt.savefig(output_path)
            plt.close()
            print(f"Saved plot for {defect_type} at {output_path}")  # Confirmation message
        else:
            print(f"No sensitivity scores to plot for {defect_type}")

    return sensitivity_scores
