# Calculate the number of emitted MP particles from emission masses
from math import pi

def calculate_number_of_emitted_MP(emission_mass_macro, emission_mass_micro):
  # density of plastic particles in kg/m³
  density = 980
  volume_macro = 0.0001  # volume of macroplastic particles in m³
  diameter_micro = 0.005 # diameter of microplastic particles in meters
  
  number_of_emitted_macro = emission_mass_macro / (density * volume_macro)
  number_of_emitted_micro = emission_mass_micro / (density * (1/6) * pi * diameter_micro**3)
  
  # print(f"Number of emitted macroplastic particles: {number_of_emitted_macro}")
  # print(f"Number of emitted microplastic particles: {number_of_emitted_micro}")

  return number_of_emitted_macro, number_of_emitted_micro