#define the function...
#let's do some big code task here
#suppose we have an imaginary database call, we are processing data inside process_ping()
#to mimic database i am using a dictionary
#in real world scenario, this function can have complex logic
#this database has marks of 20 students and their names

#lets make this even more modular... 
#we will create a seperate directory called service and put this file in that directory

#lets go even further.. lets make seperate files for each function

#this function returns top 10 students based on their marks

#import students database from models folder
from models.students import dict_db

async def sorted_students():
    #sort the dictionary based on marks in descending order and get top 10
    top_students = sorted(dict_db.items(), key=lambda x: x[1], reverse=True)[:10]
    result = {"top_students": top_students}
    print("Top students processed")
    return result

