def main():
    while True:
        print("\n==================================")
        print("🏎️  F1 PIT STOP STRATEGY TOOL 🏎️")
        print("==================================")
        print("1. Calculate Optimal Pit Window")
        print("2. View Tire Compound Data")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            print("\nCalculating pit window... (Logic coming soon)")
        elif choice == '2':
            print("\nFetching tire data... (Logic coming soon)")
        elif choice == '3':
            print("\nBox, box. Exiting strategy tool.")
            break
        else:
            print("\nInvalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
