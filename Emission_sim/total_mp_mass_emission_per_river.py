def total_mp_mass_emission_per_river(simulation_results_by_water_type, em_results):
    """
    Calculate the total microplastic mass emission per river type based on simulation results and emission data.
    Args:
        simulation_results_by_water_type (dict): Results of the abrasion simulation categorized by water type.
        em_results (dict): Emission results for each river type.
    Returns:
        dict: A dictionary containing the total microplastic mass emission per river type.
    """
    final_results = {}

    for water_type, sim_data in simulation_results_by_water_type.items():

        em_data = em_results[water_type]
        final_results[water_type] = {}

        for polymer in sim_data:
            sim_polymer = sim_data[polymer]

            # Beispiel: 'ps' -> 'micro_ps' und 'macro_ps'
            micro_key = f"number_of_emitted_micro_{polymer}"
            macro_key = f"number_of_emitted_macro_{polymer}"

            num_micro = em_data.get(micro_key, 0)
            num_macro = em_data.get(macro_key, 0)

            # total_volume_loss_min = sim_polymer.get("total_volume_loss_min", 0)
            # total_volume_loss_max = sim_polymer.get("total_volume_loss_max", 0)
            total_mass_loss_min = sim_polymer.get("total_mass_loss_min", 0)
            total_mass_loss_max = sim_polymer.get("total_mass_loss_max", 0)

            final_results[water_type][polymer] = {
                # "total_volume_loss_min_macro": total_volume_loss_min * num_macro,
                # "total_volume_loss_min_micro": total_volume_loss_min * num_micro,
                # "total_volume_loss_max_macro": total_volume_loss_max * num_macro,
                # "total_volume_loss_max_micro": total_volume_loss_max * num_micro,
                "total_mass_loss_min_macro": total_mass_loss_min * num_macro,
                "total_mass_loss_min_micro": total_mass_loss_min * num_micro,
                "total_mass_loss_max_macro": total_mass_loss_max * num_macro,
                "total_mass_loss_max_micro": total_mass_loss_max * num_micro,
            }
        
    return final_results  

