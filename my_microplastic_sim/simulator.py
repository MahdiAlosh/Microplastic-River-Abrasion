import math
from .config import polymers
from math import pi
# from config import polymers

def t6_simulate_abrasion(exposure_time_min, exposure_time_max, w_eff_min, w_eff_max):

    # Step 1: Initialize a dictionary to store simulation results for each polymer
    sim_results = {}
    for polymer in polymers:
        # Step 2: Set initial and minimum diameters (in meters)
        initial_diameter_m = 0.005 # in micrometer = 5000 µm
        min_diameter_m = max_diameter_m = 0.00003 # im micrometer = 30 µm
        exposure_time_min_h = exposure_time_min

        # Step 3: Get density and abrasion coefficient for the current polymer
        density = polymers[polymer]["density"]
        a_pol = polymers[polymer]["a"] * 3600       #convert from mg/m²s to mg/m²h

        # Step 4: Initialize variables for the minimum abrasion scenario
        diameter_m_min = initial_diameter_m
        remaining_h_min_micro = exposure_time_min_h
        step_min = 0
        sum_volume_loss_m3_micro_min = sum_volume_loss_m3_micro_max = sum_mass_loss_kg_micro_min = sum_mass_loss_kg_micro_max = sum_loss_diameter_m_micro_min = sum_loss_diameter_m_micro_max = 0

        # Calculate the initial volume of the particle (in cubic meters)
        initial_volume_m3_min = (math.pi/6) * diameter_m_min**3 # for macro initial volume as V = a*b*c

        # Step 5: Simulate abrasion for minimum effective power
        while (diameter_m_min >= min_diameter_m) and (remaining_h_min_micro > 0): # iintil c <= 0
            step_min += 1

            # Step 5a: Calculate the contact area (A) in m²
            # A = (0.5 * (1000 + 4 * (10*100))) / 1000000 # A = 1/2*(1000mm^2+4*(10*100)mm^2) => in quadratmer = 0,0025 m^2 # for macro v = a * b
            
            A = (0.5 * (pi * (diameter_m_min**2)))

            # Step 5b: Calculate mass and volume loss for this step
            mass_loss_kg_min = (a_pol * w_eff_min * A) / 1000000
            volume_loss_m3_min = mass_loss_kg_min / density

            # Step 5c: Calculate the new volume after abrasion
            initial_volume_m3_min = (math.pi/6) * (diameter_m_min**3)
            new_volume_m3_min = initial_volume_m3_min - volume_loss_m3_min

            sum_volume_loss_m3_micro_min += volume_loss_m3_min
            sum_mass_loss_kg_micro_min += mass_loss_kg_min

            # Step 5d: Stop if the particle is fully abraded
            if new_volume_m3_min <= 0:
                break

            # Step 5e: Calculate new diameter after abrasion
            new_diameter_m_min = (6 * new_volume_m3_min / math.pi) ** (1/3) # for macro c = v/(a*b)
            loss_diameter_m_min = diameter_m_min - new_diameter_m_min
            sum_loss_diameter_m_micro_min += new_diameter_m_min

            # Step 5f: Update diameter and remaining river length
            diameter_m_min = loss_diameter_m_min
            remaining_h_min_micro -= 1

        
        # Step 6: Initialize variables for the maximum abrasion scenario
        diameter_m_max = initial_diameter_m
        exposure_time_max_h = exposure_time_max
        remaining_h_max_micro = exposure_time_max_h
        step_max = 0

        initial_volume_m3_max = (math.pi/6) * diameter_m_max**3

        while (diameter_m_max >= max_diameter_m) and (remaining_h_max_micro > 0):
            step_max += 1

            A = (0.5 * (pi * (diameter_m_max**2)))
            mass_loss_kg_max = (a_pol * w_eff_max * A) / 1000000
            volume_loss_m3_max = mass_loss_kg_max / density

            initial_volume_m3_max = (math.pi/6) * (diameter_m_max**3)
            new_volume_m3_max = initial_volume_m3_max - volume_loss_m3_max

            sum_volume_loss_m3_micro_max += volume_loss_m3_max
            sum_mass_loss_kg_micro_max += mass_loss_kg_max

            if new_volume_m3_max <= 0:
                break

            new_diameter_m_max = (6 * new_volume_m3_max / math.pi) ** (1/3)
            loss_diameter_m_max = diameter_m_max - new_diameter_m_max
            sum_loss_diameter_m_micro_max += new_diameter_m_max

            diameter_m_max = loss_diameter_m_max
            remaining_h_max_micro -= 1

# ===========================================================
        a = 0.1 # in m
        b = 0.1 # in m
        c_initial = 0.01  # in m
        c_current_min = c_initial
        step_min = 0
        sum_volume_loss_m3_macro_min = sum_mass_loss_kg_macro_min = sum_loss_height_m_min = 0
        remaining_h_min_macro = exposure_time_min_h

        # Calculate the initial volume of the cube (in cubic meters)
        initial_volume_m3_min = a * b * c_current_min

        # Simulate abrasion for minimum effective power
        while (c_current_min >= min_diameter_m) and (remaining_h_min_macro > 0):
            step_min += 1
            base_area_mm2 = 100 * 100  # 10000 mm²
            side_area_mm2 = c_current_min * 1000 * 100  # convert c to mm, multiply by width
            #total_surface_area_mm2 = base_area_mm2 + 4 * side_area_mm2
            # A = 0.5 * total_surface_area_mm2 / 1000000  # convert to m² and take half
            A = a * b

            mass_loss_kg_min = (a_pol * w_eff_min * A) / 1000000
            volume_loss_m3_min = mass_loss_kg_min / density

            current_volume_m3_min = a * b * c_current_min
            new_volume_m3_min = current_volume_m3_min - volume_loss_m3_min
            sum_volume_loss_m3_macro_min += volume_loss_m3_min
            sum_mass_loss_kg_macro_min += mass_loss_kg_min

            if new_volume_m3_min <= 0:
                break

            # Since V = a * b * c, and a, b remain constant: c_new = V_new / (a * b)
            c_new_min = new_volume_m3_min / (a * b)
            loss_height_m_min = c_current_min - c_new_min
            sum_loss_height_m_min += loss_height_m_min

            # Update height and remaining river length
            c_current_min = c_new_min
            remaining_h_min_macro -= 1
        
        # Similar structure for maximum abrasion scenario
        c_current_max = c_initial
        remaining_h_max_macro = exposure_time_max_h
        step_max = 0
        sum_volume_loss_m3_macro_max = sum_mass_loss_kg_macro_max = sum_loss_height_m_max = 0

        while (c_current_max >= max_diameter_m) and (remaining_h_max_macro > 0):
            step_max += 1
            
            # Calculate contact area for max scenario
            A = a * b
            # Calculate losses for max scenario
            mass_loss_kg_max = (a_pol * w_eff_max * A) / 1000000
            volume_loss_m3_max = mass_loss_kg_max / density
            
            current_volume_m3_max = a * b * c_current_max
            new_volume_m3_max = current_volume_m3_max - volume_loss_m3_max
            sum_volume_loss_m3_macro_max += volume_loss_m3_max
            sum_mass_loss_kg_macro_max += mass_loss_kg_max
            
            if new_volume_m3_max <= 0:
                break
            
            c_new_max = new_volume_m3_max / (a * b)
            loss_height_m_max = c_current_max - c_new_max
            sum_loss_height_m_max += loss_height_m_max
            
            c_current_max = c_new_max
            remaining_h_max_macro -= 1

# ===========================================================

        # Step 7: Store all results for the current polymer
        sim_results[polymer] = { # 4 values => micro and macro
            'final_diameter_min': diameter_m_min,
            'final_diameter_max': diameter_m_max,
            'total_loss_diameter_micro_min': sum_loss_diameter_m_micro_min,
            'total_loss_diameter_micro_max': sum_loss_diameter_m_micro_max,
            'total_mass_loss_micro_min': sum_mass_loss_kg_micro_min,
            'total_mass_loss_micro_max': sum_mass_loss_kg_micro_max,
            'total_mass_loss_macro_min': sum_mass_loss_kg_macro_min,
            'total_mass_loss_macro_max': sum_mass_loss_kg_macro_max,
            'total_volume_loss_micro_min': sum_volume_loss_m3_micro_min,
            'total_volume_loss_micro_max': sum_volume_loss_m3_micro_max,
            'total_volume_loss_macro_min': sum_volume_loss_m3_macro_min,
            'total_volume_loss_macro_max': sum_volume_loss_m3_macro_max,
            'remaining_h_min_micro': remaining_h_min_micro,
            'remaining_h_max_micro': remaining_h_max_micro,
            'remaining_h_min_macro': remaining_h_min_macro,
            'remaining_h_max_macro': remaining_h_max_macro
        }

    # Step 8: Return the simulation results for all polymers
    return sim_results

# print(t6_simulate_abrasion(100.0, 0.1, 0.2))
