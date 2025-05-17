import csv

NUM_GHR_BITS = 16
STRONGLY_TAKEN = 0b11
WEAKLY_TAKEN = 0b10
STRONGLY_NOT_TAKEN = 0b00
WEAKLY_NOT_TAKEN = 0b01
pht = [WEAKLY_NOT_TAKEN] * (2 ** NUM_GHR_BITS)

def update_pht(is_taken, index):
    cur_value = pht[index]
    if is_taken:
        if cur_value < STRONGLY_TAKEN:
            pht[index] += 1
    else:
        if cur_value > STRONGLY_NOT_TAKEN:
            pht[index] -= 1

def get_prediction(ghr):
    prediction = pht[ghr]
    if prediction >= WEAKLY_TAKEN:
        return 1
    elif prediction <= WEAKLY_NOT_TAKEN:
        return 0

def update_ghr(ghr, actual):
    mask = (1 << NUM_GHR_BITS) - 1
    return ((ghr << 1) | actual) & mask

# Load the CSV file
with open("branch_trace.csv", newline='') as file:
    reader = csv.DictReader(file)
    total = 0
    correct = 0

    ghr = 0

    for row in reader:
        prediction = get_prediction(ghr)
        actual = int(row["Taken"])
        
        update_pht(is_taken=actual, index=ghr)
        ghr = update_ghr(ghr, actual)

        if prediction == actual:       
            correct += 1
        total += 1

accuracy = correct / total * 100
print(f"Total branches: {total}")
print(f"Correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2f}%")
