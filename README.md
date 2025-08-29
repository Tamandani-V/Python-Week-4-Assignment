# Vendors Data Processing

## Description
This project includes a Python script that:
- Creates a sample input file named `vendors_raw.txt` containing vendor data.
- Reads the input file, processes each line to extract vendor information and formats it into a human-readable sentence.
- Writes the formatted output into a new file named `vendors_revised.txt`.
- Includes basic error handling to capture and report any exceptions during file operations.

## How It Works
1. The script writes three vendor records to `vendors_raw.txt`.
2. It reads all lines from `vendors_raw.txt`.
3. Each line is split and reformatted to:  
   `"<Vendor> showcased <Data> at <Time>."`
4. The reformatted lines are saved to `vendors_revised.txt`.
5. If any error occurs during reading or writing, it is caught and displayed.

## Usage
- Run the script in an environment where you have read/write access to the current directory.
- Check the creation of both input and output files in the same directory as the script
