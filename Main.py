# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_net = None
net_changes = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net
        net_changes.append(net_change)
        previous_net = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase["amount"]:
            greatest_increase = {"date": row[0], "amount": net_change}

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease["amount"]:
            greatest_decrease = {"date": row[0], "amount": net_change}

# Calculate the average net change across the months
average_change = sum(net_changes) / len(net_changes) if net_changes else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the output
print(output)

# Write the results to a text file
try:
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
except IOError as e:
    print(f"An error occurred while writing the file: {e}")