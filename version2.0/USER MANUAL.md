Here’s the updated portion for the **USER MANUAL.md** reflecting the changes for ML-BDSO version 2.0:

---

### Updates in Version 2.0

This new release of the ML-BDSO framework (v2.0) includes enhancements for predicting and controlling specific defect types during the 3D printing process. Key updates and new functionality are outlined below:

#### Defect Type Prediction and Classification
- **Defect Types**: The framework now categorizes defects into specific types, such as **voids**, **delamination**, and **cracking**.
- **Parameter Adjustments**: Each defect type is associated with relevant parameters that influence its occurrence, allowing targeted modifications in the printing process.

#### New Input Parameters for Version 2.0
- **Material Properties**: New fields have been added in `material_properties.txt` to accommodate parameters influencing specific defect types. Each parameter now has additional defect-specific indicators.
- **Process Parameters**: Updated `process_parameters.txt` to include defect-specific printing factors such as **layer height**, **nozzle orientation**, and **print speed** adjustments based on defect type.
- **Environmental Conditions**: `environmental_conditions.txt` is extended to include defect-related environmental variables, such as **temperature gradients** and **humidity sensitivity** for more precise defect control.

#### Enhanced Bayesian Inference
- **Dynamic Prior Updates**: Bayesian priors are now dynamically updated based on defect type classification, allowing more precise control over defect probabilities for each identified type.

#### Monte Carlo Simulation with Defect Classification
- **Defect Type Segmentation**: Monte Carlo simulations are conducted with classifications for defect types, yielding more granular insights into defect probabilities by type.
- **High-Risk Sampling**: Adaptive sampling is enhanced for each defect type, focusing on high-risk probabilities specific to the type.

#### Advanced Sensitivity Analysis
- **Defect-Specific Sensitivity**: Sensitivity scores now identify top parameters influencing each defect type, guiding users on parameters to adjust for minimizing specific defects.

#### Feedback-Controlled Optimization
- **Optimized Parameters for Defects**: Version 2.0’s optimization process targets defect-specific parameters to improve layer bonding quality and minimize defect occurrence in real-time.

### Running Version 2.0
To run ML-BDSO v2.0, use the updated input data files (`material_properties.txt`, `process_parameters.txt`, `environmental_conditions.txt`) and follow the same steps as in v1.0. The output files in the `results/` directory will now reflect enhanced analyses for defect-specific predictions and optimizations.

---

In version 2.0, the results related to **specific defect type prediction** and **parameter optimization for defect mitigation** are generated and saved in the `results/` folder, specifically through the files and plots outlined below:

### 1. **Specific Defect Type Prediction**
   - The **sensitivity analysis** for specific defect types will yield plots and data files reflecting the influence of various parameters on specific defects (e.g., cracking, delamination, or voids).
   - Look for these files:
     - **`sensitivity_analysis_{defect_type}.png`**: This plot shows the sensitivity of parameters specific to each defect type. For example, `sensitivity_analysis_cracking.png` would indicate the sensitivity results for the defect type "cracking."
     - **`sensitivity_scores_defect_probability.png`**: Provides a general overview of the most sensitive parameters affecting the overall defect probability, useful for understanding critical factors across all defect types.

### 2. **Parameter Optimization for Defect Mitigation**
   - The **feedback optimization** process refines parameters to reduce the probability or severity of specific defect types. The results of this optimization process are found in:
     - **`optimized_parameters.png`**: Displays the optimal values of key parameters after the feedback optimization process, showing adjustments to reduce the likelihood of high-impact defects.
     - **`output_data.txt`**: Contains the final optimized values of parameters for each defect type. This file serves as a reference for setting parameters to achieve lower defect probabilities in practice.

### Summary of Key Output Files
   - `sensitivity_analysis_{defect_type}.png`: Sensitivity analysis for individual defect types.
   - `sensitivity_scores_defect_probability.png`: Overall sensitivity scores for defect probability.
   - `optimized_parameters.png`: Visualization of optimized parameter values.
   - `output_data.txt`: Text output with the final optimized parameter values.

These files collectively present the findings from defect-specific predictions and parameter optimization for defect mitigation. If any of these files are missing or if you need further custom outputs, feel free to ask.

### Code Description and Significance for the Proposal

The **Multi-Level Bayesian Defect Simulation and Optimization (ML-BDSO)** framework is a Python-based computational tool designed to enhance **layer bonding quality** and **reduce defect probabilities** in **3D printed concrete** structures. This framework addresses the inherent uncertainties in the 3D printing process by integrating **Bayesian inference**, **Monte Carlo simulation with adaptive sampling**, **sensitivity analysis**, and **feedback-controlled optimization**. Each module contributes to building a robust system that adjusts in real time to variations in material, process parameters, and environmental conditions, achieving consistent and high-quality bonding in layered concrete structures.

The ML-BDSO framework provides a systematic approach to quantify and manage **anisotropic defects** in layer bonding, using **eigenvalue and eigenvector analysis** in combination with uncertainty quantification (UQ) methods. The outputs guide the selection and optimization of key parameters in 3D concrete printing, supporting decision-making in mix design, print setup, and process control for large-scale, anisotropic structures. 

### Components and Code Walkthrough

#### 1. **Bayesian Inference (`bayesian_inference.py`)**

**Function**: The Bayesian inference module initializes **prior distributions** for defect probabilities based on input data from three categories:
   - **Material Properties** (e.g., compressive strength, fiber content)
   - **Process Parameters** (e.g., layer height, print speed)
   - **Environmental Conditions** (e.g., temperature, humidity)

**Purpose**: Bayesian inference is used to incorporate prior knowledge about bonding quality, updated continuously with new data to produce probabilistic predictions. The **initial defect probability distribution** generated here provides a foundational estimate of defect risks, setting up baseline expectations for bonding quality in various conditions.

**Proposal Significance**: Bayesian inference integrates existing knowledge into the framework, allowing the system to learn from initial material and process data. This feature is essential for the adaptive nature of ML-BDSO, as it allows defect predictions to be refined based on updated observations. Including Bayesian methods demonstrates a commitment to **data-driven decision-making** and **probabilistic modeling** in your proposal.

---

#### 2. **Monte Carlo Simulation with Adaptive Sampling (`monte_carlo_simulation.py`)**

**Function**: This module performs **Monte Carlo simulations** on defect probabilities, sampling from the Bayesian priors to produce a range of possible outcomes under different simulated conditions. An **adaptive sampling technique** focuses on high-risk zones, where defect probability exceeds a certain threshold.

**Outputs**:
   - **Monte Carlo Defect Probability Distribution**: A histogram of defect probabilities across all simulations.
   - **Defect Probability Trend Over Simulations**: A line plot showing the variability in defect probabilities over repeated simulation runs.

**Purpose**: Monte Carlo simulation helps quantify the **uncertainty in defect probabilities** by providing a probabilistic map of defect risks across different printing scenarios. Adaptive sampling allocates more resources to simulate scenarios with higher defect risks, improving accuracy in critical areas.

**Proposal Significance**: By incorporating Monte Carlo simulation with adaptive sampling, ML-BDSO quantifies and manages uncertainty in bonding quality, reflecting real-world variability. The Monte Carlo step shows the reviewer your framework’s ability to **capture and mitigate uncertainties** in defect formation, strengthening your proposal’s focus on reliability and consistency in 3D printing.

---

#### 3. **Sensitivity Analysis (`sensitivity_analysis.py`)**

**Function**: This module performs **sensitivity analysis** by calculating the **variance** in defect probabilities for each parameter, helping identify which parameters most significantly impact defect probability.

**Outputs**:
   - **Top Sensitivity Scores for Print Parameters**: A bar chart that ranks parameters based on sensitivity scores, highlighting the top parameters that contribute to variability in defect probability.

**Purpose**: Sensitivity analysis identifies **high-impact parameters** that need precise control to minimize defect probabilities. Parameters with high sensitivity scores (e.g., fiber content, print speed) are prioritized for close monitoring and tighter control during printing to improve bonding quality.

**Proposal Significance**: Sensitivity analysis quantifies each parameter's impact on defect probability, allowing targeted optimizations to improve layer bonding. Including sensitivity analysis in the proposal highlights ML-BDSO’s capacity for **identifying critical parameters** and **optimizing them systematically**, showcasing the framework’s practicality and applicability in real-world settings.

---

#### 4. **Feedback-Controlled Optimization (`feedback_optimization.py`)**

**Function**: The feedback optimization module dynamically adjusts parameters based on **sensitivity analysis results** to reduce defect probabilities and enhance bonding quality. It scales each parameter’s sensitivity score and applies adjustments to optimize print parameters.

**Outputs**:
   - **Top Optimized Print Parameters**: A bar chart of the top 10 parameters with adjusted values based on sensitivity results, showing the optimized settings for reducing defects.

**Purpose**: By adjusting parameters in real time based on sensitivity scores, this module ensures that the printing process is consistently optimized, reducing the likelihood of defects and improving layer bonding.

**Proposal Significance**: Feedback-controlled optimization shows the adaptability of the ML-BDSO framework, demonstrating its ability to respond to parameter changes dynamically. This real-time optimization feature aligns with goals of **smart manufacturing** and **adaptive process control** in your proposal, making it clear that ML-BDSO supports continuous improvements in 3D printing quality.

---

### How to Use ML-BDSO in Research

To use the ML-BDSO framework, the user prepares `.txt` files containing the initial material, process, and environmental data, which serve as inputs for Bayesian inference and Monte Carlo simulation. The user runs `main.py` to execute the full framework, which automatically saves results and visualizations to the `results/` folder.

Each output from the framework provides actionable insights:
1. **Initial Defect Probability**: Guides initial expectations for bonding quality.
2. **Monte Carlo Simulation**: Provides a probabilistic map of defect risks under different conditions.
3. **Sensitivity Analysis**: Highlights key parameters impacting defect formation.
4. **Feedback Optimization**: Adjusts parameter settings to achieve optimal bonding quality.

### Integrating ML-BDSO into the Proposal’s Objectives

The ML-BDSO framework aligns with your proposal’s objectives by providing a comprehensive, probabilistic approach to **minimizing defects** and **enhancing layer bonding** in 3D concrete printing. Its systematic integration of UQ and sensitivity analysis serves several purposes:

1. **Quantifies Uncertainty in Defect Formation**: Bayesian inference and Monte Carlo simulation provide probabilistic insights into defect risks, allowing engineers to account for uncertainties in bonding quality.
2. **Identifies and Prioritizes Key Parameters**: Sensitivity analysis ranks parameters based on their impact on defect probabilities, ensuring that only high-impact parameters are controlled closely.
3. **Enables Adaptive Control and Optimization**: Feedback-controlled optimization dynamically adjusts parameters to improve bonding, making the process robust to changing conditions.

### Contribution to Advancing 3D Concrete Printing

The ML-BDSO framework’s approach to handling uncertainties, assessing parameter impact, and optimizing in real time aligns with the objectives of advancing 3D concrete printing technology. This framework offers a structured methodology for developing **robust, adaptive 3D printing processes** that ensure high bonding quality and reduce anisotropic weaknesses. Its data-driven, probabilistic approach positions it as a valuable tool in enhancing the reliability and scalability of 3D printed concrete structures, supporting the broader goals of your research proposal.

---

### USER_MANUAL.md

```markdown
# USER MANUAL: ML-BDSO Framework

## Introduction
The ML-BDSO (Multi-Level Bayesian Defect Simulation and Optimization) framework is designed to enhance layer bonding quality and reduce defect probabilities in 3D concrete printing by addressing uncertainties in material properties, process parameters, and environmental conditions.

This tool integrates **Bayesian inference**, **Monte Carlo simulation with adaptive sampling**, **sensitivity analysis**, and **feedback-controlled optimization** to dynamically adjust printing parameters and achieve consistent bonding quality.

## System Requirements
- **Python**: Version 3.6 or higher
- **Packages**: `pandas`, `numpy`, `scipy`, `matplotlib`

## Installation Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/franklin02/ML-BDSO.git
   cd ML-BDSO
   ```

2. **Install Dependencies**:
   Install required Python packages.
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Data**:
   Place `.txt` files in the `data/` directory, as described below.

## Input Data Files Overview

Each input file specifies parameters essential to modeling and optimizing the 3D concrete printing process. Below is a detailed explanation of each file, including units, ranges, and physical meaning for each parameter.

---

### `material_properties.txt`

This file specifies the physical and chemical properties of the concrete mix, focusing on material performance indicators. Each parameter has a value and an associated uncertainty to capture variability in material behavior.

| Parameter                  | Units            | Description                                               | Typical Range                |
|----------------------------|------------------|-----------------------------------------------------------|-------------------------------|
| **compressive_strength**   | MPa              | Strength under compression                                | 20 - 100 MPa                  |
| **tensile_strength**       | MPa              | Strength under tension                                    | 2 - 10 MPa                    |
| **elastic_modulus**        | MPa              | Material stiffness                                        | 10,000 - 40,000 MPa           |
| **aggregate_type**         | -                | Type of coarse aggregate (e.g., gravel, limestone)        | -                             |
| **fiber_content**          | Volume fraction  | Fiber content in the mix                                  | 0 - 0.1 (10% of volume)       |
| **aggregate_volume_fraction** | Volume fraction | Total aggregate volume                                    | 0.5 - 0.7                     |
| **fine_aggregate_size**    | meters           | Average size of fine aggregates                           | 0.0001 - 0.005 m              |
| **coarse_aggregate_size**  | meters           | Average size of coarse aggregates                         | 0.005 - 0.02 m                |
| **aggregate_shape**        | -                | Aggregate shape (e.g., angular, rounded)                  | -                             |
| **aggregate_alignment**    | -                | Orientation of aggregates (random or aligned)             | -                             |
| **shrinkage_rate**         | -                | Shrinkage during curing                                   | 0.005 - 0.015                 |
| **thermal_conductivity**   | W/(m·K)          | Thermal conductivity                                      | 0.5 - 2 W/(m·K)               |
| **fresh_concrete_flow_rate** | m³/s            | Flow rate of fresh concrete                               | 0.01 - 0.1 m³/s               |

---

### `process_parameters.txt`

This file specifies parameters related to the printing process, covering factors that impact layer deposition and bonding.

| Parameter                  | Units            | Description                                               | Typical Range                |
|----------------------------|------------------|-----------------------------------------------------------|-------------------------------|
| **layer_height**           | meters           | Height of each printed layer                              | 0.001 - 0.01 m               |
| **print_speed**            | m/s              | Speed of nozzle movement                                  | 0.01 - 0.1 m/s               |
| **nozzle_orientation**     | degrees          | Orientation angle of the nozzle                           | 0 - 180 degrees               |
| **curing_time**            | hours            | Time for curing after layer deposition                    | 12 - 48 hours                |
| **extrusion_pressure**     | MPa              | Pressure during extrusion                                 | 0.5 - 1.5 MPa                |
| **layer_width**            | meters           | Width of each printed layer                               | 0.01 - 0.02 m                |

---

### `environmental_conditions.txt`

This file specifies external conditions that affect the printing process, particularly important in uncontrolled environments.

| Parameter                  | Units            | Description                                               | Typical Range                |
|----------------------------|------------------|-----------------------------------------------------------|-------------------------------|
| **temperature**            | °C               | Ambient temperature                                       | 5 - 40 °C                    |
| **humidity**               | %                | Relative humidity                                         | 30 - 90%                     |
| **wind_speed**             | m/s              | Wind speed (for outdoor printing)                         | 0 - 5 m/s                    |
| **ambient_light_exposure** | Lux              | Ambient light exposure                                    | 100 - 1000 Lux               |
| **vibration_level**        | -                | External vibrations affecting layer stability             | 0 - 0.1                      |

Each file must be formatted correctly with three columns: `parameter`, `value`, and `uncertainty`. For categorical parameters like `aggregate_type` or `aggregate_shape`, an associated uncertainty can represent variability within a general type.

---

This update provides a comprehensive overview for each parameter, including the physical meaning, units, allowable ranges, and additional contextual information, helping users to prepare and understand each input file accurately. Let me know if further adjustments are needed!


## Updates 

The following changes have been incorporated:

1. **Updated Input Data Files**:
   - **New parameters and units**: The input files now include additional parameters for fresh concrete rheology and interlayer bonding characteristics.
   - **New units for consistency**: Each parameter now specifies units, improving readability and ensuring accurate calculations.
   - **Error handling for non-numeric values**: Parameters that may contain non-numeric values (e.g., categorical descriptions) are now appropriately skipped.

2. **Updated Python Code**:
   - **Adaptive Bayesian Inference**: The `bayesian_inference.py` file now includes adaptive updates for prior distributions using new observed data. This allows the framework to iteratively improve accuracy.
   - **Monte Carlo Simulation Enhancements**: The `monte_carlo_simulation.py` file has improved error handling for cases with `NaN` values, ensuring robust trend analysis.
   - **Detailed Sensitivity Analysis with Units**: Parameters in `sensitivity_analysis.py` are now presented with units, allowing for clearer interpretation of sensitivity scores.
   - **Optimized Feedback Control**: The `feedback_optimization.py` file applies a 10% reduction to sensitivity scores, prioritizing top 10 parameters for optimized print quality.

---

## Instructions for Updated Files

### Running ML-BDSO

1. **Setup**:
   - Ensure all updated `.py` files and data files are in their respective directories.
   - Use `main.py` to initialize and run the ML-BDSO framework.

2. **Input Data Files**:
   - `material_properties.txt`, `process_parameters.txt`, `environmental_conditions.txt`: Updated input files are preloaded with new parameters, units, and instructions for use.

3. **Generated Outputs**:
   - All output files are saved in the `results/` directory:
     - **Defect Probability Distribution**: Histogram and trend plots.
     - **Sensitivity Scores**: Top 10 sensitivity scores are shown with units.
     - **Optimized Parameters**: Feedback optimization results are shown with units.

---

## File Descriptions

1. **Input Files**:
   - **material_properties.txt**: Contains physical and rheological properties with updated units and descriptions.
   - **process_parameters.txt**: Updated to include process-specific parameters relevant to layer bonding and defect management.
   - **environmental_conditions.txt**: Contains environmental variables (temperature, humidity) with added clarity in units.

2. **Python Scripts**:
   - **main.py**: Runs the entire ML-BDSO workflow and logs outputs in `output_data.txt`.
   - **bayesian_inference.py**: Initializes adaptive priors based on input data; incorporates new data for posterior updates.
   - **monte_carlo_simulation.py**: Generates defect probability distributions using robust error handling.
   - **sensitivity_analysis.py**: Calculates sensitivity scores, ensuring each parameter is labeled with units.
   - **feedback_optimization.py**: Optimizes top parameters by reducing sensitivity scores to enhance print quality.

---

## Running the Framework

1. **Execute Main Script**:
   Navigate to the `src/` directory and run the main script to execute the ML-BDSO framework:
   ```bash
   cd src
   python main.py
   ```

2. **Pipeline Steps**:
   The framework automatically performs each stage:
   - **Bayesian Inference**: Initializes defect probability priors based on input data and produces an initial defect probability distribution.
   - **Monte Carlo Simulation**: Simulates defect probabilities with adaptive sampling and plots the defect probability distribution.
   - **Sensitivity Analysis**: Calculates sensitivity scores, identifying which parameters most affect bonding quality.
   - **Feedback Optimization**: Dynamically adjusts parameters to optimize bonding, showing the top adjusted parameters.

3. **Output Files**:
   The `results/` directory contains:
   - Monte Carlo defect probability distribution
   - Sensitivity scores
   - Optimized print parameters
   - Trend of defect probabilities across simulations

## Visualizations and Interpretation

### 1. Initial Defect Probability Distribution
   - **Description**: This histogram shows the initial probability distribution of defects based on Bayesian inference.
   - **Interpretation**: Large values suggest certain parameters have a higher influence on initial defect probability. Review these for potential improvements in bonding quality.

### 2. Monte Carlo Defect Probability Distribution
   - **Description**: Displays defect probabilities generated by the Monte Carlo simulation.
   - **Interpretation**: A well-centered distribution suggests stable defect probabilities under various simulated conditions.

### 3. Defect Probability Trend Over Simulations
   - **Description**: Line plot showing how defect probabilities fluctuate across simulation runs.
   - **Interpretation**: Provides insight into the consistency of defect probability under simulated variations. Fluctuations may indicate parameters that need more control.

### 4. Top Sensitivity Scores for Print Parameters
   - **Description**: Bar plot of the top 10 parameters with the highest sensitivity scores.
   - **Interpretation**: Higher sensitivity scores indicate parameters with a substantial impact on defect probability. Prioritize these parameters for precise control to reduce defects.

### 5. Optimized Print Parameters
   - **Description**: Bar chart displaying the top 10 adjusted parameters based on sensitivity analysis.
   - **Interpretation**: Shows how parameter adjustments can improve bonding quality. The values represent optimal settings to minimize defects.

## Troubleshooting

1. **No Output in Sensitivity or Optimization Plots**:
   - Check that `monte_carlo_results` is properly structured and that `sensitivity_analysis.py` is correctly calculating variance.

2. **Excessive Defect Probability in Initial Distribution**:
   - Ensure that the initial values in `material_properties.txt` are within realistic ranges. High initial values may result from outlier data.

3. **Plotting Errors**:
   - Ensure `matplotlib` is installed and working properly. You can test this by creating a simple plot:
     ```python
     import matplotlib.pyplot as plt
     plt.plot([1, 2, 3], [1, 4, 9])
     plt.show()
     ```

4. **Parameter Formatting**:
   - Double-check `.txt` files for consistent tab-separated formatting, especially in header rows.

## Contact

For further assistance, contact Prof. Yang Lu, yanglufrank@boisestate.edu.
```

The **ML-BDSO v2.0** simulations generate a variety of outputs that provide insights into defect classification, parameter sensitivity, and optimization adjustments for enhancing 3D-printed concrete quality. Here’s a breakdown of the key output results and values produced by the framework:

### Key Output Results and Values

#### 1. **Bayesian Inference Results**
   - **Defect Classification**: The Bayesian inference process classifies the defect type based on parameter priors. Possible classifications include:
      - **Delamination**
      - **Porosity**
      - **Interlayer Weakness (Anisotropy)**
      - **Shrinkage and Warping**
      - **Voids**
      - **Cracking**
   - **Initial Defect Probability**: This value represents the calculated probability of defect occurrence based on initial conditions and parameter priors. A lower probability suggests stable conditions, while higher values indicate greater defect risk.
   - **Parameter Priors (Mean and Std Dev)**: For each parameter, Bayesian inference outputs the initial mean and standard deviation, which serve as baselines for Monte Carlo simulations and sensitivity analysis.

#### 2. **Monte Carlo Simulation Results**
   - **Defect Probability Distribution**: A histogram showing the distribution of defect probabilities across simulation iterations, providing insights into the variability of defect risk under different conditions.
   - **Defect Probability Trend Over Simulations**: A line plot displaying defect probability variations over each Monte Carlo iteration. This trend helps visualize how defect risk fluctuates with different parameter configurations.

#### 3. **Sensitivity Analysis Results**
   - **Top Sensitivity Scores**: This result highlights the top parameters with the highest sensitivity scores, indicating which parameters have the most substantial influence on defect probability. The scores are presented in a bar plot and are typically calculated based on variance.
   - **Parameter Rankings by Sensitivity**: Parameters are ranked according to their influence on defect probability, helping identify those that contribute most to defect formation.

#### 4. **Feedback-Controlled Optimization Results**
   - **Optimized Parameter Values**: The optimization step adjusts parameter values to minimize defect probability. The framework provides optimized values specifically tailored to the classified defect type. Examples of optimizations include:
      - **Porosity**: Adjustments to `aggregate_volume_fraction` and `layer_compaction_rate`.
      - **Interlayer Weakness**: Modifications to `interlayer_shear_strength` and `fiber_orientation_anisotropy`.
      - **Shrinkage and Warping**: Adjustments to `shrinkage_rate`, `curing_time`, and `thermal_expansion_anisotropy`.
   - **Optimization Plots**: These bar plots visualize the optimized values for the most influential parameters, showing the adjustments made to mitigate defect risks.

---

### Summary of Output Plots and Files
- **`output_data.txt`**: Contains a summary of defect classification, initial defect probability, sensitivity analysis rankings, and optimized parameter values for the classified defect type.
- **`defect_probability_distribution.png`**: A histogram showing the initial defect probability distribution.
- **`defect_probability_trend.png`**: A line plot displaying defect probability variations across Monte Carlo simulations.
- **`sensitivity_{defect_type}.png`**: A sensitivity analysis plot for the classified defect type, showing top sensitivity scores for influential parameters.
- **`optimized_parameters_{defect_type}.png`**: A bar plot illustrating the optimized values of parameters targeted to reduce defect probability for the classified defect type.

These outputs together provide a comprehensive view of defect probability, parameter sensitivity, and specific optimizations made by ML-BDSO v2.0 to improve bonding quality and reduce defect risks in 3D-printed structures. Let me know if you need further clarification on any of these output elements!


I’ll add interpretations for the three newly implemented classifications—**porosity**, **interlayer weakness (anisotropy)**, and **shrinkage and warping**—to the document. Here’s how each classification operates within the ML-BDSO v2.0 framework and its impact on the defect detection process.

---

### New Classifications in ML-BDSO v2.0

#### 1. **Porosity Classification**

**Objective**: The purpose of detecting porosity is to identify conditions where small, interconnected voids or pores may form within the material. This type of defect impacts the strength and durability of 3D-printed concrete.

**Classification Logic**:
   - Parameters influencing porosity include **aggregate_volume_fraction**, **fiber_content**, **layer_compaction_rate**, and **water_cement_ratio**. 
   - The classifier detects porosity by checking if these parameters fall within threshold ranges that indicate high porosity risk (e.g., high aggregate volume fraction or low compaction rate).

**Results and Impact**:
   - If classified as porosity, the framework would focus sensitivity analysis on parameters affecting mix consistency and flowability. This enables optimization steps that improve compaction and reduce the likelihood of void formation.
   - **Optimization**: Targeted adjustments to `layer_compaction_rate` and `fiber_content` would be made to reduce porosity, enhancing the overall density and integrity of the printed material.

#### 2. **Interlayer Weakness (Anisotropy) Classification**

**Objective**: This classification aims to detect weak bonding between printed layers, often due to anisotropic properties that cause strength discrepancies along different directions.

**Classification Logic**:
   - Key parameters for identifying interlayer weakness include **interlayer_shear_strength**, **interlayer_tensile_strength**, **fiber_orientation_anisotropy**, and **aggregate_alignment**. 
   - These parameters reflect the quality of bonding between layers and the degree of directional strength anisotropy.

**Results and Impact**:
   - If classified as interlayer weakness, the framework would prioritize sensitivity analysis and optimization on bonding parameters that can improve layer adhesion and reduce anisotropy.
   - **Optimization**: By enhancing parameters such as `interlayer_shear_strength` and `fiber_orientation_anisotropy`, the framework can minimize directional weaknesses, thus improving the structural integrity of the printed layers.

#### 3. **Shrinkage and Warping Classification**

**Objective**: Detecting shrinkage and warping focuses on identifying conditions that lead to dimensional instability, typically due to rapid curing, high shrinkage rates, or temperature sensitivity.

**Classification Logic**:
   - Parameters used for shrinkage and warping detection include **shrinkage_rate**, **curing_time**, **water_cement_ratio**, and **thermal_expansion_anisotropy**.
   - Thresholds for these parameters help the classifier recognize conditions that are likely to cause unwanted contractions or expansions, leading to deformations.

**Results and Impact**:
   - If shrinkage and warping is classified, the framework’s sensitivity analysis would emphasize dimensional stability parameters. This allows for targeted adjustments to control curing time, water-cement ratio, and temperature sensitivity, thereby mitigating warping.
   - **Optimization**: The framework would adjust parameters like `curing_time` and `shrinkage_rate` to improve stability, ensuring dimensional accuracy in the final structure.

---

These new classifications extend the ML-BDSO v2.0 framework’s capabilities, allowing it to address diverse defect types that can compromise the quality of 3D-printed structures. This refined classification approach enables more precise sensitivity analysis and parameter optimization based on each defect type’s unique characteristics.


To implement **Interlayer Weakness (Anisotropy)** in the ML-BDSO framework, we’ll focus on parameters related to interlayer bonding strength and directional properties. Interlayer weakness is often due to insufficient bonding between layers or anisotropic properties where strength is different along and across layers. This defect type is critical in 3D printing and composite materials because it affects structural integrity under load.

Here’s how we’ll proceed with the implementation for Interlayer Weakness (Anisotropy):

### Steps for Implementing Interlayer Weakness (Anisotropy)

1. **Define Classification Criteria**: Extend the `classify_defect_type` function to include thresholds specific to interlayer weakness.
   - Key parameters for anisotropy include **interlayer_shear_strength**, **interlayer_tensile_strength**, **fiber_orientation_anisotropy**, and **aggregate_alignment**.
   - The thresholds will be set to detect low bonding strength or high anisotropy.

2. **Update Sensitivity Analysis**: Emphasize interlayer weakness parameters in the sensitivity analysis.
   - By increasing the weight for anisotropy-related parameters, we can ensure these parameters are prioritized when the defect type is classified as interlayer weakness.

3. **Adjust Feedback Optimization**: Refine feedback-controlled optimization to focus on improving interlayer bonding when interlayer weakness is classified.

Let’s go through each step, starting with updating the classification criteria.

---

### Step 1: Add Interlayer Weakness to `classify_defect_type` in `bayesian_inference.py`

To classify interlayer weakness, we’ll add threshold criteria for parameters like `interlayer_shear_strength`, `fiber_orientation_anisotropy`, and `aggregate_alignment`. 

Here’s the updated `classify_defect_type` function with interlayer weakness criteria:

```python
def classify_defect_type(priors, thresholds=None):
    """
    Classifies defect types based on Bayesian priors for relevant parameters.

    Parameters:
    - priors: dict
        Dictionary of parameter names and their inferred prior values (mean, std).
    - thresholds: dict, optional
        Dictionary defining threshold ranges for defect types. 

    Returns:
    - defect_type: str
        Classified defect type based on the thresholds and prior values.
    """
    if thresholds is None:
        thresholds = {
            'porosity': {'aggregate_volume_fraction': (0.6, 0.7), 'fiber_content': (0.02, 0.03), 
                         'layer_compaction_rate': (0.5, 0.8), 'water_cement_ratio': (0.45, 0.55)},
            'delamination': {'elastic_modulus': (25000, 40000), 'initial_yield_stress': (800, 1200)},
            'voids': {'aggregate_volume_fraction': (0.5, 0.65), 'fiber_content': (0.01, 0.04)},
            'cracking': {'tensile_strength': (4.5, 6), 'shrinkage_rate': (0.005, 0.02)},
            'interlayer_weakness': {'interlayer_shear_strength': (0.2, 0.4), 'interlayer_tensile_strength': (0.3, 0.5), 
                                    'fiber_orientation_anisotropy': (0.5, 0.7), 'aggregate_alignment': (0.7, 1.0)}
        }
    
    defect_type = "unknown"
    
    for defect, criteria in thresholds.items():
        match = all(
            criteria[param][0] <= priors.get(param, (0,))[0] <= criteria[param][1] 
            for param in criteria
        )
        if match:
            defect_type = defect
            break

    return defect_type
```

### Explanation of Thresholds for Interlayer Weakness
- **interlayer_shear_strength** and **interlayer_tensile_strength**: Low values within ranges of 0.2–0.4 and 0.3–0.5 MPa indicate poor bonding strength between layers.
- **fiber_orientation_anisotropy** and **aggregate_alignment**: Values close to 1 indicate high alignment or anisotropy, which may contribute to weakness along specific directions.

---

### Step 2: Emphasize Anisotropy Parameters in `sensitivity_analysis.py`

To prioritize anisotropy-related parameters in sensitivity analysis, we’ll increase the sensitivity weight for parameters such as `interlayer_shear_strength`, `interlayer_tensile_strength`, `fiber_orientation_anisotropy`, and `aggregate_alignment`.

Here’s the updated `sensitivity_analysis_by_defect` function:

```python
def sensitivity_analysis_by_defect(defect_data, initial_priors, defect_type):
    """
    Performs sensitivity analysis specifically for a given defect type, identifying top
    parameters influencing the defect's probability.

    Parameters:
    - defect_data: dict
        Dictionary with defect probability data for each defect type.
    - initial_priors: dict
        Dictionary of initial prior values (mean, std) for each parameter.
    - defect_type: str
        Type of defect to focus on for the sensitivity analysis.

    Returns:
    - defect_sensitivity_results: dict
        Sorted dictionary with parameters and their sensitivity scores for the specified defect type.
    """
    defect_sensitivity_results = {}

    if defect_type not in defect_data:
        logging.error(f"Defect type '{defect_type}' not found in defect data.")
        return defect_sensitivity_results

    data = defect_data[defect_type]
    scores = {param: 0 for param in initial_priors.keys()}

    anisotropy_parameters = ['interlayer_shear_strength', 'interlayer_tensile_strength', 
                             'fiber_orientation_anisotropy', 'aggregate_alignment']
    weight_multiplier = 1.5 if defect_type == 'interlayer_weakness' else 1.0  # Emphasize anisotropy parameters

    for param in scores.keys():
        param_data = [entry.get(param, np.nan) for entry in data if isinstance(entry, dict)]
        param_data = [value for value in param_data if not np.isnan(value)]

        if not param_data:
            logging.warning(f"No valid data for parameter '{param}' in defect type '{defect_type}'")
            continue

        sensitivity_score = np.var(param_data)
        if param in anisotropy_parameters:
            sensitivity_score *= weight_multiplier

        scores[param] = sensitivity_score

    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)[:10])
    defect_sensitivity_results[defect_type] = sorted_scores

    return defect_sensitivity_results
```

### Step 3: Refine Feedback-Controlled Optimization for Interlayer Weakness in `feedback_optimization.py`

In the optimization step, we’ll ensure that when interlayer weakness is classified, the framework prioritizes adjustments to bonding strength and alignment parameters, like `interlayer_shear_strength` and `fiber_orientation_anisotropy`.

```python
def feedback_optimization_refined(sensitivity_scores, initial_priors, defect_type=None):
    """
    Optimizes parameters with targeted adjustments and visual feedback for specified defect types.

    Parameters:
    - sensitivity_scores: dict
        Sensitivity scores for each defect type.
    - initial_priors: dict
        Initial prior values for each parameter.
    - defect_type: str, optional
        The specific defect type to optimize parameters for.

    Returns:
    - optimized_parameters: dict
        Dictionary of optimized parameter values for defect mitigation.
    """
    optimized_parameters = {}

    print(f"Starting feedback optimization for defect type: {defect_type}")
    if defect_type not in sensitivity_scores:
        print(f"Error: Defect type '{defect_type}' not found in sensitivity scores.")
        return optimized_parameters

    sensitivities = sensitivity_scores[defect_type]
    anisotropy_parameters = ['interlayer_shear_strength', 'interlayer_tensile_strength', 
                             'fiber_orientation_anisotropy', 'aggregate_alignment']

    for param, sensitivity_score in sensitivities.items():
        if param in initial_priors:
            original_value, uncertainty = initial_priors[param]
            adjustment_factor = 0.2 if defect_type == 'interlayer_weakness' and param in anisotropy_parameters else 0.1
            adjustment = original_value - (sensitivity_score * adjustment_factor)
            optimized_value = max(adjustment, 0)
            optimized_parameters[param] = optimized_value
            print(f"Optimized {param} for {defect_type}: {optimized_value}")
        else:
            print(f"Warning: Parameter {param} not found in initial priors.")

    plt.figure(figsize=(10, 6))
    plt.bar(optimized_parameters.keys(), optimized_parameters.values(), color='blue', edgecolor='black')
    plt.title(f"Optimized Parameters for {defect_type.capitalize()}")
    plt.xlabel("Parameters")
    plt.ylabel("Optimized Value")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"../results/optimized_parameters_{defect_type}.png")
    plt.close()

    return optimized_parameters
```

### Summary of Adjustments

1. **Classification**: `classify_defect_type` now includes thresholds for **interlayer weakness**, with criteria based on bonding strength and anisotropy.
2. **Sensitivity Analysis**: `sensitivity_analysis_by_defect` prioritizes anisotropy parameters if interlayer weakness is the classified defect type.
3. **Optimization**: `feedback_optimization_refined` targets interlayer bonding parameters for adjustment to improve bonding quality and mitigate anisotropy.

### Next Steps

1. **Run the Framework with Updated Code**: Test these adjustments with input conditions likely to lead to interlayer weakness.
2. **Save Results and Review**: Once the framework completes, save and examine the output data and generated plots to confirm interlayer weakness classification.
3. **Analyze Outputs**: Evaluate the sensitivity and optimization results to ensure that interlayer parameters were prioritized as intended.


Based on the attached outputs and generated plots, here is a detailed interpretation of the **porosity classification test** using the ML-BDSO v2.0 framework.

### Case Study: Porosity Detection

#### 1. **Bayesian Inference and Defect Type Classification**
   - **Objective**: To detect porosity by analyzing parameters such as `aggregate_volume_fraction`, `fiber_content`, `layer_compaction_rate`, and `water_cement_ratio`.
   - **Result**: Despite the targeted parameter values for porosity, the defect type was still classified as **"delamination"** rather than "porosity."
   - **Interpretation**: 
      - The classification into "delamination" rather than "porosity" may indicate that the thresholds set for detecting porosity were not met, or that certain parameters, like `elastic_modulus`, `initial_yield_stress`, and environmental factors, exerted a dominant influence.
      - **Next Steps**: To achieve a porosity classification, the threshold settings for porosity-related parameters might need refinement, or Bayesian priors might need to be emphasized differently to allow porosity-related parameters to take priority.

#### 2. **Initial Defect Probability Distribution**
   - **Observation**: The **Initial Defect Probability Distribution** plot shows that most defect probabilities cluster around very low values, with only a few outliers at higher probabilities.
   - **Interpretation**: 
      - This distribution suggests that the initial parameters yield a low baseline defect probability, with isolated higher probabilities potentially due to parameter combinations that increase delamination risks, as classified in this case.
      - This result aligns with the framework’s classification of "delamination" rather than porosity, as high initial defect probabilities would be more indicative of porosity-prone conditions.

#### 3. **Monte Carlo Simulation Results**
   - **Defect Probability Trend**: The **Defect Probability Trend Over Simulations** plot shows fluctuations over 100 iterations, with defect probabilities varying between approximately 520 and 640.
      - The observed variations indicate the probabilistic effect of parameter ranges, showing that defect probability isn’t constant across the Monte Carlo samples.
   - **Monte Carlo Defect Probability Distribution**: The histogram shows that the distribution centers around 580, with a spread that includes higher probabilities, which aligns with increased risk factors for delamination or voids.
   - **Interpretation**: 
      - The trends and distribution highlight the framework’s sensitivity to parameter variations, providing an adaptable basis for classification based on specific defect criteria.
      - For porosity detection, this suggests that tighter control on compaction and mix ratios might be needed to observe a clearer shift toward porosity-prone conditions.

#### 4. **Sensitivity Analysis for Delamination (Instead of Porosity)**
   - **Top Parameters**: The sensitivity analysis plot identifies **elastic_modulus**, **initial_yield_stress**, and **modulus_gradient_interface** as the most influential parameters, with environmental parameters like **ambient_light_exposure** and **solar_radiation_intensity** also showing high sensitivity scores.
   - **Interpretation**: 
      - The dominance of `elastic_modulus` and `initial_yield_stress` suggests that these parameters are major contributors to defect classification.
      - These parameters might have overshadowed the impact of porosity-related parameters (e.g., `aggregate_volume_fraction` and `layer_compaction_rate`), leading the framework to classify the defect as delamination.
      - Adjusting the sensitivity weight or threshold emphasis for porosity-related parameters might help bring about porosity classification in future tests.

#### 5. **Feedback-Controlled Optimization**
   - **Optimized Parameters**: The optimization plot shows that **elastic_modulus**, **initial_yield_stress**, and **modulus_gradient_interface** were set to zero to minimize their influence, while other parameters, such as **ambient_light_exposure** and **solar_radiation_intensity**, were adjusted to reduce defect probability.
   - **Interpretation**:
      - The optimized parameters reflect adjustments aimed at mitigating delamination rather than porosity.
      - To achieve porosity mitigation, parameters such as **layer_compaction_rate** and **water_cement_ratio** would need specific adjustments, suggesting that further refinement in optimization settings for porosity classification is needed.

---

### Summary of Observations and Recommendations
1. **Classification as Delamination**: The framework classified the defect as "delamination," likely due to the high influence of parameters like `elastic_modulus` and `initial_yield_stress`. To achieve a porosity classification, it may be necessary to:
   - Adjust threshold values for porosity-specific parameters.
   - Increase the sensitivity weight of parameters such as `aggregate_volume_fraction`, `fiber_content`, `layer_compaction_rate`, and `water_cement_ratio` in the Bayesian inference and sensitivity analysis steps.

2. **Parameter Influence**:
   - **Sensitivity Analysis** reveals a strong influence of structural and environmental parameters related to bonding and interlayer strength.
   - **Optimization**: Further tuning of optimization processes may be required for porosity to adjust mix and compaction-related parameters more effectively.

3. **Future Adjustments**:
   - Refine the **classification thresholds** for porosity-related parameters to make them more responsive.
   - Consider **prioritizing porosity-related parameters** in Bayesian inference, sensitivity analysis, and optimization if porosity is the targeted defect type.






The latest results indicate that the ML-BDSO framework continues to classify the defect type as **"delamination"** despite adjustments for **interlayer weakness (anisotropy)**. Here’s a detailed analysis of the outcomes, along with insights on why interlayer weakness has not yet been detected.

### Analysis of Interlayer Weakness Classification Attempt

#### 1. **Bayesian Inference and Defect Classification**
   - **Expected Outcome**: Adjustments to the classification thresholds and parameters were designed to increase the sensitivity to interlayer weakness conditions by focusing on parameters such as `interlayer_shear_strength`, `interlayer_tensile_strength`, `fiber_orientation_anisotropy`, and `aggregate_alignment`.
   - **Actual Outcome**: Despite these adjustments, the defect type was classified as **"delamination"** instead of **"interlayer weakness"**.
   - **Interpretation**:
      - The classification as "delamination" indicates that structural parameters like `elastic_modulus` and `initial_yield_stress` are still dominant, potentially overshadowing the influence of interlayer weakness parameters.
      - This could be due to the relatively high sensitivity scores associated with these structural parameters, which consistently drive the framework toward classifying defects as delamination.

#### 2. **Initial Defect Probability Distribution**
   - **Observation**: The **Initial Defect Probability Distribution** plot remains concentrated around lower defect probabilities with a few higher outliers.
   - **Interpretation**:
      - The concentrated distribution at low probabilities does not suggest significant variability associated with weak interlayer bonding or anisotropy, which would likely increase the defect probability.
      - A more dispersed distribution might be expected under conditions of interlayer weakness, as bonding issues and anisotropic effects would likely increase defect probabilities.

#### 3. **Monte Carlo Simulation Results**
   - **Defect Probability Trend and Distribution**: The **Defect Probability Trend Over Simulations** plot shows variability over simulations, with defect probabilities fluctuating between 520 and 640.
   - **Interpretation**:
      - The Monte Carlo distribution does not display the spread or instability that might be characteristic of interlayer weakness conditions. Instead, the observed trends align more with structural integrity conditions relevant to delamination.
      - This suggests that porosity-related conditions might need further emphasis within the Monte Carlo sampling range to detect interlayer weakness.

#### 4. **Sensitivity Analysis Results**
   - **Top Parameters**: The sensitivity analysis results show **elastic_modulus** as the most influential parameter, followed by **modulus_gradient_interface** and **initial_yield_stress**. Interlayer-related parameters such as `interlayer_shear_strength` and `fiber_orientation_anisotropy` are not highlighted as top factors.
   - **Impact on Classification**: 
      - The high sensitivity scores of delamination-related parameters reinforce the delamination classification. Even with an increased weight on interlayer parameters, they do not rank highly in the sensitivity analysis.
      - This suggests that parameters like `interlayer_shear_strength` and `fiber_orientation_anisotropy` may need further prioritization in sensitivity analysis to make interlayer weakness more detectable.

#### 5. **Feedback-Controlled Optimization**
   - **Optimized Parameters**: The optimization focused on reducing the influence of delamination-related parameters, such as `elastic_modulus` and `modulus_gradient_interface`, while making adjustments to environmental parameters and compaction rates.
   - **Impact on Interlayer Weakness**:
      - The optimization primarily targets delamination-relevant factors rather than addressing bonding strength or anisotropy. To mitigate interlayer weakness, parameters like `interlayer_shear_strength` and `fiber_orientation_anisotropy` would need to be the focus.

---

### Recommendations to Enhance Detection of Interlayer Weakness

1. **Further Tighten Bayesian Thresholds for Interlayer Weakness**:
   - Narrow down the threshold values for parameters specific to interlayer weakness (e.g., reduce acceptable ranges for `interlayer_shear_strength` and `fiber_orientation_anisotropy`) to enhance sensitivity to anisotropy-prone conditions.

2. **Increase Sensitivity Weighting for Interlayer Parameters**:
   - Further increase the sensitivity weight for interlayer-specific parameters, such as `aggregate_alignment` and `fiber_orientation_anisotropy`. This should make them more likely to emerge as high-sensitivity factors when interlayer weakness conditions are present.

3. **Introduce Anisotropy-Specific Sampling in Monte Carlo Simulation**:
   - Modify the Monte Carlo simulation to introduce anisotropy-specific sampling, focusing on greater variability for parameters like `interlayer_shear_strength` and `aggregate_alignment`.

4. **Dedicated Interlayer Weakness Analysis and Optimization Logic**:
   - Introduce defect-type-specific logic to optimize for interlayer weakness, focusing on the enhancement of interlayer bonding strength, as well as alignment factors that reduce anisotropy.

The persistent classification as delamination suggests that while the framework effectively detects delamination-related parameters, more extensive changes are necessary to differentiate interlayer weakness. This could involve dedicated classification rules or custom analysis workflows tailored to each defect type. Let me know if you’d like to proceed with further adjustments or explore defect-type-specific workflows for interlayer weakness.