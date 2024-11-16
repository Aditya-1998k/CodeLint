import sys

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
                indent_level = len(line) - len(modified_line)
                if indent_level % 4 != 0:
                    issues.append(f"Line {i}: Indentation is not a multiple of 4 spaces.")
        return issues
        
    def run_checks(self):
        issues = []
        issues.extend(self.check_line_length())
        issues.extend(self.check_indentation())
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
