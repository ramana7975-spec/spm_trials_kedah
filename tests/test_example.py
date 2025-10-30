"""
Example test file for SPM solutions
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.helpers import (
    round_to_significant_figures,
    format_answer,
    check_answer,
)


class TestHelpers:
    """Test utility helper functions"""

    def test_round_to_significant_figures(self):
        """Test rounding to significant figures"""
        assert round_to_significant_figures(123.456, 3) == 123
        assert round_to_significant_figures(0.00123, 2) == 0.0012
        assert round_to_significant_figures(9.81, 2) == 9.8

    def test_format_answer(self):
        """Test answer formatting"""
        assert format_answer(9.81, "m/s²", 3) == "9.81 m/s²"
        assert format_answer(100, "kg", 2) == "100 kg"

    def test_check_answer(self):
        """Test answer verification"""
        assert check_answer(9.81, 9.81) is True
        assert check_answer(9.81, 9.82, tolerance=0.1) is True
        assert check_answer(9.81, 10.0, tolerance=0.1) is False


# Example subject-specific tests
@pytest.mark.mathematics
class TestMathematics:
    """Example mathematics tests"""

    def test_placeholder(self):
        """Placeholder test"""
        assert True


@pytest.mark.physics
class TestPhysics:
    """Example physics tests"""

    def test_placeholder(self):
        """Placeholder test"""
        assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
