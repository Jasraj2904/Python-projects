def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

def main():
    rides = {
        1: ("Bike", {
            1: "Sport Bike",
            2: "Cruiser"
        }),
        2: ("Car", {
            1: "Sedan",
            2: "SUV"
        })
    }

    print("==== Select Your Ride ====")
    for k, (name, _) in rides.items():
        print(f"{k}. {name}")

    main_choice = get_int("Choose category (1/2): ")

    if main_choice not in rides:
        print("Invalid choice. Exiting.")
        return

    main_name, sub_menu = rides[main_choice]

    print(f"\n-- {main_name} Types --")
    for k, v in sub_menu.items():
        print(f"{k}. {v}")

    sub_choice = get_int("Choose subcategory (1/2): ")

    if sub_choice not in sub_menu:
        print("Invalid choice. Exiting.")
        return

    print(f"\nYou selected: {main_name} → {sub_menu[sub_choice]}")

if __name__ == "__main__":
    main()
