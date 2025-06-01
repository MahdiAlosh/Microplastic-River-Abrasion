import math
from .config import polymers#import math


def simulate_abrasion(total_length, w_eff_min, w_eff_max):
    results = {}

    for polymer in polymers:
        initial_diameter_um = 5000
        min_diameter_um = max_diameter_um = 30
        river_length_km = total_length

        density = polymers[polymer]["density"]
        a = polymers[polymer]["a"]

        diameter_um_min = initial_diameter_um
        remaining_km_min = river_length_km
        step_min = 0
        sum_volume_loss_um3_min = sum_volume_loss_um3_max = sum_mass_loss_mg_min = sum_mass_loss_mg_max = sum_loss_diameter_um_min = sum_loss_diameter_um_max = 0

        initial_volume_um3_min = (math.pi/6) * diameter_um_min**3

        while (diameter_um_min >= min_diameter_um) and (remaining_km_min > 0):
            step_min += 1
            d_m = diameter_um_min * 1e-6
            A = 0.5 * math.pi * d_m**2
            mass_loss_mg_min = (a * w_eff_min * 1000 * A)
            volume_loss_um3_min = (mass_loss_mg_min * 1e9) / density
            volume_loss_in_cm3_min = volume_loss_um3_min * 1e-12

            initial_volume_um3_min = (math.pi/6) * diameter_um_min**3
            new_volume_um3_min = initial_volume_um3_min - volume_loss_um3_min

            if new_volume_um3_min <= 0:
                break

            new_diameter_cm_min = (6 * volume_loss_in_cm3_min / math.pi) ** (1/3)
            new_diameter_um_min = new_diameter_cm_min * 1e4
            loss_diameter_um_min = diameter_um_min - new_diameter_um_min

            sum_volume_loss_um3_min += volume_loss_um3_min
            sum_mass_loss_mg_min += mass_loss_mg_min

            diameter_um_min = loss_diameter_um_min
            sum_loss_diameter_um_min += new_diameter_um_min

            remaining_km_min -= 1

        diameter_um_max = initial_diameter_um
        remaining_km_max = river_length_km
        step_max = 0
        initial_volume_um3_max = (math.pi/6) * diameter_um_max**3

        while (diameter_um_max >= max_diameter_um) and (remaining_km_max > 0):
            step_max += 1
            d_m = diameter_um_max * 1e-6
            A = 0.5 * math.pi * d_m**2
            mass_loss_mg_max = (a * w_eff_max * 1000 * A)
            volume_loss_um3_max = (mass_loss_mg_max * 1e9) / density
            volume_loss_in_cm3_max = volume_loss_um3_max * 1e-12

            initial_volume_um3_max = (math.pi/6) * diameter_um_max**3
            new_volume_um3_max = initial_volume_um3_max - volume_loss_um3_max

            if new_volume_um3_max <= 0:
                break

            new_diameter_cm_max = (6 * volume_loss_in_cm3_max / math.pi) ** (1/3)
            new_diameter_um_max = new_diameter_cm_max * 1e4
            loss_diameter_um_max = diameter_um_max - new_diameter_um_max

            sum_volume_loss_um3_max += volume_loss_um3_max
            sum_mass_loss_mg_max += mass_loss_mg_max

            diameter_um_max = loss_diameter_um_max
            sum_loss_diameter_um_max += new_diameter_um_max

            remaining_km_max -= 1

        results[polymer] = {
            'final_diameter_min': diameter_um_min,
            'final_diameter_max': diameter_um_max,
        }

def simulate_abrasion(total_length, w_eff_min, w_eff_max):
    results = {}

    for polymer in polymers:
        initial_diameter_um = 5000
        min_diameter_um = max_diameter_um = 30
        river_length_km = total_length

        density = polymers[polymer]["density"]
        a = polymers[polymer]["a"]

        diameter_um_min = initial_diameter_um
        remaining_km_min = river_length_km
        step_min = 0
        sum_volume_loss_um3_min = sum_volume_loss_um3_max = sum_mass_loss_mg_min = sum_mass_loss_mg_max = sum_loss_diameter_um_min = sum_loss_diameter_um_max = 0

        initial_volume_um3_min = (math.pi/6) * diameter_um_min**3

        while (diameter_um_min >= min_diameter_um) and (remaining_km_min > 0):
            step_min += 1
            d_m = diameter_um_min * 1e-6
            A = 0.5 * math.pi * d_m**2
            mass_loss_mg_min = (a * w_eff_min * 1000 * A)
            volume_loss_um3_min = (mass_loss_mg_min * 1e9) / density
            volume_loss_in_cm3_min = volume_loss_um3_min * 1e-12

            initial_volume_um3_min = (math.pi/6) * diameter_um_min**3
            new_volume_um3_min = initial_volume_um3_min - volume_loss_um3_min

            if new_volume_um3_min <= 0:
                break

            new_diameter_cm_min = (6 * volume_loss_in_cm3_min / math.pi) ** (1/3)
            new_diameter_um_min = new_diameter_cm_min * 1e4
            loss_diameter_um_min = diameter_um_min - new_diameter_um_min

            sum_volume_loss_um3_min += volume_loss_um3_min
            sum_mass_loss_mg_min += mass_loss_mg_min

            diameter_um_min = loss_diameter_um_min
            sum_loss_diameter_um_min += new_diameter_um_min

            remaining_km_min -= 1

        diameter_um_max = initial_diameter_um
        remaining_km_max = river_length_km
        step_max = 0
        initial_volume_um3_max = (math.pi/6) * diameter_um_max**3

        while (diameter_um_max >= max_diameter_um) and (remaining_km_max > 0):
            step_max += 1
            d_m = diameter_um_max * 1e-6
            A = 0.5 * math.pi * d_m**2
            mass_loss_mg_max = (a * w_eff_max * 1000 * A)
            volume_loss_um3_max = (mass_loss_mg_max * 1e9) / density
            volume_loss_in_cm3_max = volume_loss_um3_max * 1e-12

            initial_volume_um3_max = (math.pi/6) * diameter_um_max**3
            new_volume_um3_max = initial_volume_um3_max - volume_loss_um3_max

            if new_volume_um3_max <= 0:
                break

            new_diameter_cm_max = (6 * volume_loss_in_cm3_max / math.pi) ** (1/3)
            new_diameter_um_max = new_diameter_cm_max * 1e4
            loss_diameter_um_max = diameter_um_max - new_diameter_um_max

            sum_volume_loss_um3_max += volume_loss_um3_max
            sum_mass_loss_mg_max += mass_loss_mg_max

            diameter_um_max = loss_diameter_um_max
            sum_loss_diameter_um_max += new_diameter_um_max

            remaining_km_max -= 1

        results[polymer] = {
            'final_diameter_min': diameter_um_min,
            'final_diameter_max': diameter_um_max,
            'total_loss_diameter_min': sum_loss_diameter_um_min,
            'total_loss_diameter_max': sum_loss_diameter_um_max,
            'total_mass_loss_min': sum_mass_loss_mg_min,
            'total_mass_loss_max': sum_mass_loss_mg_max,
            'total_volume_loss_min': sum_volume_loss_um3_min,
            'total_volume_loss_max': sum_volume_loss_um3_max,
            'remaining_km_min': remaining_km_min,
            'remaining_km_max': remaining_km_max
        }

    return results
