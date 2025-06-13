import csv
import sys

BIT_OPTIONS = [4, 8, 16, 32, 64]
NUM_GHR_BITS = 32
NUM_PERCEPTRONS = 64
THETA = 1.93 * NUM_GHR_BITS + 14
NOT_TAKEN = -1
TAKEN = 1
perceptron_table = [[0 for _ in range(NUM_GHR_BITS + 1)] for _ in range(NUM_PERCEPTRONS)]

def calculate_output(index, ghr):
    y = 0
    perceptron_weights = perceptron_table[index]

    x_i = 0
    for i in range(len(perceptron_weights)):
        weight = perceptron_weights[i]
        if i == 0:
            x_i = 1
        else:
            x_i = 1 if (ghr >> (i - 1)) & 1 else -1
        y = y + weight * x_i
    return y
    
def update_weights(t, index, ghr):
    perceptron_weights = perceptron_table[index]

    x_i = 0
    for i in range(len(perceptron_weights)):
        w_i = perceptron_weights[i]
        if i == 0:
            x_i = 1
        else:
            x_i = 1 if (ghr >> (i - 1)) & 1 else -1
        perceptron_table[index][i] = w_i + t * x_i

def update_ghr(ghr, actual):
    mask = (1 << NUM_GHR_BITS) - 1
    return ((ghr << 1) | actual) & mask

if len(sys.argv) < 2:
    print("Usage: python(3) perceptron.py <csv_file>")
    exit()

in_filename = sys.argv[1]

for num_ghr_bits in BIT_OPTIONS:
    NUM_GHR_BITS = num_ghr_bits
    THETA = 1.93 * NUM_GHR_BITS + 14

    for num_perceptrons in BIT_OPTIONS:
        NUM_PERCEPTRONS = num_perceptrons
        perceptron_table = [[0 for _ in range(NUM_GHR_BITS + 1)] for _ in range(NUM_PERCEPTRONS)]


        # Load the CSV file
        with open(in_filename, mode='r') as file:
            reader = csv.DictReader(file)
            total = 0
            correct = 0

            ghr = 0 # Replace with the branch address
            
            for row in reader:
                # print(perceptron_table)
                index = int(row["Jump Addr"], 16) % NUM_PERCEPTRONS
                y = calculate_output(index, ghr)
                prediction = 1 if y >= 0 else 0
                actual = int(row["Jump?"])
            
                if prediction != actual or abs(y) < THETA: 
                    if actual == 0: 
                        update_weights(NOT_TAKEN, index, ghr)
                    else:
                        update_weights(TAKEN, index, ghr)
                if actual == prediction:    
                    correct += 1

                ghr = update_ghr(ghr, actual)
                total += 1

        accuracy = correct / total * 100
        print(f"GHR bits: {num_ghr_bits}\tNum Perceptrons: {num_perceptrons}")
        print(f"Total branches: {total}")
        print(f"Correct predictions: {correct}")
        print(f"Accuracy: {accuracy:.2f}%")
