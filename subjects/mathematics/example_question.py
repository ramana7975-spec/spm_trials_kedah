"""
Example Mathematics Solution Template
SPM 2025 Trial - Kedah

Question: [Describe the question here]
Topic: [e.g., Quadratic Equations, Differentiation, Vectors]
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, diff, integrate, simplify


def solve_question():
    """
    Main solution function

    Returns:
        Solution or answer to the question
    """
    # Write your solution here
    pass


def visualize_solution():
    """
    Optional: Create visual representation of the solution
    """
    # Example plotting
    x = np.linspace(-10, 10, 100)
    y = x**2  # Replace with actual function

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Solution Visualization")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def verify_answer(answer, expected):
    """
    Verify if the answer is correct

    Args:
        answer: Calculated answer
        expected: Expected answer

    Returns:
        bool: True if correct
    """
    return np.isclose(answer, expected)


if __name__ == "__main__":
    # Run the solution
    result = solve_question()
    print(f"Answer: {result}")

    # Optionally visualize
    # visualize_solution()
