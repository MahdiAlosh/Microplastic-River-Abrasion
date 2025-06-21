from PA.pa import pa
from PET.pet import pet
from PS.ps import ps
from processing.em_factor import calculate_emission_factors

def plastic_emission():
    # Assuming macro and micro results are already calculated
    _,pa_macro_sum,_ = pa()
    _,pet_macro_sum,_ = pet()
    _,ps_macro_sum,_ = ps()

    _,_,pa_micro_sum = pa()
    _,_,pet_micro_sum = pet()
    _,_,ps_micro_sum = ps()

    # # summarize macro results of PA, PET, PS
    # macro_summary = pa_macro_sum + pet_macro_sum + ps_macro_sum
    # # summarize micro results of PA, PET, PS
    # micro_summary = pa_micro_sum + pet_micro_sum + ps_micro_sum

    total_factor = calculate_emission_factors()
    # _,_, total_population = calculate_emission_factors()

    plastic_em_macro_pa = total_factor * pa_macro_sum
    plastic_em_micro_pa = total_factor * pa_micro_sum
    plastic_em_macro_pet = total_factor * pet_macro_sum
    plastic_em_micro_pet = total_factor * pet_micro_sum
    plastic_em_macro_ps = total_factor * ps_macro_sum
    plastic_em_micro_ps = total_factor * ps_micro_sum

    # print(f"Total Population: {total_population}, Factor: {total_factor}")
    # print(f"Macro Plastic Emission: {macro_summary:.2f} kg")
    # print(f"Micro Plastic Emission: {micro_summary:.2f} kg")
    # print(f"Plastic Emission Macro: {plastic_em_macro:.2f} kg")
    # print(f"Plastic Emission Micro: {plastic_em_micro:.2f} kg")

    return (plastic_em_macro_pa, plastic_em_micro_pa,plastic_em_macro_pet,plastic_em_micro_pet,plastic_em_macro_ps,plastic_em_micro_ps)
