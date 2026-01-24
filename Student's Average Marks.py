import matplotlib.pyplot as plt
student_names = ["Jasraj" , "Divanshi" , "Kaashvi" , "Subeg" , "Sachit"]
student_marks = [50 , 50 , 45 , 44 , 40]
marks_perc = []
for x in student_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(student_names , student_marks)
    plt.title("Students Marks Graphs")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(student_names , marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Nmaes")
    plt.ylabel("Student Percentage")
    plt.show()
percentage_bar_chart()