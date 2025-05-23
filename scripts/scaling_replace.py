import pandas as pd

df1 = pd.read_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\IRspectrum_ts_CNna.dat', 
                 skiprows=2, 
                 sep='\s+', 
                 names=["freq", "Inten"])

N_frequency_scaled = (df1['freq'] * 0.96).tolist()
#print(N_frequency_scaled)

df2 = pd.read_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\IRspectrum_ts_CNna+.dat', 
                 skiprows=2, 
                 sep='\s+', 
                 names=["freq", "Inten"])

C_frequency_scaled = (df2['freq'] * 0.96).tolist()
#print(C_frequency_scaled)

df3 = pd.read_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\C_scaled_TSvibrational_spectrum.txt',
                skiprows=1, 
                sep='\s+', 
                names=["freq", "Inten"])

C_TS_frequency = df3['freq'].tolist()[1:]
#print(C_TS_frequency)

# if len(C_frequency_scaled) == len(df3):
#     df3['freq'] = C_frequency_scaled

# df3.to_csv('C_scaled_output.txt', sep='\t', index=False)

df4 = pd.read_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\Densum_input_1cyano\Models\TS-C-1-cyanonaphthalene\vibs\densum.dat',
                skiprows=4, 
                sep='\s+', 
                names=["mode", "type", "freq", "harmonicity", "false", "mark"])

if len(C_TS_frequency) == len(df4):
    df4['freq'] = C_TS_frequency

# df4.to_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\Densum_input_1cyano\Models\TS-C-1-cyanonaphthalene\vibs\densum_scaled.dat', sep='\t', index=False)

# df5 = pd.read_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\IRspectrum_1CNpy.dat',
#                 skiprows=2,
#                 sep='\s+',
#                 names=["freq", "Inten"])

# Npy_frequency_scaled = (df5['freq'] * 0.96).tolist()

# df6 = pd.read_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\CNpy_scaled.txt',
#                 skiprows=1,
#                 sep='\s+',
#                 names=["freq", "Inten"])

# if len(Npy_frequency_scaled) == len(df6):
#     df6['freq'] = Npy_frequency_scaled

#df6.to_csv(r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\CNpy_scaled_output.txt', sep='\t', index=False)

df = pd.read_csv(
    r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\IRspectrum_1CNpy+.dat',
    skiprows=2,
    sep='\s+',
    names=["freq", "Inten"]
)

df['freq'] = df['freq'] * 0.96

# df.to_csv(
#     r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\CNpy+_scaled_output.txt',
#     sep='\t',
#     index=False
# )

df_scaled = pd.read_csv(
    r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\CNpy+_scaled_output.txt',
    sep='\s+',
    names=["freq", "Inten"],
    header=0  # If your output file has a header, otherwise use header=None
)

scaled_freqs = df_scaled['freq'].tolist()

# Read densum.dat
df_densum = pd.read_csv(
    r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\Densum_input_1cyano\Models\C-2-cyanopyrene\vibs\densum.dat',
    skiprows=4,
    sep='\s+',
    names=["mode", "type", "freq", "harmonicity", "false", "mark"]
)

# Replace frequencies if lengths match
if len(scaled_freqs) == len(df_densum):
    df_densum['freq'] = scaled_freqs
    # Save to a new file
    df_densum.to_csv(
        r'C:\Users\Mustafa\Documents\GitHub\Project-Cynap\Cynapfolder\Database\Densum_input_1cyano\Models\C-2-cyanopyrene\vibs\densum_scaled.dat',
        sep='\t',
        index=False
    )
else:
    print("Length mismatch: scaled frequencies")