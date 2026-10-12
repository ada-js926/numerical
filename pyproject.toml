# numerical

A collection of numerical functions using NumPy for matrix operations, array element-wise calculations, and statistics.

## Installation

From this folder, in the `mpm2026` environment (or any environment with Python 3.10 or later):

```bash
pip install -e ".[dev]"
```

`[dev]` also installs the tools used to check the package, `pytest` and `flake8`.

## Usage

```python
import numpy as np
from matrix_operations import matrix_add_subtract
from array_operations import elementwise_operations
from statistics import statistical_calculations

# Example usage of matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
add_res, sub_res = matrix_add_subtract(A, B)

# Example usage of element-wise operations
mult_res, div_res = elementwise_operations(A, B)

# Example usage of statistical calculations
data = np.array([10, 20, 30, 40, 50])
mean, median, std = statistical_calculations(data)
```

## Running the tests

```bash
pytest
flake8 .
```

## License

MIT (see `LICENSE`).