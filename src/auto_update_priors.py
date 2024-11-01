import numpy as np
import pandas as pd


def auto_update_priors(current_priors, new_data):
    """
    Updates the priors based on new observed data using Bayesian updating.

    Parameters:
    - current_priors: dict
        A dictionary with parameter names as keys and tuples (mean, std) as values.
        e.g., {"compressive_strength": (40, 5), "tensile_strength": (5, 0.5)}
    - new_data: dict
        A dictionary with parameter names as keys and lists of new observations as values.
        e.g., {"compressive_strength": [42, 43, 38], "tensile_strength": [6, 4.8, 5.2]}

    Returns:
    - updated_priors: dict
        A dictionary with updated prior means and standard deviations.
    """
    updated_priors = {}

    for parameter, (prior_mean, prior_std) in current_priors.items():
        if parameter in new_data:
            # Get new observations for this parameter
            observations = new_data[parameter]
            data_mean = np.mean(observations)
            data_std = np.std(observations)

            # Bayesian update of mean and standard deviation
            updated_mean = (prior_mean * data_std ** 2 + data_mean * prior_std ** 2) / (prior_std ** 2 + data_std ** 2)
            updated_std = np.sqrt((prior_std ** 2 * data_std ** 2) / (prior_std ** 2 + data_std ** 2))

            updated_priors[parameter] = (updated_mean, updated_std)
        else:
            # If no new data, keep the prior as is
            updated_priors[parameter] = (prior_mean, prior_std)

    return updated_priors


# Example usage:
if __name__ == "__main__":
    # Example current priors (mean and std for each parameter)
    current_priors = {
        "compressive_strength": (40, 5),
        "tensile_strength": (5, 0.5),
        # Add other parameters as needed
    }

    # Example new data collected from experiments or simulations
    new_data = {
        "compressive_strength": [42, 43, 38],
        "tensile_strength": [6, 4.8, 5.2],
        # Add other parameters as needed
    }

    # Update priors
    updated_priors = auto_update_priors(current_priors, new_data)
    print("Updated Priors:", updated_priors)
