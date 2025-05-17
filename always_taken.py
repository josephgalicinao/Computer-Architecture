import csv

# Load the CSV file
with open("branch_trace.csv", newline='') as file:
    reader = csv.DictReader(file)
    total = 0
    correct = 0

    for row in reader:
        actual = int(row["Taken"])
        prediction = 1  # Always Not Taken
        total += 1
        if prediction == actual:
            correct += 1

accuracy = correct / total * 100
print(f"Total branches: {total}")
print(f"Correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2f}%")
