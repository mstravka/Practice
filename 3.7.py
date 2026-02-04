def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

from calc import add, multiply

if __name__ == "__main__":
    x = 5
    y = 3
    print("Add:", add(x, y))
    print("Multiply:", multiply(x, y))

from calc import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: pip install pytest

    - name: Run tests
      run: pytest
