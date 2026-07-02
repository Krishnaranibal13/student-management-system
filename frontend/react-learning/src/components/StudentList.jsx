function StudentList({
  students,
  onEdit,
  onDelete,
}) {
  return (
    <div>

      {students.map((student) => (

        <div key={student.id}>

          <h3>{student.name}</h3>

          <p>{student.age}</p>

          <button onClick={() => onEdit(student)}>
            Edit
          </button>

          <button onClick={() => onDelete(student.id)}>
            Delete
          </button>

          <hr />

        </div>

      ))}

    </div>
  );
}

export default StudentList;