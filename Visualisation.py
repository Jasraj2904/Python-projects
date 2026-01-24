import matplotlib.pyplot as plt
students = ["Jasraj", "Divanshi", "Kaash", "Subeg", "Sachit"]
marks = [78, 85, 67, 90, 72]
attendance = [92, 88, 80, 95, 85]
plt.plot(students, marks)
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
plt.bar(students, attendance)
plt.title("Students Attendance")
plt.xlabel("Students")
plt.ylabel("Attendance (%)")
plt.show()
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()
plt.scatter(marks, attendance)
plt.title("Marks vs Attendance")
plt.xlabel("Marks")
plt.ylabel("Attendance (%)")
plt.show()