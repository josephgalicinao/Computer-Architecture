import csv
import random

NUM_ENTRIES = 100000

# Simulate multiple branch addresses
loop_start_pc = 0x1048
loop_end_pc = 0x1064
exit_pc = 0x1070
if_else_pc = 0x1100
branch_pc = 0x1204
random_pc_1 = 0x1301  # New PC for additional branches
random_pc_2 = 0x1434  # Another PC
random_pc_3 = 0x1521  # Another one
random_pc_4 = 0x1609  # Yet another
random_pc_5 = 0x1890  # And one more

def generate_branch_data(entries=NUM_ENTRIES):
    data = []
    current_pc = loop_start_pc
    loop_counter = 0
    
    # Generate random number of loop iterations (between 2 and 5)
    loop_iterations = random.randint(2, 5)
    
    # Generate random number of if-else iterations (between 3 and 7)
    total_if_else_iterations = random.randint(3, 7)
    if_else_counter = 0
    
    for _ in range(entries):
        # Simulate loop structure
        if current_pc == loop_start_pc:
            if loop_counter < loop_iterations:
                jump_target = loop_end_pc
                taken = 1  # Taken to continue looping
                loop_counter += 1
            else:
                jump_target = exit_pc
                taken = 0  # Exit the loop
                loop_counter = 0  # Reset for potential future loops
        
        # Simulate a branching pattern with an if-else statement
        elif current_pc == if_else_pc:
            if if_else_counter < total_if_else_iterations:
                jump_target = branch_pc
                taken = 1 if random.random() < 0.6 else 0  # 60% taken
                if_else_counter += 1
            else:
                jump_target = exit_pc
                taken = 0  # Exit
                if_else_counter = 0  # Reset
        
        # Simulate random non-loop branches with various PC values
        elif current_pc == branch_pc:
            jump_target = random.choice([random_pc_1, random_pc_2, random_pc_3, random_pc_4, random_pc_5])
            taken = 1 if random.random() < 0.4 else 0

        # Additional branching with new random PCs
        elif current_pc == random_pc_1:
            jump_target = random.choice([random_pc_2, random_pc_3])
            taken = 1 if random.random() < 0.5 else 0
        
        elif current_pc == random_pc_2:
            jump_target = random.choice([random_pc_4, random_pc_5])
            taken = 1 if random.random() < 0.3 else 0
        
        elif current_pc == random_pc_3:
            jump_target = random.choice([random_pc_1, random_pc_4])
            taken = 1 if random.random() < 0.7 else 0

        elif current_pc == random_pc_4:
            jump_target = random.choice([random_pc_5, random_pc_1])
            taken = 1 if random.random() < 0.4 else 0
        
        elif current_pc == random_pc_5:
            jump_target = random.choice([random_pc_2, random_pc_3])
            taken = 1 if random.random() < 0.6 else 0
        
        else:
            jump_target = random.randint(0x2000, 0x3000)
            taken = 1 if random.random() < 0.3 else 0

        # Append the entry
        data.append({
            "BranchAddress": hex(current_pc),
            "JumpTarget": hex(jump_target),
            "Taken": taken
        })
        
        # Update PC for next iteration
        if taken == 1:
            current_pc = jump_target
        else:
            current_pc += 4  # Assume sequential execution (e.g., +4 bytes)
    
    return data

# Generate and save to CSV
with open("branch_trace.csv", "w", newline="") as csvfile:
    fieldnames = ["BranchAddress", "JumpTarget", "Taken"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(generate_branch_data(entries=NUM_ENTRIES))

print(f"Generated branch_trace.csv with {NUM_ENTRIES} entries!")
