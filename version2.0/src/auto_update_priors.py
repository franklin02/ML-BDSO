import numpy as np


def auto_update_priors_dynamic(current_priors, new_data, defect_type=None, adaptation_factors=None):
    """
    Updates priors based on new data, with optional adjustments based on defect type.

    Parameters:
    - current_priors: dict
    - new_data: dict
    - defect_type: str, optional
    - adaptation_factors: dict, optional

    Returns:
    - updated_priors: dict
    """
    if adaptation_factors is None:
        adaptation_factors = {
            'porosity': 1.3,  # Increased weighting for porosity
            'delamination': 1.1,
            'voids': 1.05,
            'cracking': 1.15
        }

    multiplier = adaptation_factors.get(defect_type, 1.0)
    porosity_params = {'aggregate_volume_fraction', 'fiber_content', 'layer_compaction_rate', 'water_cement_ratio'}
    updated_priors = {}

    for parameter, (prior_mean, prior_std) in current_priors.items():
        if parameter in new_data:
            observations = new_data[parameter]
            data_mean = np.mean(observations)
            data_std = np.std(observations)

            if not isinstance(prior_mean, (int, float)) or not isinstance(prior_std, (int, float)):
                continue  # Skip non-numeric priors

            updated_mean = (prior_mean * data_std ** 2 + data_mean * prior_std ** 2) / (prior_std ** 2 + data_std ** 2)
            updated_std = np.sqrt((prior_std ** 2 * data_std ** 2) / (prior_std ** 2 + data_std ** 2))

            if defect_type == 'porosity' and parameter in porosity_params:
                updated_mean *= multiplier

            updated_priors[parameter] = (updated_mean, updated_std * multiplier)
        else:
            updated_priors[parameter] = (prior_mean, prior_std)

    return updated_priors


# Example usage
if __name__ == "__main__":
    current_priors = {
        "compressive_strength": (40, 5),
        "tensile_strength": (5, 0.5),
    }

    new_data = {
        "compressive_strength": [42, 43, 38],
        "tensile_strength": [6, 4.8, 5.2],
    }

    updated_priors = auto_update_priors_dynamic(current_priors, new_data, defect_type="delamination")
    print("Updated Priors:", updated_priors)
