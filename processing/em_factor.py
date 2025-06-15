def calculate_emission_factors():
  # Konstante für EU-Bevölkerung
  eu_population = 448000000

  # Rohdaten: District und deren Population
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

  # summrize population data
  total_population = sum(population_data.values())
  # factor for total population
  total_factor = total_population / eu_population
  # print(f"Total Population: {total_population}, Factor: {total_factor}")

  # Ergebnis-Dictionary mit Emission Factors
  emission_factors = {}

  # Berechnung
  for district, population in population_data.items():
      factor = population / eu_population
      emission_factors[district] = round(factor, 8)  # z.B. auf 8 Nachkommastellen gerundet

  # Ausgabe (optional)
#   for district, factor in emission_factors.items():
#       print(f"{district}: {factor}")

  return emission_factors, total_factor, total_population