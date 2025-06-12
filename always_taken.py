import csv
import sys

# get args
if len(sys.argv) < 2:
    print("Usage: python(3) always_taken.py <csv_file>")
    exit()

csv_file = sys.argv[1]

# Load the CSV file
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    total = 0
    correct = 0

    for row in reader:
        actual = int(row["Jump?"])
        prediction = 1  # Always Not Taken
        total += 1
        if prediction == actual:
            correct += 1

accuracy = correct / total * 100
print(f"Total branches: {total}")
print(f"Correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2f}%")
