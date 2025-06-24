# Project Cynap
 
Project Cynap is a computational chemistry project focused on astrochemistry of cyano-substituted polycyclic aromatic hydrocarbons (PAHs), such as 1-cyanonaphthalene and 2-cyanopyrene. The repository contains:

- **Cynapfolder/Database/**: Contains theoretical and experimental data, including the NASA Ames PAH IR Spectroscopic Database & Gaussian 09 vibrational frequencies and Densum vibrational density of states outputs.
- **scripts/**: Jupyter notebooks and Python scripts for calculations, calculations.ipynb and calculations_cpy contains the rate coefficient calculations and Monte Carlo simulations for 1-cyanonaphthalene+ and 1-cyanopyrene+ respectively. full_vibfreq includes the vibrational frequency extraction from the NASA Ames PAH IR Spectroscopic Database through the AmesPAHdb package. To run code I suggest to download the following vibrational frequency dataset: pahdb-complete-theoretical-v4.00-alpha
- **plots/**: Output figures from simulations and analyses, such as dissociation rates, survival probabilities, comparison plots and simulations.
- **runs/**: Simulation results in TSV format for different molecules and conditions.

The code uses data from the Ames PAHdb and Densum outputs to model dissociation, cooling, and survival of PAHs under astrophysical conditions, with results visualized in the plots directory.