# 🛠️ Component Documentation

This document provides an overview of the key components in the **OSPSD_HW1** project.

---

## **1⃣ Calculator**
### **Description**
The **Calculator** component provides basic arithmetic operations.

### **Features**
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)

### **Implementation**
Located in: `src/calculator.py`

### **Usage Example**
```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)  # Returns 8
```

### **Methods**
| Method        | Description                | Example |
|--------------|----------------------------|---------|
| `add(a, b)`  | Returns `a + b`            | `calc.add(3, 2) -> 5` |
| `subtract(a, b)` | Returns `a - b`       | `calc.subtract(3, 2) -> 1` |
| `multiply(a, b)` | Returns `a * b`       | `calc.multiply(3, 2) -> 6` |

### **Unit Tests**
Tests for `Calculator` are in `tests/unit_tests/test_calculator.py`
- **Tested Functions:** `add()`, `subtract()`, `multiply()`

---

## **2⃣ Logger**
### **Description**
The **Logger** component records and stores calculation logs.

### **Features**
- Log operations performed by the calculator.
- Retrieve stored logs.

### **Implementation**
Located in: `src/logger.py`

### **Usage Example**
```python
from src.logger import Logger

logger = Logger()
logger.log("5 + 3 = 8")
```

### **Methods**
| Method       | Description                     | Example |
|-------------|---------------------------------|---------|
| `log(msg)`  | Logs a message                 | `logger.log("Operation completed")` |
| `get_logs()` | Retrieves all logs            | `logger.get_logs() -> ["5 + 3 = 8"]` |

### **Unit Tests**
Tests for `Logger` are in `tests/unit_tests/test_logger.py`
- **Tested Functions:** `log()`, `get_logs()`

---

## **3⃣ Notifier**
### **Description**
The **Notifier** component sends alerts when a calculation exceeds a **specified threshold**.

### **Features**
- Sends an alert if the result is greater than the threshold.
- Allows modifying the threshold.

### **Implementation**
Located in: `src/notifier.py`

### **Usage Example**
```python
from src.notifier import Notifier

notifier = Notifier(threshold=10)
notifier.notify(15)  # Sends an alert
```

### **Methods**
| Method         | Description                         | Example |
|--------------|---------------------------------|---------|
| `set_threshold(thresh)` | Updates the threshold value | `notifier.set_threshold(20)` |
| `notify(value)` | Sends an alert if `value > threshold` | `notifier.notify(25)` |

### **Unit Tests**
Tests for `Notifier` are in `tests/unit_tests/test_notifier.py`
- **Tested Functions:** `set_threshold()`, `notify()`

---

## **🔗 Integration Tests**
The integration tests validate interactions between components:
- **Calculator ➞ Logger** (`tests/integration_tests/test_integration_calculator_logger.py`)
- **Logger ➞ Notifier** (`tests/integration_tests/test_integration_logger_notifier.py`)

---

## **🛠️ End-to-End Test**
The end-to-end test verifies that:
1. A calculation is performed.
2. The result is logged.
3. A notification is sent if the threshold is exceeded.

Location: `tests/end_to_end_tests/test_end_to_end.py`

### **Workflow**
```python
calc = Calculator()
logger = Logger()
notifier = Notifier(threshold=10)

result = calc.add(6, 5)  # 6 + 5 = 11
logger.log(f"6 + 5 = {result}")
notifier.notify(result)  # Sends alert (threshold exceeded)
```

---


