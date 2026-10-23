from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mysql.connector import Error
from db import connection, cursor

app = FastAPI(title="Student Management System")


class Student(BaseModel):
    name: str
    age: int


@app.get("/health")
def health():
    try:
        connection.ping(reconnect=True, attempts=1, delay=0)
        return {"status": "healthy", "database": "connected"}
    except Error:
        raise HTTPException(status_code=503, detail="Database unavailable")


@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students ORDER BY id")
    return cursor.fetchall()


@app.post("/students")
def add_student(student: Student):
    cursor.execute(
        "INSERT INTO students(name, age) VALUES(%s, %s)",
        (student.name, student.age),
    )
    connection.commit()
    return {"message": "Student Added Successfully"}


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    cursor.execute(
        "UPDATE students SET name=%s, age=%s WHERE id=%s",
        (student.name, student.age, student_id),
    )
    connection.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student Updated Successfully"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (student_id,),
    )
    connection.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student Deleted Successfully"}
