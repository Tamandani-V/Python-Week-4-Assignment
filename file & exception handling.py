#Creating a sample input file
file_path = "vendors_raw.txt"
with open(file_path, "w") as file:
    file.write("Vendor: Apple | Data: iPhone 12 | Time: 10:00 AM\n")
    file.write("Vendor: Samsung | Data: Galaxy S21 | Time: 11:00 AM\n")
    file.write("Vendor: Google | Data: Pixel 5 | Time: 12:00 PM\n")

#Read and Modify
try:
    with open(file_path, "r") as infile:
        lines = infile.readlines()

    cleaned_lines = []
    for line in lines:
        parts = line.strip().split(" | ")
        vendor = parts[0].split(": ")[1]
        data = parts[1].split(": ")[1]
        time = parts[2].split(": ")[1]
        cleaned_lines.append(f"{vendor} showcased {data} at {time}.\n")

    #Writes modified file to a new file
    with open("vendors_revised.txt", "w") as outfile:
        outfile.writelines(cleaned_lines)

    print("✅ vendors_cleaned.txt has been created with formatted entries.")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")