import math
from .config import polymers

def t6_simulate_abrasion(total_length, w_eff_min, w_eff_max):

    # Step 1: Initialize a dictionary to store simulation results for each polymer
    sim_results = {}
    for polymer in polymers:
        # Step 2: Set initial and minimum diameters (in meters)
        initial_diameter_m = 0.005 # in micrometer = 5000 µm
        min_diameter_m = max_diameter_m = 0.00003 # im micrometer = 30 µm
        river_length_km = total_length

        # Step 3: Get density and abrasion coefficient for the current polymer
        density = polymers[polymer]["density"]
        a = polymers[polymer]["a"]

        # Step 4: Initialize variables for the minimum abrasion scenario
        diameter_m_min = initial_diameter_m
        remaining_km_min = river_length_km
        step_min = 0
        sum_volume_loss_m3_min = sum_volume_loss_m3_max = sum_mass_loss_kg_min = sum_mass_loss_kg_max = sum_loss_diameter_m_min = sum_loss_diameter_m_max = 0

        # Calculate the initial volume of the particle (in cubic meters)
        initial_volume_m3_min = (math.pi/6) * diameter_m_min**3

        # Step 5: Simulate abrasion for minimum effective power
        while (diameter_m_min >= min_diameter_m) and (remaining_km_min > 0):
            step_min += 1

            # Step 5a: Calculate the contact area (A) in m²
            A = (0.5 * (1000 + 4 * (10*100))) / 1000000 # A = 1/2*(1000mm^2+4*(10*100)mm^2) => in quadratmer = 0,0025 m^2
            
            # Step 5b: Calculate mass and volume loss for this step
            mass_loss_kg_min = (a * w_eff_min * A)
            volume_loss_m3_min = mass_loss_kg_min / density

            # Step 5c: Calculate the new volume after abrasion
            initial_volume_m3_min = (math.pi/6) * diameter_m_min**3
            new_volume_m3_min = initial_volume_m3_min - volume_loss_m3_min

            sum_volume_loss_m3_min += volume_loss_m3_min
            sum_mass_loss_kg_min += mass_loss_kg_min

            # Step 5d: Stop if the particle is fully abraded
            if new_volume_m3_min <= 0:
                break

            # Step 5e: Calculate new diameter after abrasion
            new_diameter_m_min = (6 * new_volume_m3_min / math.pi) ** (1/3)
            loss_diameter_m_min = diameter_m_min - new_diameter_m_min
            sum_loss_diameter_m_min += new_diameter_m_min

            # Step 5f: Update diameter and remaining river length
            diameter_m_min = loss_diameter_m_min
            remaining_km_min -= 1

        
        # Step 6: Initialize variables for the maximum abrasion scenario
        diameter_m_max = initial_diameter_m
        remaining_km_max = river_length_km
        step_max = 0

        initial_volume_m3_max = (math.pi/6) * diameter_m_max**3

        while (diameter_m_max >= max_diameter_m) and (remaining_km_max > 0):
            step_max += 1

            A = (0.5 * (1000 + 4 * (10*100))) / 1000000
            mass_loss_kg_max = (a * w_eff_max * A)
            volume_loss_m3_max = mass_loss_kg_max / density

            initial_volume_m3_max = (math.pi/6) * diameter_m_max**3
            new_volume_m3_max = initial_volume_m3_max - volume_loss_m3_max

            sum_volume_loss_m3_max += volume_loss_m3_max
            sum_mass_loss_kg_max += mass_loss_kg_max

            if new_volume_m3_max <= 0:
                break

            new_diameter_m_max = (6 * new_volume_m3_max / math.pi) ** (1/3)
            loss_diameter_m_max = diameter_m_max - new_diameter_m_max
            sum_loss_diameter_m_max += new_diameter_m_max

            diameter_m_max = loss_diameter_m_max
            remaining_km_max -= 1

        # Step 7: Store all results for the current polymer
        sim_results[polymer] = {
            'final_diameter_min': diameter_m_min,
            'final_diameter_max': diameter_m_max,
            'total_loss_diameter_min': sum_loss_diameter_m_min,
            'total_loss_diameter_max': sum_loss_diameter_m_max,
            'total_mass_loss_min': sum_mass_loss_kg_min,
            'total_mass_loss_max': sum_mass_loss_kg_max,
            'total_volume_loss_min': sum_volume_loss_m3_min,
            'total_volume_loss_max': sum_volume_loss_m3_max,
            'remaining_km_min': remaining_km_min,
            'remaining_km_max': remaining_km_max
        }

    # Step 8: Return the simulation results for all polymers
    return sim_results
