# cost_benefit_analysis.py
# Author: Yi Ma
# Description: This script performs cost-benefit analysis using Net Present Value (NPV) calculations.
# It is designed to help users assess the financial feasibility of projects by comparing benefits and costs over time.
# ------------------------------------------------------------------

# Notes for Users:
# - Data Requirements: Your CSV file should include columns named "Year," "Benefit," and "Cost."
# - Customizable Elements: You can change the discount rates or use a different dataset by updating the 'file_path' variable.
# - Running the Script: Use a Python environment (like Anaconda, Jupyter, or your local IDE) to execute this script.
# - Dependencies: Make sure you have 'pandas' installed (`pip install pandas`).

import pandas as pd

def calculate_npv(benefits, costs, discount_rate):
    """
    Calculate Net Present Value (NPV) given benefits, costs, and a discount rate.
    
    Args:
        benefits (list): List of benefits for each year.
        costs (list): List of costs for each year.
        discount_rate (float): The discount rate to apply.
    
    Returns:
        float: The calculated NPV.
    """
    npv = sum([(b - c) / (1 + discount_rate)**t for t, (b, c) in enumerate(zip(benefits, costs))])
    return npv

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pandas.DataFrame: Loaded data in a structured format.
    """
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    # Load sample data
    file_path = "data/sample_data.csv"  # Path to your sample dataset
    data = load_data(file_path)

    # Extract benefits and costs from the data
    benefits = data["Benefit"].tolist()
    costs = data["Cost"].tolist()

    # Set a base discount rate
    base_discount_rate = 0.05

    # Calculate NPV using the base discount rate
    npv = calculate_npv(benefits, costs, base_discount_rate)
    print(f"Net Present Value (NPV) at {base_discount_rate*100}% discount rate: {npv}")

    # Perform sensitivity analysis with different discount rates
    for rate in [0.03, 0.05, 0.07]:
        npv = calculate_npv(benefits, costs, rate)
        print(f"NPV at {rate*100}% discount rate: {npv}")

# Additional Considerations
# Scenario Analysis: Test how changes in variables like the discount rate affect the NPV, which is crucial for public policy decisions.
# Sensitivity Analysis: Analyze how sensitive your results are to key assumptions, such as the discount rate or projected benefits.
# Externalities: Consider the broader social and environmental impacts, which may not have direct monetary values but can be included as qualitative benefits.
