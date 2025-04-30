import math

# Polymer properties (density in g/cm³)
polymers = {
    "ps_tio": {"a": 1.00036, "density": 1.05},
    "ps": {"a": 0.81021, "density": 1.05},
    "petg": {"a": 0.52683, "density": 1.27},
    "pet": {"a": 0.35373, "density": 1.39},
    "pa6": {"a": 0.32447, "density": 1.14}
}

# Simulation parameters
initial_diameter_um = 5000  # 5 mm in µm
min_diameter_um = 30        # Abruchkriterium
river_length_km = 66.46
w_eff_min = 14.8226336925046    # W/m²
w_eff_max = 1091.790083         # W/m²
polymer = "ps_tio"          # Test mit PS/TiO2

def simulate_abrasion():
    diameter_um_min = diameter_um_max = initial_diameter_um
    remaining_km = river_length_km
    step = 0
    
    print(f"Simulation für {polymer} über {river_length_km} km")
    print(f"Startdurchmesser: {diameter_um_min} µm")
    initial_volume_um3_min = (math.pi/6) * diameter_um_min**3
    initial_volume_um3_max = (math.pi/6) * diameter_um_max**3
    print(f"Initial Volume (min): {initial_volume_um3_min:.2f} µm³")
    print(f"Initial Volume (max): {initial_volume_um3_max:.2f} µm³")
    print("="*50)
    
    while (diameter_um_min >= min_diameter_um or diameter_um_max >= min_diameter_um) and (remaining_km > 0):
        step += 1
        # Convert to meters
        d_m = diameter_um_min * 1e-6
        
        # 1. Calculate contact area (m²)
        A = 0.5 * math.pi * d_m**2
        
        # 2. Calculate mass loss (mg/km)
        mass_loss_mg_min = (polymers[polymer]["a"] * w_eff_min * 1000 * A)
        mass_loss_mg_max = (polymers[polymer]["a"] * w_eff_max * 1000 * A)
        
        # 3. Calculate volume loss (µm³/km)
        volume_loss_um3_min = (mass_loss_mg_min * 1e9) / polymers[polymer]["density"]  # mg → µg → µm³
        volume_loss_um3_max = (mass_loss_mg_max * 1e9) / polymers[polymer]["density"]
        
        # 4. Update volume (µm³)
        initial_volume_um3_min = (math.pi/6) * diameter_um_min**3
        initial_volume_um3_max = (math.pi/6) * diameter_um_max**3
        print(f"Initial Volume (min): {initial_volume_um3_min:.2f} µm³")
        print(f"Initial Volume (max): {initial_volume_um3_max:.2f} µm³")
        new_volume_um3_min = initial_volume_um3_min - volume_loss_um3_min
        print(f"New Volume (min): {new_volume_um3_min:.2f} µm³")
        new_volume_um3_max = initial_volume_um3_min - volume_loss_um3_max
        print(f"New Volume (max): {new_volume_um3_max:.2f} µm³")
        
        if new_volume_um3_min <= 0 or new_volume_um3_max <= 0:
            print(f"Partikel vollständig abradiert nach {step} Schritten")
            break
            
        # 5. Calculate new diameter (µm)
        new_diameter_um_min = (6 * new_volume_um3_min / math.pi) ** (1/3)
        new_diameter_um_max = (6 * new_volume_um3_max / math.pi) ** (1/3)
        
        # Progress output
        print(f"Schritt {step}:")
        print(f"• Durchmesser (min): {diameter_um_min:.2f} → {new_diameter_um_min:.2f} µm")
        print(f"• Durchmesser (max): {diameter_um_min:.2f} → {new_diameter_um_max:.2f} µm")
        print(f"• Massenverlust (min): {mass_loss_mg_min:.6f} mg/km")
        print(f"• Massenverlust (max): {mass_loss_mg_max:.6f} mg/km")
        print(f"• Volumenverlust (min): {volume_loss_um3_min:.2f} µm³")
        print(f"• Volumenverlust (max): {volume_loss_um3_max:.2f} µm³")
        print("-"*50)
        
        # Update for next iteration
        diameter_um_min = new_diameter_um_min # um -> µm
        diameter_um_max = new_diameter_um_max

        remaining_km -= 1
    
    print("Endergebnis:")
    print(f"MIN: Finaler Durchmesser: {diameter_um_min:.2f} µm")
    print(f"MAX: Finaler Durchmesser: {diameter_um_max:.2f} µm")
    print(f"Reststrecke: {remaining_km:.2f} km")
    print("="*50)

simulate_abrasion()