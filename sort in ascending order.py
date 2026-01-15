import numpy as np
data_type = [('name', 'S15') , ('class' , int) , ('height', float)]
student_details = [('Jasraj' , 8 , 168.2) , ('Divanshi' , 8 , 154.1) , ('Sachit' , 8 , 155.3) , ('Udhav' , 8 , 156.4)]
students = np.array(student_details , dtype = data_type)
print("Original Array")
print(students)
print("Sort by Height")
print(np.sort(students, order= 'height'))