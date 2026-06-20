TIRE_DATA = {
    "Soft": {"lifespan": 15, "time_loss": 0.15},
    "Medium": {"lifespan": 25, "time_loss": 0.10},
    "Hard": {"lifespan": 40, "time_loss": 0.05}
}

def calculate_pit_window(total_laps, starting_tire):
    lifespan = TIRE_DATA[starting_tire]["lifespan"]
    pit_lap = min(lifespan, total_laps - 1)
    
    strategy_output = f"Locked in: {total_laps} laps starting on {starting_tire}s.\n"
    if pit_lap <= 0 or pit_lap >= total_laps:
        strategy_output += "Strategy: No pit stop needed! You can push to the end."
    else:
        strategy_output += f"Optimal Pit Window: Lap {max(1, pit_lap - 2)} to Lap {pit_lap + 1}\n"
        strategy_output += f"Target Box Lap: Lap {pit_lap}"
        
    return strategy_output
