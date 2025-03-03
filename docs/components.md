# Components Documentation

This document describes the components available in this project and their directory structure.

## Directory Structure

```
src/
  calculator/              # Calculator component
    __init__.py           # Package initialization
    api.py               # Public API
    calculator.py        # Implementation
    tests/               # Component-specific tests
      test_calculator.py # Unit tests
  logger/                 # Logger component
    __init__.py          # Package initialization
    api.py               # Public API
    logger.py            # Implementation
    tests/               # Component-specific tests
      test_logger.py     # Unit tests
  notifier/              # Notifier component
    __init__.py          # Package initialization
    api.py               # Public API
    notifier.py          # Implementation
    tests/               # Component-specific tests
      test_notifier.py   # Unit tests
tests/
  integration_tests/     # Integration tests
  end_to_end_tests/     # End-to-end tests
```

## Components

### Calculator Component

The Calculator component provides basic arithmetic operations.

- Location: `src/calculator/`
- Main class: `Calculator`
- Available operations:
  - Addition
  - Subtraction
  - Multiplication

### Logger Component

The Logger component handles logging operations with timestamps.

- Location: `src/logger/`
- Main class: `Logger`
- Features:
  - Basic message logging
  - Error logging
  - Calculation logging
  - UTC timestamps
  - File-based storage

### Notifier Component

The Notifier component handles notification delivery.

- Location: `src/notifier/`
- Main class: `Notifier`
- Features:
  - Basic notification delivery
  - Console output

## Component Dependencies

- Calculator -> No dependencies
- Logger -> No dependencies
- Notifier -> No dependencies

## Using Components

Each component provides a public API through its `api.py` file. It is recommended to use these APIs rather than directly instantiating the classes.

Example usage:

```python
# Using Calculator
from src.calculator import add, subtract, multiply
result = add(5, 3)  # Returns 8

# Using Logger
from src.logger import create_logger, log_message
logger = create_logger("myapp.log")
log_message("Hello, World!", logger)

# Using Notifier
from src.notifier import notify
notify("Important message!")
```

## Component Design Principles

1. **Encapsulation**: Each component encapsulates its functionality and exposes a clean API.
2. **Single Responsibility**: Each component has a single, well-defined responsibility.
3. **Testability**: Components are designed to be easily testable in isolation.
4. **API-First**: Components expose their functionality through a well-defined API.
5. **Documentation**: Components include comprehensive documentation.

## Creating New Components

To create a new component:

1. Create a new directory under `src/`
2. Create the following files:
   - `__init__.py` - Package initialization and API exports
   - `api.py` - Public API functions
   - `component_name.py` - Implementation
3. Add unit tests in the `tests/` subdirectory
4. Update this document to include the new component 