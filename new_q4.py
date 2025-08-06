import os

output_folder = "data_output"
summary = [("file1.txt", 10, 100), ("file2.txt", 8, 76)]  
summary_path = os.path.join(output_folder, "summary.txt")

with open(summary_path, 'w') as summary_file:
    summary_file.write("Filename\tLines\tWords\n")
    summary_file.write("-" * 30 + "\n")
    for filename, lines, words in summary:
        summary_file.write(f"{filename}\t{lines}\t{words}\n")

print("Summary written to data_output/summary.txt")
