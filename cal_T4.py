import math

# Polymer properties (density in g/cm³)
polymers = {
    "ps_tio": {"a": 1.00036, "density": 1.05},
    "ps": {"a": 0.81021, "density": 1.05},
    "petg": {"a": 0.52683, "density": 1.27},
    "pet": {"a": 0.35373, "density": 1.39},
    "pa6": {"a": 0.32447, "density": 1.14}
}

# polymer = "pa6"

def simulate_abrasion():
    
    for polymer in polymers:
        # Simulation parameters
        initial_diameter_um = 5000  # 5 mm in µm
        min_diameter_um = max_diameter_um = 30  # Abruchkriterium
        river_length_km = 66.46
        w_eff_min = 14.8226336925046    # W/m²
        w_eff_max = 1091.790083         # W/m²
        
        density = polymers[polymer]["density"]
        a = polymers[polymer]["a"]
        
        diameter_um_min = initial_diameter_um
        remaining_km_min = river_length_km
        step_min = 0
        sum_volume_loss_um3_min = sum_volume_loss_um3_max = sum_mass_loss_mg_min = sum_mass_loss_mg_max = 0

        print(f"Simulation für {polymer} über {river_length_km} km")
        print(f"Startdurchmesser: {diameter_um_min} µm")
        initial_volume_um3_min = (math.pi/6) * diameter_um_min**3
        print(f"Initial Volume (min): {initial_volume_um3_min:.2f} µm³")
        print("="*50)

        while (diameter_um_min >= min_diameter_um) and (remaining_km_min > 0):
            step_min += 1
            # Convert to meters
            d_m = diameter_um_min * 1e-6
            
            # 1. Calculate contact area (m²)
            A = 0.5 * math.pi * d_m**2
            
            # 2. Calculate mass loss (mg/km)
            mass_loss_mg_min = (a * w_eff_min * 1000 * A)
            
            # 3. Calculate volume loss (µm³/km)
            volume_loss_um3_min = (mass_loss_mg_min * 1e9) / density  # mg → µg → µm³
            
            # 4. Update volume (µm³)
            initial_volume_um3_min = (math.pi/6) * diameter_um_min**3
            print(f"Initial Volume (min): {initial_volume_um3_min:.2f} µm³")
            new_volume_um3_min = initial_volume_um3_min - volume_loss_um3_min
            print(f"New Volume (min): {new_volume_um3_min:.2f} µm³")
            
            if new_volume_um3_min <= 0:
                print(f"Partikel vollständig abradiert nach {step_min} Schritten")
                break
                
            # 5. Calculate new diameter (µm)
            new_diameter_um_min = (6 * new_volume_um3_min / math.pi) ** (1/3)
            
            # Progress output
            print(f"Schritt {step_min}:")
            print(f"• Durchmesser (min): {diameter_um_min:.2f} → {new_diameter_um_min:.2f} µm")
            print(f"• Massenverlust (min): {mass_loss_mg_min:.6f} mg/km")
            print(f"• Volumenverlust (min): {volume_loss_um3_min:.2f} µm³")
            print("-"*50)
            
            # sum up volume loss (min)
            sum_volume_loss_um3_min += volume_loss_um3_min

            # sum up mass loss (min)
            sum_mass_loss_mg_min += mass_loss_mg_min

            # Update for next iteration
            diameter_um_min = new_diameter_um_min # um -> µm

            remaining_km_min -= 1


        # Now calculate the maximum diameter
        print("*"*50)
        diameter_um_max = initial_diameter_um
        remaining_km_max = river_length_km
        step_max = 0
        print(f"\nSimulation für {polymer} über {river_length_km} km")
        print(f"Startdurchmesser: {diameter_um_max} µm")
        initial_volume_um3_max = (math.pi/6) * diameter_um_max**3
        print(f"Initial Volume (max): {initial_volume_um3_max:.2f} µm³")
        print("="*50)

        while (diameter_um_max >= max_diameter_um) and (remaining_km_max > 0):
            step_max += 1
            # Convert to meters
            d_m = diameter_um_max * 1e-6
            
            # 1. Calculate contact area (m²)
            A = 0.5 * math.pi * d_m**2
            
            # 2. Calculate mass loss (mg/km)
            mass_loss_mg_max = (a * w_eff_max * 1000 * A)
            
            # 3. Calculate volume loss (µm³/km)
            volume_loss_um3_max = (mass_loss_mg_max * 1e9) / density
            
            # 4. Update volume (µm³)
            initial_volume_um3_max = (math.pi/6) * diameter_um_max**3
            print(f"Initial Volume (max): {initial_volume_um3_max:.2f} µm³")
            new_volume_um3_max = initial_volume_um3_max - volume_loss_um3_max
            print(f"New Volume (max): {new_volume_um3_max:.2f} µm³")
            
            if new_volume_um3_max <= 0:
                print(f"Partikel vollständig abradiert nach {step_max} Schritten")
                break
                
            # 5. Calculate new diameter (µm)
            new_diameter_um_max = (6 * new_volume_um3_max / math.pi) ** (1/3)
            
            # Progress output
            print(f"Schritt {step_max}:")
            print(f"• Durchmesser (max): {diameter_um_max:.2f} → {new_diameter_um_max:.2f} µm")
            print(f"• Massenverlust (max): {mass_loss_mg_max:.6f} mg/km")
            print(f"• Volumenverlust (max): {volume_loss_um3_max:.2f} µm³")
            print("-"*50)
            
            # sum up volume loss (max)
            sum_volume_loss_um3_max += volume_loss_um3_max

            # sum up mass loss (max)
            sum_mass_loss_mg_max += mass_loss_mg_max

            # Update for next iteration
            diameter_um_max = new_diameter_um_max # um -> µm

            remaining_km_max -= 1


        print("\nEndergebnis:")
        print(f"MIN: Finaler Durchmesser: {diameter_um_min:.2f} µm")
        print(f"MAX: Finaler Durchmesser: {diameter_um_max:.2f} µm")
        print(f"MIN: Gesamtmassenverlust: {sum_mass_loss_mg_min:.2f} mg")
        print(f"MAX: Gesamtmassenverlust: {sum_mass_loss_mg_max:.2f} mg")
        print(f"MIN: Gesamtvolumenverlust: {sum_volume_loss_um3_min:.2f} µm³")
        print(f"MAX: Gesamtvolumenverlust: {sum_volume_loss_um3_max:.2f} µm³")
        print(f"MIN: Reststrecke: {remaining_km_min:.2f} km")
        print(f"MAX: Reststrecke: {remaining_km_max:.2f} km")
        print("="*50)

        
def main():
    simulate_abrasion()

if __name__ == "__main__":
    main()