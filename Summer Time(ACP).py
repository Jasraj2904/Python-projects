weather = input("Enter the current weather (summer, winter, rainy, windy): ").lower()

if weather == "summer":
    print("It's hot outside! Wear light cotton clothes and drink plenty of water.")
elif weather == "winter":
    print("It's cold outside! Wear warm clothes and stay cozy.")
elif weather == "rainy":
    print("It's rainy outside! Carry an umbrella and wear waterproof shoes.")
elif weather == "windy":
    print("It's windy outside! Wear a windbreaker or a jacket.")
else:
    print("Sorry, I don't have suggestions for this weather. Stay safe!")
