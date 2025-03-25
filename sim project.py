# Function to display SIM providers
def show_providers():
    print("\nAvailable SIM Providers:")
    print("1. Airtel")
    print("2. Jio")
    print("3. Idea (Vi)")

# Function to display recharge plans
def show_plans(provider):
    plans = {
        "Airtel": {"199": "1.5GB/day - 28 Days", "399": "2.5GB/day - 56 Days"},
        "Jio": {"209": "1GB/day - 28 Days", "479": "1.5GB/day - 56 Days"},
        "Idea": {"249": "1.5GB/day - 28 Days", "449": "2GB/day - 56 Days"}
    }

    print(f"\n{provider} Recharge Plans:")
    for price, details in plans[provider].items():
        print(f"₹{price} - {details}")

# Function for SIM recharge
def recharge():
    show_providers()
    choice = input("\nEnter your SIM provider (Airtel/Jio/Idea): ").capitalize()

    if choice in ["Airtel", "Jio", "Idea"]:
        show_plans(choice)
        amount = input("\nEnter recharge amount: ₹")

        if amount in ["199", "399", "209", "479", "249", "449"]:
            print(f"\nRecharge Successful! You have recharged ₹{amount} for {choice}.")
        else:
            print("\nInvalid amount! Choose from the available plans.")
    else:
        print("\nInvalid provider! Try again.")

# Run the program
recharge()