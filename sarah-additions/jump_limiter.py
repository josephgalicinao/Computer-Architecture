# Takes in a csv as an argument and goes through and makes a file without jumps

import csv
import sys


def main():
    
    # get args
    if len(sys.argv) < 2:
        print("Usage: python(3) jump_limiter.py <csv_file>")
        return

    in_filename = sys.argv[1]
    
    with open(in_filename, mode="r") as in_csv, open(f"{in_filename[:-4]}_jump.csv", mode="w") as out_csv:
        csv_reader = csv.DictReader(in_csv, delimiter=",")
        csv_writer = csv.DictWriter(out_csv, fieldnames=csv_reader.fieldnames)
        csv_writer.writeheader()
        for row in csv_reader:
            inst_name = row["Inst Name"]
            inst_parts = row["Inst Name"].split()
            if(inst_name.startswith("JP") or inst_name.startswith("JR") or inst_name.startswith("CALL") or inst_name.startswith("RET") or inst_name.startswith("RETI") or inst_name.startswith("RST"))\
               and (len(inst_parts) > 1 and not (inst_name.split()[1].startswith("$"))):
                csv_writer.writerow(row)

    
    # create a new CSV file with "_jumps" at end of name before ".csv"


if __name__ == "__main__":
    main()