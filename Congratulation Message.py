# Ask for user input
name = input("Enter your name: ")
achievement = input("What did you achieve? ")

# Using string operations
name = name.strip().title()  # Removes extra spaces and capitalizes the name
achievement = achievement.strip().capitalize()

# Create the congratulations message
message = "Congratulations, " + name + "! 🎉\n"
message += "You have successfully achieved: " + achievement + ".\n"
message += "We are proud of you, " + name.split()[0] + "! Keep it up!"

# Display the message
print("\n" + "-"*50)
print(message)
print("-"*50)
