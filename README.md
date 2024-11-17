
# CodeLint

**CodeLint** is a lightweight Python module that ensures your code complies with PEP 8 standards. By identifying common issues like long lines, incorrect indentation, inconsistent naming conventions, and unnecessary whitespace, CodeLint helps you write clean, professional, and maintainable Python code.

---

## Table of Contents

<p align="center">
  <a href="#key-features" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Key%20Features-blue?style=for-the-badge" alt="Key Features">
  </a>
  <a href="#installation" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Installation-green?style=for-the-badge" alt="Installation">
  </a>
  <a href="#usage" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Usage-orange?style=for-the-badge" alt="Usage">
  </a>
  <a href="#running-tests-with-pytest" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Running%20Tests-yellow?style=for-the-badge" alt="Running Tests">
  </a>
  <a href="#how-it-works" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/How%20It%20Works-red?style=for-the-badge" alt="How It Works">
  </a>
  <a href="#contributing" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Contributing-purple?style=for-the-badge" alt="Contributing">
  </a>
  <a href="#license" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/License-grey?style=for-the-badge" alt="License">
  </a>
</p>

---

## Key Features

- **Line Length Check**: Flags lines exceeding a specified maximum length.
- **Indentation Check**: Detects incorrect visual indentation (e.g., mixed tabs and spaces).
- **Snake Case Check**: Ensures variable and function names follow the `snake_case` naming convention.
- **Whitespace Check**: Identifies trailing whitespace and excessive blank lines.

---

## Installation

Install **CodeLint** easily using `pip`:

```bash
pip install codelint
```

![Installation Screenshot](https://github.com/user-attachments/assets/039b7171-6661-4bf0-84d2-263025a99117)

---

## Usage

**CodeLint** can be run directly from the terminal to analyze Python files for PEP 8 violations.

### Command:
```bash
codelint <file.py>
```

### Example:
```bash
>> pip install codelint
>> codelint my_script.py
```

![Usage Example Screenshot](https://github.com/user-attachments/assets/d8b8f5be-1eef-473c-8f57-aed34b49b15c)

---

## Running Tests with Pytest

CodeLint includes comprehensive tests to ensure functionality and reliability. Follow these steps to run the test suite:

1. Clone the repository:
   ```bash
   git clone https://github.com/Aditya-1998k/CodeLint.git
   ```

2. Navigate to the project directory:
   ```bash
   cd CodeLint
   ```

3. Install `pytest`:
   ```bash
   pip install pytest
   ```

4. Run the tests:
   ```bash
   pytest tests/test_checker.py
   ```

### Example:
![Test Example Screenshot](https://github.com/user-attachments/assets/d628ca8f-de04-4755-8eb6-0cd913355db4)

---

## How It Works

**CodeLint** scans your Python files for the following issues:

- **Line Length**: Checks for lines that exceed the standard maximum length (default is 79 characters).
- **Indentation**: Ensures consistent indentation (e.g., no mixing of tabs and spaces).
- **Snake Case Naming**: Verifies that function and variable names adhere to PEP 8's `snake_case` standard.
- **Trailing Whitespace**: Identifies and flags any trailing spaces at the end of lines.
- **Excessive Blank Lines**: Warns about more than one consecutive blank line.

---

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

**CodeLint** is licensed under the MIT License. See the [LICENSE](https://github.com/Aditya-1998k/CodeLint?tab=MIT-1-ov-file) file for details.  

---

**CodeLint** helps you maintain high coding standards effortlessly. Install today and ensure your Python projects adhere to best practices! 🚀
