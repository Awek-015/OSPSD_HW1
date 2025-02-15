# Python Project Template - OSPSD_HW1

## Overview

This repository serves as a Python project template, providing a structured foundation for developing Python applications. It includes:

- **Continuous Integration & Testing**: Automated tests with **CircleCI**
- **Static Analysis & Code Formatting**: Uses **Ruff** and **Mypy**
- **Comprehensive Testing Framework**: Includes **unit, integration, and end-to-end tests**
- **Component-based Design**: Implements `Calculator`, `Logger`, and `Notifier`

## Prerequisites

- **Python 3.10 or higher**
- **CircleCI** (configured for automated builds & tests)
- **uv** (for dependency management, recommended)

## Project Setup

To set up the project environment:

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install project dependencies using uv (recommended):**
   ```sh
   pip install uv
   uv pip install --system -r requirements.txt
   ```
   **Or using pyproject.toml:**
    ```sh
   uv pip install --system
   ```

## Running the Application

To run the application, use:
```sh
python src/main.py
```

Replace `src/main.py` with the relevant script.

## Testing

This repository includes **three levels of testing**:

1. **Unit Tests** (test individual components)
2. **Integration Tests** (test interactions between components)
3. **End-to-End Tests** (simulate real-world workflows)

Run all tests using:
```sh
pytest
```

To run tests separately:
```sh
pytest tests/unit_tests
pytest tests/integration_tests
pytest tests/end_to_end_tests
```

## Static Analysis & Code Formatting

This repository enforces **strict code quality standards** using:
- **Ruff**: For linting & auto-formatting
- **Mypy**: For type checking

Run **Ruff** checks:
```sh
ruff check .
```

Run **Mypy** type checking:
```sh
mypy src/
```

## CI/CD Pipeline (CircleCI)

**CircleCI** is configured to:
- Run **unit, integration, and end-to-end tests**
- Perform **static analysis** (Ruff, Mypy)
- Generate **test coverage reports**

To view test results:
1. Navigate to [CircleCI Dashboard](https://app.circleci.com/pipelines/circleci/mr17jU9wJBnXPo4vt5qdJ/6JUYQ89ZVGTAJke7rhE99X)
2. Select the latest pipeline run
3. View the **"Tests" section** (enabled via `store_test_results`)
4. Download **coverage reports** from the **Artifacts** tab

**Include CircleCI run links in HW submission:**
- One successful test run
- One failed test run

## Project Components

This project follows a **modular component-based architecture**.

| Component | Description |
|-----------|------------|
| **Calculator** | Performs basic arithmetic operations (add, subtract, multiply) |
| **Logger** | Records calculations performed by the calculator |
| **Notifier** | Sends alerts when results exceed a certain threshold |

Each component has:
- **Unit Tests**
- **Integration Tests**
- **End-to-End Tests**

For more details, refer to **[`component.md`](docs/component.md)**.

## Project Structure

```
OSPSD_HW1/
│── src/
│   ├── calculator.py
│   ├── logger.py
│   ├── notifier.py
│── tests/
│   ├── unit_tests/
│   │   ├── test_calculator.py
│   │   ├── test_logger.py
│   │   ├── test_notifier.py
│   ├── integration_tests/
│   │   ├── test_integration_calculator_logger.py
│   │   ├── test_integration_logger_notifier.py
│   ├── end_to_end_tests/
│   │   ├── test_end_to_end.py
│── docs/
│   ├── component.md
│   ├── documentation.md
│── .circleci/
│   ├── config.yml
│── .github/
│   ├── pull_request_template.md
│── README.md
│── pyproject.toml
│── requirements.txt
│── LICENSE
```

## Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repository**
2. **Create a new branch**
3. **Use GitHub issue templates (`.github/issue_template`)**
4. **Follow the pull request template (`.github/pull_request_template.md`)**
5. **Ensure tests pass before submitting PR**

By contributing, you agree to license your code under Apache 2.0.

## License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.

## Additional Information

- **`.gitignore`** is configured to exclude unnecessary files (`__pycache__`, `.venv`, etc.)
- For detailed documentation, see **[`component.md`](docs/component.md)**

