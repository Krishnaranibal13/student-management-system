from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import connection, cursor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

class Student(BaseModel):
    name: str
    age: int

@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

@app.post("/students")
def add_student(student: Student):

    query = """
    INSERT INTO students(name,age)
    VALUES(%s,%s)
    """

    cursor.execute(query, (student.name, student.age))
    connection.commit()

    return {"message": "Student Added Successfully"}


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    query = """
    UPDATE students
    SET name=%s, age=%s
    WHERE id=%s
    """

    cursor.execute(query, (student.name, student.age, student_id))
    connection.commit()

    return {"message": "Student Updated Successfully"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (student_id,))

    connection.commit()

    return {"message": "Student Deleted Successfully"}