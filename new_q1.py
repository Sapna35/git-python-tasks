import os

input_folder = "data_input"


if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"'{input_folder}' folder created. Please add .txt files into it and run the script again.")
    exit()

print(f"{input_folder}' folder exists. Proceeding to next step...")
