import logging
import numpy as np
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def sensitivity_analysis(defect_data, initial_priors):
    """
    Perform sensitivity analysis on defect data.

    Parameters:
        defect_data (dict): Dictionary with defect types as keys and associated Monte Carlo results.
        initial_priors (dict): Dictionary of priors for each parameter.

    Returns:
        dict: Sensitivity scores for each defect type.
    """
    sensitivity_scores = {}

    # Log the structure of defect_data at the start
    logging.debug("Starting sensitivity analysis with defect_data keys: %s", list(defect_data.keys()))

    for defect_type, defect_values in defect_data.items():
        logging.debug("Analyzing defect type: %s with %d data points", defect_type, len(defect_values))

        if not isinstance(defect_values, list) or len(defect_values) == 0:
            logging.warning("Defect type '%s' has an unexpected structure or no data", defect_type)
            continue

        sensitivity_scores[defect_type] = {param: 0 for param in initial_priors.keys()}

        # Extract and initialize sensitivity scores for parameters
        parameter_keys = list(initial_priors.keys())
        initial_sensitivity = {param: 0 for param in parameter_keys}
        sensitivity_scores[defect_type] = initial_sensitivity

        # Calculate sensitivity scores
        for param in parameter_keys:
            values = [
                run.get(param, np.nan) for run in defect_values if isinstance(run, dict) and param in run
            ]
            logging.debug("Collected %d values for parameter '%s' in defect type '%s'", len(values), param, defect_type)

            # Filter out NaN values
            valid_values = [v for v in values if not np.isnan(v)]
            if len(valid_values) == 0:
                logging.warning("Parameter %s has no valid data in defect type %s", param, defect_type)
                continue

            # Compute sensitivity score as standard deviation / mean (relative variability)
            sensitivity_score = np.std(valid_values) / np.mean(valid_values) if np.mean(valid_values) != 0 else 0
            sensitivity_scores[defect_type][param] = sensitivity_score
            logging.debug("Sensitivity score for %s: %.4f", param, sensitivity_score)

        # Sort and save top sensitivities if available
        sorted_sensitivities = sorted(sensitivity_scores[defect_type].items(), key=lambda item: item[1], reverse=True)[:10]
        sensitivity_scores[defect_type] = dict(sorted_sensitivities)
        logging.debug("Top sensitivities for %s: %s", defect_type, sensitivity_scores[defect_type])

        # Plotting sensitivity results
        if len(sensitivity_scores[defect_type]) > 0:
            plt.figure(figsize=(10, 6))
            plt.barh(list(sensitivity_scores[defect_type].keys()), list(sensitivity_scores[defect_type].values()))
            plt.xlabel("Sensitivity Score")
            plt.ylabel("Parameter")
            plt.title(f"Top Sensitivity Scores for {defect_type}")
            plt.tight_layout()
            plot_filename = f"../results/sensitivity_scores_{defect_type}.png"
            plt.savefig(plot_filename)
            logging.info("Saved sensitivity plot for %s as %s", defect_type, plot_filename)
            plt.close()
        else:
            logging.warning("No valid sensitivities to plot for defect type: %s", defect_type)

    logging.debug("Final sensitivity results: %s", sensitivity_scores)
    return sensitivity_scores
