def total_mp_mass_emission_per_river(simulation_results_by_water_type, em_results):
    """
    Calculate the total microplastic mass emission per river type based on simulation results and emission data.
    Args:
        simulation_results_by_water_type (dict): Results of the abrasion simulation categorized by water type.
        em_results (dict): Emission results for each river type.
    Returns:
        dict: A dictionary containing the total microplastic mass emission per river type.
    """
    # Step 1: Initialize the final results dictionary
    final_results = {}

    # Step 2: Iterate over each water type in the simulation results
    for water_type, sim_data in simulation_results_by_water_type.items():

        # Step 3: Get emission data for the current water type
        em_data = em_results[water_type]
        final_results[water_type] = {}

        # Step 4: For each polymer, calculate total mass loss for micro and macro particles
        for polymer in sim_data:
            sim_polymer = sim_data[polymer]

            # Step 4a: Build keys for micro and macro emission numbers
            # Beispiel: 'ps' -> 'micro_ps' und 'macro_ps'
            micro_key = f"number_of_emitted_micro_{polymer}"
            macro_key = f"number_of_emitted_macro_{polymer}"

            # Step 4b: Get the number of emitted micro and macro particles
            num_micro = em_data.get(micro_key, 0)
            num_macro = em_data.get(macro_key, 0)

            # total_volume_loss_min = sim_polymer.get("total_volume_loss_min", 0)
            # total_volume_loss_max = sim_polymer.get("total_volume_loss_max", 0)

            # Step 4c: Get the total mass loss values from the simulation
            total_mass_loss_micro_min = sim_polymer.get("total_mass_loss_micro_min", 0)
            total_mass_loss_micro_max = sim_polymer.get("total_mass_loss_micro_max", 0)
            total_mass_loss_macro_min = sim_polymer.get("total_mass_loss_macro_min", 0)
            total_mass_loss_macro_max = sim_polymer.get("total_mass_loss_macro_max", 0)

            # Step 4d: Calculate and store the total mass loss for micro and macro particles
            final_results[water_type][polymer] = {
                # "total_volume_loss_min_macro": total_volume_loss_min * num_macro,
                # "total_volume_loss_min_micro": total_volume_loss_min * num_micro,
                # "total_volume_loss_max_macro": total_volume_loss_max * num_macro,
                # "total_volume_loss_max_micro": total_volume_loss_max * num_micro,
                
                "total_mass_loss_min_macro": total_mass_loss_macro_min * num_macro,
                "total_mass_loss_min_micro": total_mass_loss_micro_min * num_micro,
                "total_mass_loss_max_macro": total_mass_loss_macro_max * num_macro,
                "total_mass_loss_max_micro": total_mass_loss_micro_max * num_micro,
            }
        
    # Step 5: Return the final results dictionary
    return final_results  

