from strategy import TIRE_DATA, calculate_pit_window

def main():
    while True:
        print("\n==================================")
        print("🏎️  F1 PIT STOP STRATEGY TOOL 🏎️")
        print("==================================")
        print("1. Calculate Optimal Pit Window")
        print("2. View Tire Compound Data")
        print("3. Exit")
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice not in ['1', '2', '3']:
                raise ValueError("Please enter a valid number (1, 2, or 3).")
        except ValueError as e:
            print(f"\nError: {e}")
            continue
        
        if choice == '1':
            try:
                total_laps = int(input("\nEnter total race laps: "))
                if total_laps <= 0:
                    raise ValueError("Laps must be greater than 0.")
                    
                starting_tire = input("Enter starting tire (Soft, Medium, Hard): ").strip().capitalize()
                if starting_tire not in TIRE_DATA:
                    raise ValueError("Invalid tire compound. Choose Soft, Medium, or Hard.")
                
                strategy_output = calculate_pit_window(total_laps, starting_tire)
                
                print(f"\n--- Strategy Output ---")
                print(strategy_output)
                
                with open("race_strategy.txt", "w") as file:
                    file.write("F1 STRATEGY REPORT\n====================\n")
                    file.write(strategy_output)
                print("\n[Strategy successfully saved to race_strategy.txt]")
                    
            except ValueError as e:
                print(f"\nError: {e}")
                
        elif choice == '2':
            print("\n--- Tire Compound Data ---")
            for compound, data in TIRE_DATA.items():
                print(f"{compound}: Lasts ~{data['lifespan']} laps, drops {data['time_loss']}s per lap.")
                
        elif choice == '3':
            print("\nBox, box. Exiting strategy tool.")
            break

if __name__ == "__main__":
    main()
