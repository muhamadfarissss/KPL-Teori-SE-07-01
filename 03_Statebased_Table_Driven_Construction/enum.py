from enum import Enum

class jenis_kelamin(Enum):
    Laki_Laki = 1
    Perempuan = 2

print(jenis_kelamin.Laki_Laki)#value of enum
print(jenis_kelamin.Laki_Laki.name)#name of enum
print(jenis_kelamin.Laki_Laki.value)#value of Laki_Laki
