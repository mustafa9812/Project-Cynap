import numpy as np
import matplotlib.pyplot as plt

def approx_surface_area_pah(Nc): # number of carbon atoms in the molecule
    s_area = 5 * 10**(-16) * Nc # in cm^2
    return s_area

def approx_radius_pah(Nc):
    a = 0.9 * 10**(-8) * Nc**(1/2) # in cm
    return a

def FUV_absorption_cross_section(Nc):
    sigma = 7 * 10**(-18) * Nc # in cm^2
    return sigma

def UV_absorption_timescale(Nc,G0):
    # G0 is the radiation field in units of the Habing field
    t_UV = 1.4 * 10**(9) / (Nc*G0) # in seconds
    return t_UV

def vibrational_degrees_of_freedom(N):
    # For a PAH, the number of vibrational degrees of freedom is 3*N - 6
    return 3*N - 6

N = 19 # the total number of atoms in the molecule cyanonaphthalene
Nc = 11 # for cyanonaphthalene the number of carbon atoms is 11
G0 = 1.7 # Habing field, 1.7 is the value for the diffuse ISM
# Example usage

print("Number of vibrational degrees of freedom: ", vibrational_degrees_of_freedom(N))
print("Approximate surface area of cyanonaphthalene: ", approx_surface_area_pah(Nc), "cm^2")
print("Approximate radius of cyanonaphthalene: ", approx_radius_pah(Nc), "cm")
print("Approximate FUV absorption cross section of cyanonaphthalene: ", FUV_absorption_cross_section(Nc), "cm^2")
print("Approximate UV absorption timescale in the ISM: ", UV_absorption_timescale(Nc,G0), "seconds", "and which in years is: ", UV_absorption_timescale(Nc,G0)/3.154e7, "years")