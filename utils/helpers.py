"""
Utility functions for SPM Trial solutions
"""

import numpy as np
from typing import Union, List


def round_to_significant_figures(value: float, sig_figs: int = 3) -> float:
    """
    Round a number to specified significant figures

    Args:
        value: Number to round
        sig_figs: Number of significant figures

    Returns:
        Rounded value
    """
    if value == 0:
        return 0
    return round(value, sig_figs - int(np.floor(np.log10(abs(value)))) - 1)


def format_answer(value: Union[float, int], unit: str = "", sig_figs: int = 3) -> str:
    """
    Format answer with proper significant figures and units

    Args:
        value: The calculated value
        unit: Unit of measurement
        sig_figs: Number of significant figures

    Returns:
        Formatted answer string
    """
    rounded_value = round_to_significant_figures(value, sig_figs)
    if unit:
        return f"{rounded_value} {unit}"
    return str(rounded_value)


def check_answer(calculated: float, expected: float, tolerance: float = 1e-6) -> bool:
    """
    Check if calculated answer matches expected answer within tolerance

    Args:
        calculated: Calculated answer
        expected: Expected answer
        tolerance: Acceptable difference

    Returns:
        True if answers match within tolerance
    """
    return abs(calculated - expected) <= tolerance


def print_step(step_number: int, description: str, result=None):
    """
    Print a step in the solution process

    Args:
        step_number: Step number
        description: Description of the step
        result: Optional result to display
    """
    print(f"\nStep {step_number}: {description}")
    if result is not None:
        print(f"  Result: {result}")


def create_table(headers: List[str], data: List[List]) -> str:
    """
    Create a simple text table

    Args:
        headers: Column headers
        data: Rows of data

    Returns:
        Formatted table string
    """
    # Calculate column widths
    col_widths = [len(str(h)) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Create format string
    row_format = " | ".join([f"{{:<{w}}}" for w in col_widths])

    # Build table
    table = row_format.format(*headers) + "\n"
    table += "-" * (sum(col_widths) + 3 * (len(headers) - 1)) + "\n"
    for row in data:
        table += row_format.format(*row) + "\n"

    return table
