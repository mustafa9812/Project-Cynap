from amespahdbpythonsuite.amespahdb import AmesPAHdb

# Path to your downloaded XML file
xml_file = r"C:\Users\Mustafa\Downloads\pahdb-selection-theoretical-v3.20_2dhf1bcoblsg65L7BE0.xml"

# Load the database from your file
pahdb = AmesPAHdb(filename=xml_file, check=False, cache=False)

# List all available UIDs (Unique IDs for molecules in the DB)
uids = pahdb.getuids()
print("Available UIDs:", uids)

# Pick one UID (like the first one for now)
transitions = pahdb.gettransitionsbyuid([uids[0]])

# Plot the raw stick spectrum
transitions.plot(show=True)

# Optionally: Calculate emission cascade spectrum at 6 eV
transitions.cascade(6 * 1.603e-12, multiprocessing=False)
transitions.plot(show=True)

# Optionally: Convolve with Gaussian
convolved = transitions.convolve(fwhm=15.0, gaussian=True, multiprocessing=False)
convolved.plot(show=True)