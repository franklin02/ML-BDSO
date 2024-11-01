Here’s the **USER_MANUAL.md** file, providing detailed instructions on setting up, running, and interpreting the ML-BDSO framework.

Here is a detailed description and explanation of the ML-BDSO framework code, highlighting its purpose, functionality, and how it contributes to the proposal. You can use this description to articulate the significance and mechanics of ML-BDSO in your proposal.

---

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
