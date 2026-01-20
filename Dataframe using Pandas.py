import pandas as pd
import numpy as np
exam_data = {'name' : ['Jasraj' , 'Divanshi' , 'Kaashvi' , 'Sachit' , 'Subeg' , 'Harshit'] , 
        'score' : [21 , 19 , 15 , np.nan , 19 , np.nan] , 
        'attempts' : [1 , 1 , 2 , 5 , 6 , 3 ] , 
        'qualify' : ['yes' , 'yes' , 'yes' , 'no' , 'yes' , 'no']}
labels = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
df = pd.DataFrame(exam_data , index= labels)
print("Summary of the basic information about this dataframe and its data:")
print(df.info())