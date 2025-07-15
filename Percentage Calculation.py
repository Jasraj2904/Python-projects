print("Enter Marks Obtained in 7 Subjects")
math = int(input("maths :"))
english = int(input("English :"))
science = int(input("Science :"))
social_science = int(input("Social Science :"))
hindi = int(input("Hindi :"))
punjabi = int(input("Punjabi"))
computer = int(input("Computer :"))

sum = math+english+science+social_science+hindi+punjabi+computer
print("Sum of Math, English, Science, Social Science, Hindi, Punjabi and Computer", sum)

perc = (sum/700) * 100
print("Your percentage is :", perc)