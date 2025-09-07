import random
import time
def get_random_date(startdate , enddate):
    print("Printing random date between " , startdate , "and" , enddate)
    random_generator = random.random()
    date_format = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(startdate , date_format))
    end_time = time.mktime(time.strptime(enddate , date_format))
    random_time = start_time + random_generator * (end_time - start_time)
    random_date = time.strftime(date_format , time.localtime(random_time))
    return random_date
print("Random date = " , get_random_date("4/29/2012" , "9/7/2025"))