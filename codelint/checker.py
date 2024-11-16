import sys
import re

class CodeLint:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_line_length(self, max_length=79):
        """
        Check if line exceeding Maximum Length
        """
        issues = []
        with open(self.file_path, 'r') as file:
            for i, line in enumerate(file, start=1):
                if len(line.strip()) > max_length:
                    issues.append(f"Line {i}: Exceeds {max_length} characters.")
        return issues

    def check_indentation(self):
        """
        Check for inconsistent Identation
        """
        issues = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                modified_line = line.lstrip()
                if not modified_line:
                    continue
                indent_level = len(line) - len(modified_line)
                if indent_level % 4 != 0:
                    issues.append(f"Line {i}: Indentation is not a multiple of 4 spaces.")
        return issues
    
    def check_snake_case(self):
        issues = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if "def " in line or "=" in line:
                    if "def " in line:
                        function_name = line.split("def ")[1].split("(")[0].strip()
                        if not re.match(r"^[a-z_][a-z0-9_]*$", function_name):
                            issues.append(f"Snake case issue on line {line_number}: {function_name}")
                    
                    if "=" in line:
                        variable_name = line.split("=")[0].strip()
                        if not re.match(r"^[a-z_][a-z0-9_]*$", variable_name):
                            issues.append(f"Snake case issue on line {line_number}: {variable_name}")
        return issues
    
    def check_trailing_whitespace(self):
        issues = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                modified_lines = line.rstrip()
                if modified_lines != line:
                    issues.append(f"Line {i}: Trailing whitespace detected.")
        return issues
                


    def run_checks(self):
        issues = []
        issues.extend(self.check_line_length())
        issues.extend(self.check_indentation())
        issues.extend(self.check_snake_case())
        issues.extend(self.check_trailing_whitespace())
        return issues
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python code_lint.py <file_path>")
        sys.exit(1)
    else:
        linter = CodeLint(sys.argv[1])
        result = linter.run_checks()
        if result:
            print("\n".join(result))
        else:
            print("No issues found.")
