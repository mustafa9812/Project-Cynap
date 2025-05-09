import os
import subprocess

# Define paths
densum_input_path = r"C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\Densum_input_1cyano\Models\1-cyanonaphthalene\vibs\densum.dat"
densum_exe_path = r"C:\Users\Mustafa\Documents\MultiWell\multiwell-2023-windows\bin\densum.exe"
output_dir = os.path.join(os.path.dirname(densum_input_path), "densum_mode_sweeps")

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Read original densum.dat
with open(densum_input_path, 'r') as f:
    lines = f.readlines()

# Identify vibrational mode lines (e.g., "1 vib 102.6893 0.0 1 !")
mode_lines = [line for line in lines if line.strip().split()[0].isdigit() and "vib" in line]

# Base (non-mode) content
prefix_lines = [line for line in lines if line not in mode_lines]

# Iterate over modes
for i, removed_line in enumerate(mode_lines):
    mode_index = i + 1

    mode_dir = os.path.join(output_dir, f"mode_{mode_index}")
    os.makedirs(mode_dir, exist_ok=True)

    # Adjust header line (assume it's line 3)
    modified_lines = lines.copy()
    header_idx = 2  # Usually line index 2
    parts = modified_lines[header_idx].split()
    if parts[0].isdigit():
        original_mode_count = int(parts[0])
        parts[0] = str(original_mode_count - 1)
        modified_lines[header_idx] = "    ".join(parts) + "\n"

    # Remove selected mode
    modified_lines = [line for line in modified_lines if line != removed_line]

    # Save as densum.dat
    input_path = os.path.join(mode_dir, "densum.dat")
    with open(input_path, 'w') as f:
        f.writelines(modified_lines)

    # Run densum
    result = subprocess.run(
        [densum_exe_path],
        cwd=mode_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Log output
    log_path = os.path.join(mode_dir, "densum_log.txt")
    with open(log_path, 'w') as log_file:
        log_file.write(result.stdout)
        log_file.write("\n--- STDERR ---\n")
        log_file.write(result.stderr)

    print(f"Finished mode {mode_index}")

