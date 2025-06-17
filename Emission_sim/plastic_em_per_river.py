from Emission_sim.plastic_emission import plastic_emission

def plastic_emission_per_river(data,  plastic_em):
  
  results = {}
  index = 0

  for _, row in data.iterrows():
      water_type = row["Type"]
      river_length = row["Length (km)"]
      if river_length > 0:
        index += 1
        results[water_type] = {
            "index": index,
            "length: ": river_length
        }

  total_length = 0.0
  # Calculate the plastic emission per river
  for _, length in results.items():
      index = length['index']
      length = length['length: ']

      total_length += length 

      # print(f"River index: {index}, \t length: {length} km") # both are values, because keys are the name of the river type
      # print(f"Plastic Emission Macro: {plastic_em[0]:.2f} kg")
      # plastic_em_per_river_macro = plastic_em[0] / length
      # print(f"Plastic Emission Macro per River {index}: {plastic_em_per_river_macro:.2f} kg/km")
      # print(f"Plastic Emission Micro: {plastic_em[1]:.2f} kg")
      # plastic_em_per_river_micro = plastic_em[1] / length
      # print(f"Plastic Emission Micro per River {index}: {plastic_em_per_river_micro:.2f} kg/km")
      

  print(f"Plastic Emission Macro: {plastic_em[0]:.2f} kg")
  print(f"Plastic Emission Micro: {plastic_em[1]:.2f} kg")
  print(f"Total Length of All Rivers: {total_length:.2f} km")
  plastic_em_per_river_macro = plastic_em[0] / total_length
  plastic_em_per_river_micro = plastic_em[1] / total_length
  print(f"Plastic Emission Macro per River: {plastic_em_per_river_macro:.2f} kg/km")
  print(f"Plastic Emission Micro per River: {plastic_em_per_river_micro:.2f} kg/km")


  # print("Results:\n", results)
  # print(f"Plastic Emission Macro: {plastic_em[0]:.2f} kg")
  # print(f"Plastic Emission Micro: {plastic_em[1]:.2f} kg")
