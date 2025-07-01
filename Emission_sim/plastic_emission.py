from PA.pa import pa
from PET.pet import pet
from PS.ps import ps
from processing.em_factor import calculate_emission_factors

def plastic_emission():
    # Step 1: Calculate macroplastic emission sums for PA, PET, and PS
    _,pa_macro_sum,_ = pa()
    _,pet_macro_sum,_ = pet()
    _,ps_macro_sum,_ = ps()

    # Step 2: Calculate microplastic emission sums for PA, PET, and PS
    _,_,pa_micro_sum = pa()
    _,_,pet_micro_sum = pet()
    _,_,ps_micro_sum = ps()

    # Step 3: Get the total emission factor (e.g., based on population or other scaling)
    total_factor = calculate_emission_factors()
    # _,_, total_population = calculate_emission_factors()

    # Step 4: Calculate total emissions for each polymer and size using the emission factor
    plastic_em_macro_pa = total_factor * pa_macro_sum
    plastic_em_micro_pa = total_factor * pa_micro_sum
    plastic_em_macro_pet = total_factor * pet_macro_sum
    plastic_em_micro_pet = total_factor * pet_micro_sum
    plastic_em_macro_ps = total_factor * ps_macro_sum
    plastic_em_micro_ps = total_factor * ps_micro_sum

    # Step 5: Return the calculated emissions as a tuple
    return (plastic_em_macro_ps, plastic_em_micro_ps,plastic_em_macro_pet,plastic_em_micro_pet,plastic_em_macro_pa,plastic_em_micro_pa)

    # Reihenfolge!!!