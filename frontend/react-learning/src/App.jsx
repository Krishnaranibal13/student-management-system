import { useEffect, useState } from "react";

import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";

import {
  getStudents,
  addStudent,
  updateStudent,
  deleteStudent,
} from "./services/api";

function App() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [editId, setEditId] = useState(null);

  const loadStudents = async () => {
    const data = await getStudents();
    setStudents(data);
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadStudents();
  }, []);

  const handleSubmit = async () => {
    if (name === "" || age === "") {
      alert("Please fill all fields");
      return;
    }

    const student = {
      name,
      age: Number(age),
    };

    if (editId === null) {
      await addStudent(student);
    } else {
      await updateStudent(editId, student);
      setEditId(null);
    }

    setName("");
    setAge("");

    await loadStudents();
  };

  const handleEdit = (student) => {
    setName(student.name);
    setAge(student.age);
    setEditId(student.id);
  };

  const handleDelete = async (id) => {
    await deleteStudent(id);
    await loadStudents();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Management System</h1>

      <StudentForm
        name={name}
        setName={setName}
        age={age}
        setAge={setAge}
        onSubmit={handleSubmit}
        isEditing={editId !== null}
      />

      <hr />

      <StudentList
        students={students}
        onEdit={handleEdit}
        onDelete={handleDelete}
      />
    </div>
  );
}

export default App;