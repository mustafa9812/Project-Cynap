import gzip
import shutil

# Paths to the input and output files
input_path = 'pahdb-complete-theoretical-v4.00-alpha_3gd93u5m0i5k5555C0T.xml.gz'
output_path = 'pahdb-complete-theoretical-v4.00-alpha_3gd93u5m0i5k5555C0T.xml'

# Decompress the file
with gzip.open(input_path, 'rb') as f_in:
    with open(output_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("✅ File decompressed successfully!")

