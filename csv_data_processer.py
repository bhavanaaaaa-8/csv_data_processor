
import csv

def calculate_statistics(filename):
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or "Sales" not in reader.fieldnames:
                print("Error: CSV must contain a 'Sales' column.")
                return

            sales_values = []

            for row in reader:
                try:
                    sales = float(row["Sales"])
                    sales_values.append(sales)
                except (ValueError, TypeError):
                    print(f"Warning: Invalid sales value skipped: {row.get('Sales')}")

            if not sales_values:
                print("No valid sales data found.")
                return

            total = sum(sales_values)
            average = total / len(sales_values)
            highest = max(sales_values)
            lowest = min(sales_values)
            count = len(sales_values)

            print("\n--- Sales Statistics ---")
            print(f"Total Sales   : {total:.2f}")
            print(f"Average Sales : {average:.2f}")
            print(f"Highest Sales : {highest:.2f}")
            print(f"Lowest Sales  : {lowest:.2f}")
            print(f"Valid Records : {count}")

    except FileNotFoundError:
        print("Error: CSV file not found. Check the filename.")
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except OSError as error:
        print(f"Error reading the file: {error}")


calculate_statistics("sales.csv")
