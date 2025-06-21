# Calculate the number of emitted MP particles from emission masses
from math import pi
from my_microplastic_sim.config import polymers

def calculate_number_of_emitted_MP(emission_mass_macro_ps, emission_mass_micro_ps, emission_mass_macro_pet, emission_mass_micro_pet, emission_mass_macro_pa, emission_mass_micro_pa):
  # density of plastic particles in kg/m³
  volume_macro = 0.0001  # volume of macroplastic particles in m³
  diameter_micro = 0.005 # diameter of microplastic particles in meters
  
  number_of_emitted_macro_ps = emission_mass_macro_ps / (polymers["ps"]["density"] * volume_macro)
  number_of_emitted_micro_ps = emission_mass_micro_ps / (polymers["ps"]["density"] * (1/6) * pi * diameter_micro**3)
  number_of_emitted_macro_pet = emission_mass_macro_pet / (polymers["pet"]["density"] * volume_macro)
  number_of_emitted_micro_pet = emission_mass_micro_pet / (polymers["pet"]["density"] * (1/6) * pi * diameter_micro**3)
  number_of_emitted_macro_pa = emission_mass_macro_pa / (polymers["pa"]["density"] * volume_macro)
  number_of_emitted_micro_pa = emission_mass_micro_pa / (polymers["pa"]["density"] * (1/6) * pi * diameter_micro**3)
  
  # print(f"Number of emitted macroplastic particles: {number_of_emitted_macro}")
  # print(f"Number of emitted microplastic particles: {number_of_emitted_micro}")

  return (number_of_emitted_macro_ps, number_of_emitted_micro_ps, number_of_emitted_macro_pet, number_of_emitted_micro_pet, number_of_emitted_macro_pa, number_of_emitted_micro_pa)