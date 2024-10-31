Here’s the **README.md** file, focusing on providing a concise overview, project structure, 
setup instructions, and main functionalities of the ML-BDSO framework.

---

### README.md

```markdown
# ML-BDSO: Multi-Level Bayesian Defect Simulation and Optimization Framework

## Overview
The **ML-BDSO** framework is a Python-based tool designed to improve layer bonding quality and 
reduce defect probabilities in large-scale 3D concrete printing. It combines **Bayesian inference**, 
**Monte Carlo simulation with adaptive sampling**, **machine learning-based sensitivity analysis**, 
and **feedback-controlled optimization** to provide real-time adjustments during the printing process, 
addressing uncertainties in material properties, process parameters, and environmental conditions.

## Project Structure

```plaintext
ML-BDSO/
│
├── data/                           # Directory for input and output data files
│   ├── material_properties.txt      # Initial data on material properties
│   ├── process_parameters.txt       # Data on printing parameters (speed, layer height, orientation)
│   ├── environmental_conditions.txt # Environmental data (temperature, humidity)
│
├── src/                             # Main source code directory
│   ├── main.py                      # Main script to run the ML-BDSO framework
│   ├── bayesian_inference.py        # Bayesian inference and updating functions
│   ├── monte_carlo_simulation.py    # Monte Carlo simulation with adaptive sampling
│   ├── sensitivity_analysis.py      # Machine learning-based sensitivity analysis
│   ├── feedback_optimization.py     # Feedback-controlled optimization for print parameters
│   └── utils.py                     # Utility functions (data loading, plotting, logging)
│
├── results/                         # Directory to store outputs and plots
└── README.md                        # Project overview and setup instructions
└── USER_MANUAL.md                   # Detailed user guide for the project
```

## Dependencies

This project requires Python 3.x and the following packages:
- `pandas` for data handling
- `numpy` for numerical operations
- `scipy` for statistical functions
- `matplotlib` for plotting results

Install dependencies using:
```bash
pip install -r requirements.txt
```

## How to Run the ML-BDSO Framework

1. **Prepare Data**:
   - Ensure the `data/` directory contains properly formatted `.txt` files:
     - **material_properties.txt**: Defines material characteristics like compressive strength, fiber content, etc.
     - **process_parameters.txt**: Defines printing parameters like layer height, print speed, and nozzle orientation.
     - **environmental_conditions.txt**: Defines external conditions such as temperature and humidity.
   
2. **Execute Main Script**:
   - Navigate to the `src/` folder and run `main.py` to execute the ML-BDSO framework:
   ```bash
   cd src
   python main.py
   ```
   
3. **Check Results**:
   - Output files, including defect probability distributions, sensitivity scores, and optimized parameters, are saved in the `results/` directory.

## Functionality and Key Outputs

1. **Bayesian Inference**: Initializes defect probability priors based on material, process, and environmental data, generating an initial defect probability distribution.
2. **Monte Carlo Simulation**: Simulates defect probabilities with adaptive sampling, producing a distribution and trend of defect probabilities across simulations.
3. **Sensitivity Analysis**: Identifies the top parameters impacting defect probability. High sensitivity scores indicate parameters with a substantial influence on bonding quality.
4. **Feedback Optimization**: Adjusts parameters based on sensitivity results to enhance bonding quality. The optimized values are plotted for visualization.

### Output Visualizations

The framework produces the following plots, saved in `results/`:
- **Initial Defect Probability Distribution**: Shows the initial probability distribution based on Bayesian inference.
- **Monte Carlo Defect Probability Distribution**: Visualizes defect probability distribution from simulations.
- **Defect Probability Trend Over Simulations**: Tracks probability variations across simulations.
- **Top Sensitivity Scores**: Highlights the parameters most affecting defect probability.
- **Optimized Print Parameters**: Shows the top parameters and their adjusted values based on optimization.

For more detailed instructions, please refer to the USER_MANUAL.md.
```

---

Please review this README, and once you confirm, I’ll proceed with creating the USER_MANUAL.md file. 
Let me know if there are any additional adjustments you’d like!