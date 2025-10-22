import json

# ✅ Python dictionary (like database)
student_data = {
    "name": "Temesgen Mehari",
    "age": 23,
    "department": "Computer Science",
    "skills": ["Python", "Networking", "Digital Forensics"]
}

# --- Serialize (Save data to file) ---
with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)
print("✅ Data saved successfully to student.json")

# --- Deserialize (Load data from file) ---
with open("student.json", "r") as file:
    loaded_data = json.load(file)

print("\n📘 Loaded Data:")
print(loaded_data)
