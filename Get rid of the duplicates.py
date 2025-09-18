student_data = {'id1': {'name' : ['Divanshi'] , 'class' :['VIII'] , 'subject' : ['Maths , Science']} , 
'id2' : {'name' : ['Jasraj'] , 'class' :['VIII'] , 'subject' : ['Maths , Science']}  , 
'id3': {'name' : ['Divanshi'] , 'class' :['VIII'] , 'subject' : ['Maths , Science']} , }
result = {}
for key,value in student_data.items():
    if value not in result.values() :
        result[key] = value
print(result)