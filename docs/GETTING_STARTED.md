# Getting Started with SPM Trial Solutions

This guide will help you get started with creating and running solutions for SPM trial questions.

## Quick Start

1. **Set up your environment** (see README.md for detailed instructions)
2. **Choose a subject** and navigate to its directory
3. **Copy a template** or create a new solution file
4. **Write your solution** following the template structure
5. **Test your solution** and verify the answer

## Writing Your First Solution

### Step 1: Choose a Template

For a mathematics question:
```bash
cd subjects/mathematics
cp example_question.py question_1.py
```

### Step 2: Fill in the Question Details

Edit `question_1.py`:

```python
"""
Question 1: Quadratic Equations
Topic: Algebra - Quadratic Equations

Question: Solve the equation 2x² + 5x - 3 = 0
"""

from sympy import symbols, solve

def solve_question():
    # Define the variable
    x = symbols('x')

    # Define the equation
    equation = 2*x**2 + 5*x - 3

    # Solve the equation
    solutions = solve(equation, x)

    return solutions
```

### Step 3: Add Working Steps

```python
def show_working():
    print("Step 1: Identify coefficients")
    print("  a = 2, b = 5, c = -3")
    print()
    print("Step 2: Use quadratic formula")
    print("  x = (-b ± √(b² - 4ac)) / 2a")
    print()
    print("Step 3: Calculate discriminant")
    print("  Δ = b² - 4ac = 25 - 4(2)(-3) = 49")
    print()
    print("Step 4: Calculate solutions")
    print("  x = (-5 ± √49) / 4")
    print("  x = (-5 ± 7) / 4")
    print("  x₁ = 0.5, x₂ = -3")
```

### Step 4: Run Your Solution

```bash
python question_1.py
```

## Best Practices

### 1. Clear Documentation

Always include:
- Question number and description
- Topic or subtopic
- Given information
- What is being asked

### 2. Step-by-Step Working

Break down your solution:
```python
def solve_question():
    # Step 1: Given information
    mass = 10  # kg
    velocity = 20  # m/s

    # Step 2: Calculate kinetic energy
    kinetic_energy = 0.5 * mass * velocity**2

    # Step 3: Return result
    return kinetic_energy
```

### 3. Use Utility Functions

```python
from utils.helpers import format_answer, print_step

# Format your answer properly
answer = format_answer(200, "J", sig_figs=3)
print(f"Kinetic Energy = {answer}")

# Print steps clearly
print_step(1, "Calculate kinetic energy using KE = ½mv²")
```

### 4. Verify Your Answers

```python
from utils.helpers import check_answer

calculated = 200
expected = 200
if check_answer(calculated, expected):
    print("✓ Answer is correct!")
else:
    print("✗ Answer is incorrect")
```

### 5. Add Visualizations

For mathematics and physics problems, visualizations help:

```python
import matplotlib.pyplot as plt
import numpy as np

def visualize_solution():
    x = np.linspace(-10, 10, 100)
    y = 2*x**2 + 5*x - 3

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.3)
    plt.grid(True)
    plt.title("Graph of 2x² + 5x - 3 = 0")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
```

## Subject-Specific Tips

### Mathematics
- Use SymPy for symbolic calculations
- Show algebraic steps clearly
- Include graphs where appropriate
- Verify answers by substitution

### Physics
- Always include units
- Use SI units consistently
- Reference physical constants from scipy.constants
- Draw force diagrams or motion graphs

### Computer Science
- Write clean, well-commented code
- Include time and space complexity analysis
- Add multiple test cases
- Explain your algorithm

## Testing Your Solutions

Create tests in the `tests/` directory:

```python
# tests/test_mathematics_q1.py
from subjects.mathematics.question_1 import solve_question

def test_quadratic_solution():
    solutions = solve_question()
    assert len(solutions) == 2
    assert 0.5 in solutions
    assert -3 in solutions
```

Run tests:
```bash
pytest tests/
```

## Getting Help

- Check example solutions in each subject directory
- Review the utility functions in `utils/helpers.py`
- Read the main README.md for setup issues
- Refer to library documentation (NumPy, SymPy, etc.)

## Common Issues

### Import Errors
Make sure you're in the project root directory and have activated your virtual environment.

### Missing Dependencies
Run `pip install -r requirements.txt` to install all required packages.

### Plot Not Showing
Add `plt.show()` at the end of your plotting code.

---

Happy solving! Good luck with your SPM Trial preparation!
