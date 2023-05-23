import csv
import sys

if len(sys.argv) < 4:
    print("Usage: python script.py <input_csv_file> <output_csv_file> <max_row_size> (use value 200 for custom terminology and 1000 for parallel data)")
    sys.exit(1)

input_csv_file = sys.argv[1]
output_csv_file = sys.argv[2]
max_row_size = int(sys.argv[3])

# Open the input CSV file and create the output CSV file
with open(input_csv_file, 'r') as input_file, open(output_csv_file, 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    cleaned_rows = []

    for row in reader:
        # Remove hard line breaks from each cell in the row
        cleaned_row = [cell.replace('\n', '') for cell in row]
        cleaned_rows.append(cleaned_row)

    for i, row in enumerate(cleaned_rows):
        # Strip trailing whitespaces from each cell in the row
        cleaned_row = [cell.strip() for cell in row]
        cleaned_rows[i] = cleaned_row

    # Remove rows with empty cells and row size over X bytes
    cleaned_rows = [row for row in cleaned_rows if all(row) and len(','.join(row).encode('utf-8')) <= max_row_size]

    for row in cleaned_rows:
        if any(cell.strip() for cell in row):
            writer.writerow(row)