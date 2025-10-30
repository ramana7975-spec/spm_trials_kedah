# SPM 2025 Trial Solutions - Kedah

Code solutions for the SPM (Sijil Pelajaran Malaysia) 2025 Trial Exam - Kedah state.

## Project Overview

This repository contains Python solutions for various SPM trial exam questions across multiple subjects including Mathematics, Physics, Chemistry, Biology, and Computer Science.

## Project Structure

```
spm_trials_kedah/
├── subjects/
│   ├── mathematics/        # Mathematics solutions
│   ├── physics/            # Physics solutions
│   ├── chemistry/          # Chemistry solutions
│   ├── biology/            # Biology solutions
│   └── computer_science/   # Computer Science solutions
├── utils/                  # Utility functions and helpers
├── tests/                  # Unit tests
├── docs/                   # Documentation
├── examples/               # Example solutions
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd spm_trials_kedah
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Solutions

Each subject has its own directory with individual question solutions. To run a solution:

```bash
python subjects/mathematics/example_question.py
```

### Creating New Solutions

1. Navigate to the appropriate subject directory
2. Copy an example template or create a new file
3. Follow the template structure:
   - Add question description and topic
   - Implement the `solve_question()` function
   - Add working steps and explanations
   - Include test cases if applicable

### Using Utility Functions

The `utils/helpers.py` module provides common functions:

```python
from utils.helpers import format_answer, print_step, check_answer

# Format an answer with proper significant figures
answer = format_answer(9.81, "m/s²", sig_figs=3)

# Print solution steps
print_step(1, "Calculate velocity", "20 m/s")

# Verify your answer
is_correct = check_answer(calculated=9.81, expected=9.81)
```

## Dependencies

Key libraries used in this project:

- **numpy**: Numerical computations
- **scipy**: Scientific computing and constants
- **sympy**: Symbolic mathematics
- **matplotlib**: Data visualization
- **pandas**: Data analysis
- **pytest**: Testing framework
- **jupyter**: Interactive notebooks

See `requirements.txt` for complete list.

## Running Tests

To run all tests:

```bash
pytest tests/
```

To run tests with coverage:

```bash
pytest --cov=subjects tests/
```

## Contributing

1. Create a new branch for your solutions
2. Follow the existing code structure and templates
3. Add comments and explanations for clarity
4. Include test cases where applicable
5. Commit with clear messages

## Coding Standards

- Use clear, descriptive variable names
- Add docstrings to all functions
- Follow PEP 8 style guidelines
- Include step-by-step working
- Add units to physical quantities
- Use proper significant figures

## Tips for Solutions

1. **Always show your working** - Include step-by-step calculations
2. **Use comments liberally** - Explain your logic
3. **Verify answers** - Include verification checks
4. **Add visualizations** - Graphs and diagrams help understanding
5. **Test edge cases** - Consider special cases and boundaries

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [SymPy Documentation](https://docs.sympy.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)

## License

This project is for educational purposes only.

## Contact

For questions or contributions, please open an issue or submit a pull request.

---

**Good luck with your SPM Trial preparation!**
