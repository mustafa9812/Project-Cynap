import subprocess

densum_input_dir = r"C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\Densum_input_1cyano\Models\other-TS-C-2-cyanopyrene\vibs"
densum_input_file = "densum.dat"
densum_exe_path = r"C:\Users\Mustafa\Documents\MultiWell\multiwell-2023-windows\bin\densum.exe"

result = subprocess.run(
    [densum_exe_path, densum_input_file],
    cwd=densum_input_dir,  # Set working directory
    capture_output=True,
    text=True
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)