def calculate_emission_factors():
  # Step 1: Define the constant for the EU population
  # https://european-union.europa.eu/principles-countries-history/facts-and-figures-european-union_en
  eu_population = 448000000

  # Step 2: Define raw data for districts and their populations
  population_data = {
      "Chemnitz, Stadt": 250681,
      "Erzgebirgskreis": 326896,
      "Mittelsachsen": 300308,
      "Vogtlandkreis": 221953,
      "Zwickau": 310111,
      "Dresden, Stadt": 566222,
      "Bautzen": 296506,
      "Görlitz": 248479,
      "Meißen": 241160,
      "Sächsische Schweiz-Osterzgebirge": 246011,
      "Leipzig, Stadt": 619879,
      "Leipzig": 261573,
      "Nordsachsen": 199688
  }

  # Step 3: Summarize the total population from all districts
  total_population = sum(population_data.values())
  # Step 4: Calculate the factor for total population relative to the EU
  total_factor = total_population / eu_population
  # print(f"Total Population: {total_population}, Factor: {total_factor}")

  # Ausgabe (optional)
#   for district, factor in emission_factors.items():
#       print(f"{district}: {factor}")

  # Step 5: Return the calculated factor
  return total_factor #, total_population