const BASE_URL = "http://127.0.0.1:8000";

export async function getStudents() {
  const response = await fetch(`${BASE_URL}/students`);
  return await response.json();
}

export async function addStudent(student) {
  await fetch(`${BASE_URL}/students`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(student),
  });
}

export async function updateStudent(id, student) {
  await fetch(`${BASE_URL}/students/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(student),
  });
}

export async function deleteStudent(id) {
  await fetch(`${BASE_URL}/students/${id}`, {
    method: "DELETE",
  });
}