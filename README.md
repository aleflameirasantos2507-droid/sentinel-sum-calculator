# Sentinel Sum Calculator

A beginner-friendly Python project that reads numbers entered by the user until a sentinel value is provided. After the input process ends, the program displays how many numbers were entered and their total sum.

## Features

- Accepts multiple integer inputs
- Uses a sentinel value (`999`) to stop execution
- Counts how many valid numbers were entered
- Calculates the sum of all entered numbers
- Uses an infinite loop with `break`

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/sentinel-sum-calculator.git
```

2. Navigate to the project folder:

```bash
cd sentinel-sum-calculator
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
Enter a value (999 stops the program): 10
Enter a value (999 stops the program): 20
Enter a value (999 stops the program): 15
Enter a value (999 stops the program): 999
```

### Output

```text
You entered 3 numbers and their sum is 45!
```

## Learning Objectives

This project demonstrates:

- `while True` loops
- The `break` statement
- Sentinel values
- Counters and accumulators
- User input handling
- Formatted string literals (f-strings)

## Key Concepts

### Counter

Tracks how many valid numbers were entered:

```python
count += 1
```

### Accumulator

Stores the running total:

```python
total += number
```

### Sentinel Value

A special value used to stop the program:

```python
if number == 999:
    break
```
