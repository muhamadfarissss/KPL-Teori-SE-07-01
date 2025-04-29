from enum import Enum

class jenis_kelamin(Enum):
    pria = 1
    wanita = 2

patients = []

def add_patients (name: str, gender: jenis_kelamin):
    if not isinstance(gender, jenis_kelamin):
        raise ValueError("jenis kelamin harusnya adalah pria atau wanita")
    patients.append({"name": name, "gender": gender.name})

add_patients("Andi", jenis_kelamin.pria)
add_patients("Siti", jenis_kelamin.wanita)

for patient in patients:
    print(f"{patient['name']} adalah {patient['gender']}")

