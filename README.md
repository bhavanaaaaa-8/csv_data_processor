# CSV Data Statistics Using Python

## Description
This project reads employee or sales data from a CSV file and calculates useful statistics using Python. It displays the total, average, highest value, lowest value, and number of valid records.

## Features
- Reads data from a CSV file.
- Calculates total and average sales.
- Finds the highest and lowest sales values.
- Counts valid numeric records.
- Handles missing files and permission errors.
- Skips invalid numeric values with a warning.

## Requirements
- Python 3.x
- A CSV file containing a `Sales` column.

## Project Structure
```text
CSV-Statistics/
├── sales.csv
├── sales_statistics.py
└── README.md
```

## Sample CSV Data
Create a file named `sales.csv`:

```csv
Employee,Department,Sales
Arun,Sales,15000
Priya,HR,12000
Rahul,Sales,20000
Sneha,IT,18000
Kiran,Sales,25000
```

## How to Run
1. Install Python 3 if it is not already installed.
2. Save the Python program as `sales_statistics.py`.
3. Place `sales.csv` in the same folder.
4. Open a terminal in that folder.
5. Run the command:

```bash
python sales_statistics.py
```

## Sample Output
```text
--- Sales Statistics ---
Total Sales   : 90000.00
Average Sales : 18000.00
Highest Sales : 25000.00
Lowest Sales  : 12000.00
Valid Records : 5
```

## Error Handling
- **FileNotFoundError:** Displays a message if the CSV file is missing.
- **PermissionError:** Handles files that cannot be accessed.
- **ValueError:** Skips rows containing invalid numeric values.
- **Empty or invalid data:** Displays a message when no valid sales values are available.

## Customization
To analyze employee salaries instead of sales, replace the `Sales` column name in the Python program with `Salary` and update the CSV file accordingly.

## Concepts Used
- Python functions
- CSV file handling
- Lists and loops
- Built-in functions: `sum()`, `len()`, `max()`, and `min()`
- Exception handling

## Conclusion
This project demonstrates how Python can process CSV files and calculate basic statistical summaries while handling common file and data errors.

