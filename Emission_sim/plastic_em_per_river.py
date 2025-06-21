from Emission_sim.calculate_number_of_emitted_MP import calculate_number_of_emitted_MP

def plastic_emission_per_river(data,  plastic_em):
  
  # Step 1: Initialize results dictionary and index counter
  em_results = {}
  index = 0

  # Step 2: Collect river types and their lengths if length > 0
  for _, row in data.iterrows():
      water_type = row["Type"]
      river_length = row["Length (km)"]
      if river_length > 0:
        index += 1
        em_results[water_type] = {
            "length": river_length
        }

  total_length = 0.0
  # Step 3: Calculate the total length of all rivers
  for _, length in em_results.items():
      # index = length['index']
      length = length['length']

      total_length += length 

  # Step 4: Calculate plastic emission per river (per km) for each polymer and size
  plastic_em_per_river_macro_ps = plastic_em[0] / total_length
  plastic_em_per_river_micro_ps = plastic_em[1] / total_length
  plastic_em_per_river_macro_pet = plastic_em[2] / total_length
  plastic_em_per_river_micro_pet = plastic_em[3] / total_length
  plastic_em_per_river_macro_pa = plastic_em[4] / total_length
  plastic_em_per_river_micro_pa = plastic_em[5] / total_length

  # Step 5: For each river type, calculate emission mass and number of emitted particles
  for river_type, length in em_results.items():
      # index = length['index']
      length = length['length']
      emission_mass_macro_ps = length * plastic_em_per_river_macro_ps
      emission_mass_micro_ps = length * plastic_em_per_river_micro_ps
      emission_mass_macro_pet = length * plastic_em_per_river_macro_pet
      emission_mass_micro_pet = length * plastic_em_per_river_micro_pet
      emission_mass_macro_pa = length * plastic_em_per_river_macro_pa
      emission_mass_micro_pa = length * plastic_em_per_river_micro_pa

      # Step 6: Calculate the number of emitted particles for each polymer and size
      number_of_emitted =  calculate_number_of_emitted_MP(emission_mass_macro_ps, emission_mass_micro_ps, emission_mass_macro_pet, emission_mass_micro_pet, emission_mass_macro_pa, emission_mass_micro_pa)
      
      # Step 7: Store the results in the dictionary
      em_results[river_type].update({
        # "emission_mass_macro_ps": emission_mass_macro_ps,
        # "emission_mass_micro_ps": emission_mass_micro_ps,
        # "emission_mass_macro_pet": emission_mass_macro_pet,
        # "emission_mass_micro_pet": emission_mass_micro_pet,
        # "emission_mass_macro_pa": emission_mass_macro_pa,
        # "emission_mass_micro_pa": emission_mass_micro_pa,
        "number_of_emitted_macro_ps": number_of_emitted[0],
        "number_of_emitted_micro_ps": number_of_emitted[1],
        "number_of_emitted_macro_pet": number_of_emitted[2],
        "number_of_emitted_micro_pet": number_of_emitted[3],
        "number_of_emitted_macro_pa": number_of_emitted[4],
        "number_of_emitted_micro_pa": number_of_emitted[5]
      })
  # Step 8: Return the results dictionary containing emission data for each river type
  return em_results
