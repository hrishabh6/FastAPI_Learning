#suppose another function which returns average marks of all students
#import database dictionary from sortedStudents.py
from models.students import dict_db

async def average_marks():
    print("Calculating average marks...")
    total_marks = sum(dict_db.values())
    average = total_marks / len(dict_db)
    result = {"average_marks": average}
    print("Average marks calculated")
    return result