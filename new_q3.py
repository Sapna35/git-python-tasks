import os

input_folder = "data_input"
output_folder = "data_output"


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

summary = []

for filename in txt_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    line_count = 0
    word_count = 0
    modified_lines = []

    with open(input_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.strip().startswith("#"):
                continue

            line_count += 1
            word_count += len(line.split())

            modified_line = line.replace("temp", "permanent")
            modified_lines.append(modified_line)

    with open(output_path, 'w') as file:
        file.writelines(modified_lines)

    summary.append((filename, line_count, word_count))
    print(f"Processed {filename}: {line_count} lines, {word_count} words")
