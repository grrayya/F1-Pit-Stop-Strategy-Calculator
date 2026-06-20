def main():
    while True:
        print("\n==================================")
        print("🏎️  F1 PIT STOP STRATEGY TOOL 🏎️")
        print("==================================")
        print("1. Calculate Optimal Pit Window")
        print("2. View Tire Compound Data")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
      elif choice == '1':
            total_laps = int(input("\nEnter total race laps: "))
            starting_tire = input("Enter starting tire (Soft, Medium, Hard): ").capitalize()
            
            if starting_tire in TIRE_DATA:
                lifespan = TIRE_DATA[starting_tire]["lifespan"]
                pit_lap = min(lifespan, total_laps - 1)
                
                print(f"\n--- Strategy Output ---")
                print(f"Locked in: {total_laps} laps starting on {starting_tire}s.")
                if pit_lap <= 0 or pit_lap >= total_laps:
                    print("Strategy: No pit stop needed! You can push to the end.")
                else:
                    print(f"Optimal Pit Window: Lap {max(1, pit_lap - 2)} to Lap {pit_lap + 1}")
                    print(f"Target Box Lap: Lap {pit_lap}")
        elif choice == '2':
            print("\n--- Tire Compound Data ---")
            for compound, data in TIRE_DATA.items():
                print(f"{compound}: Lasts ~{data['lifespan']} laps, drops {data['time_loss']}s per lap.")
        elif choice == '3':
            print("\nBox, box. Exiting strategy tool.")
            break
        else:
            print("\nInvalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
