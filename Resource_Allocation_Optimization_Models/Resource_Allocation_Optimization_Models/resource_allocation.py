# resource_allocation.py
# Author: Yi Ma
# Description: This script demonstrates resource allocation optimization using linear programming.

from scipy.optimize import linprog

def allocate_resources(costs, benefits, constraints):
    """
    Perform resource allocation optimization using linear programming.

    Args:
        costs (list): Cost coefficients for each project/resource.
        benefits (list): Benefit coefficients for each project/resource.
        constraints (dict): Dictionary with constraint names and values.
    
    Returns:
        dict: Optimal resource allocation and maximum benefit.
    """
    # Negate benefits for maximization (linprog minimizes by default)
    c = [-b for b in benefits]
    
    # Constraints (example: budgets or resource limits)
    A = constraints["A"]  # Coefficients for constraints
    b = constraints["b"]  # Right-hand side values
    
    # Bounds for variables (e.g., resource proportions between 0 and 1)
    x_bounds = [(0, 1) for _ in range(len(costs))]
    
    # Solve the optimization problem
    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method="highs")
    
    if result.success:
        allocation = {f"Resource_{i+1}": x for i, x in enumerate(result.x)}
        max_benefit = -result.fun
        return {"allocation": allocation, "max_benefit": max_benefit}
    else:
        return {"error": "Optimization failed"}

# Sample Usage
if __name__ == "__main__":
    # Example costs and benefits
    costs = [10, 20, 15]  # Costs for each resource
    benefits = [40, 50, 45]  # Benefits for each resource
    
    # Example constraints
    constraints = {
        "A": [[1, 1, 1]],  # Budget constraint coefficients
        "b": [1]  # Total budget (e.g., normalized to 1)
    }
    
    # Run the resource allocation optimization
    result = allocate_resources(costs, benefits, constraints)
    
    if "error" not in result:
        print("Optimal Resource Allocation:", result["allocation"])
        print("Maximum Benefit Achieved:", result["max_benefit"])
    else:
        print(result["error"])
