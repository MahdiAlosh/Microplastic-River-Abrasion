from Emission_sim.calculate_number_of_emitted_MP import calculate_number_of_emitted_MP

def plastic_emission_per_river(data,  plastic_em):
  
  em_results = {}
  index = 0

  for _, row in data.iterrows():
      water_type = row["Type"]
      river_length = row["Length (km)"]
      if river_length > 0:
        index += 1
        em_results[water_type] = {
            "length": river_length
        }

  total_length = 0.0
  # Calculate the plastic emission per river
  for _, length in em_results.items():
      # index = length['index']
      length = length['length']

      total_length += length 

  # print(f"Plastic Emission Macro: {plastic_em[0]:.2f} kg")
  # print(f"Plastic Emission Micro: {plastic_em[1]:.2f} kg")
  # print(f"Total Length of All Rivers: {total_length:.2f} km")

  plastic_em_per_river_macro_ps = plastic_em[0] / total_length
  plastic_em_per_river_micro_ps = plastic_em[1] / total_length
  plastic_em_per_river_macro_pet = plastic_em[2] / total_length
  plastic_em_per_river_micro_pet = plastic_em[3] / total_length
  plastic_em_per_river_macro_pa = plastic_em[4] / total_length
  plastic_em_per_river_micro_pa = plastic_em[5] / total_length

  # print(f"Plastic Emission Macro per River: {plastic_em_per_river_macro:.2f} kg/km")
  # print(f"Plastic Emission Micro per River: {plastic_em_per_river_micro:.2f} kg/km")

  # emission mass = river type length * plastic emission per km
  # total_emission_mass_macro = 0.0
  # total_emission_mass_micro = 0.0

  for river_type, length in em_results.items():
      # index = length['index']
      length = length['length']
      emission_mass_macro_ps = length * plastic_em_per_river_macro_ps
      emission_mass_micro_ps = length * plastic_em_per_river_micro_ps
      emission_mass_macro_pet = length * plastic_em_per_river_macro_pet
      emission_mass_micro_pet = length * plastic_em_per_river_micro_pet
      emission_mass_macro_pa = length * plastic_em_per_river_macro_pa
      emission_mass_micro_pa = length * plastic_em_per_river_micro_pa

      number_of_emitted =  calculate_number_of_emitted_MP(emission_mass_macro_ps, emission_mass_micro_ps, emission_mass_macro_pet, emission_mass_micro_pet, emission_mass_macro_pa, emission_mass_micro_pa)
      
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

  return em_results
  # =================================================================== 
  #     total_emission_mass_macro += emission_mass_macro
  #     total_emission_mass_micro += emission_mass_micro

  # print(f"Total Emission Mass Macro: {total_emission_mass_macro} kg")
  # print(f"Total Emission Mass Micro: {total_emission_mass_micro} kg")

  # print("Results:\n", em_results)
  # print(f"Plastic Emission Macro: {plastic_em[0]:.2f} kg")
  # print(f"Plastic Emission Micro: {plastic_em[1]:.2f} kg")

  # calculate_number_of_emitted_MP(total_emission_mass_macro, total_emission_mass_micro)



  """
  Typ 5: Grobmaterialreiche, silikatische Mittelgebirgsbäche
  River index: 1, Length: 2832.52 km
  Emission Mass Macro: 1704.22 kg
  Emission Mass Micro: 1495.43 kg
  Number of emitted macroplastic particles: 17389,99283
  Number of emitted microplastic particles: 23314793.567154568

  Wobei:
  density = 980,
  volume_macro = 0.0001  # volume of macroplastic particles in m³,
  diameter_micro = 0.005 # diameter of microplastic particles in meters
  """