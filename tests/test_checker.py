import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from codelint.checker import CodeLint

@pytest.fixture
def sample_file(tmp_path):
    """Creates a temporary Python file with trailing whitespace for testing."""
    file_path = tmp_path / "sample.py"
    file_path.write_text(
        "def SampleFunction():\n"
        "    return 'rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr\\pass'\n"
        " \n"  # Empty line, no trailing whitespace
        "x=5\n"
        "\n"  # Another empty line, no trailing whitespace
        "     def another_function():\n"  # Improper indentation, no trailing whitespace
        "        pass\n"  # Properly indented, no trailing whitespace
    )
    return file_path

def test_line_length(sample_file):
    checker = CodeLint(str(sample_file))
    issues = checker.check_line_length(max_length=20)
    assert len(issues) > 0, "Should detect lines exceeding the max length"

def test_indentation(sample_file):
    checker = CodeLint(str(sample_file))
    issues = checker.check_indentation()
    assert len(issues) > 0, "Should detect incorrect indentation"

def test_check_snake_case(sample_file):
    checker = CodeLint(str(sample_file))
    issues = checker.check_snake_case()
    assert len(issues) > 0, "Should detect non-snake_case variables"

def test_check_trailing_whitespace(sample_file):
    checker = CodeLint(str(sample_file))
    issues = checker.check_trailing_whitespace()
    import pdb; pdb.set_trace()
    print(issues)
    assert len(issues) > 0, "Should detect trailing whitespace"
