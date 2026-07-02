function StudentForm({
  name,
  setName,
  age,
  setAge,
  onSubmit,
  isEditing,
}) {
  return (
    <div>
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />

      <br /><br />

      <button onClick={onSubmit}>
        {isEditing ? "Update Student" : "Add Student"}
      </button>
    </div>
  );
}

export default StudentForm;