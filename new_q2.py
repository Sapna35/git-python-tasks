import os

input_folder = "data_input"


files = os.listdir(input_folder)


txt_files = [file for file in files if file.endswith(".txt")]


if not txt_files:
    print("No .txt files found in the 'data_input' folder. Please add some and try again.")
    exit()


print("Found .txt files:")
for file in txt_files:
    print("-", file)
