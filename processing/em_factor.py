def calculate_emission_factors():
  # Step 1: Define the constant for the EU population
  # https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Population_structure_and_ageing#Source_data_for_tables_and_graphs
  eu_population = 449300000

  # Step 2: Define the constant Saxon populatio
  # https://www.bevoelkerungsmonitor.sachsen.de/bevoelkerungsbestand.html#a-20463 
  saxony_population = 4100000

  
  # Step 4: Calculate the factor for total population relative to the EU
  total_factor = saxony_population / eu_population
  # print(f"Total Population: {total_population}, Factor: {total_factor}")

  # Ausgabe (optional)
#   for district, factor in emission_factors.items():
#       print(f"{district}: {factor}")

  # Step 5: Return the calculated factor
  return total_factor #, total_population