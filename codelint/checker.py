import sys
from colorama import Fore, Style
from codelint.model import CodeLint
                
def run_checks(self):
    issues = []
    issues.extend(CodeLint.check_line_length())
    issues.extend(CodeLint.check_indentation())
    issues.extend(CodeLint.check_snake_case())
    issues.extend(CodeLint.check_trailing_whitespace())
    issues.extend(CodeLint.check_excessive_blank_lines())
    return issues
    



def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python code_lint.py <file_path>" + Style.RESET_ALL)
        sys.exit(1)
    else:
        linter = CodeLint(sys.argv[1])
        result = run_checks()
        if result:
            print(Fore.YELLOW + "Issues Found:" + Style.RESET_ALL)
            print("\n".join(Fore.CYAN + issue + Style.RESET_ALL for issue in result))
        else:
            print(Fore.GREEN + "No issues found. Your code is clean!" + Style.RESET_ALL)
