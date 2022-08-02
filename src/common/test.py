from common_repo.personas.schemas import Persona, Animal
from common_repo.base_de_datos.schemas import Contratista

P1 = Persona(25832303, "Miguel","Herize","M")
print("Dueño: ",P1.cedula)

M1 = Animal(25832303, "Tommy","Perro","M")
print("Mascota: ",M1.nombre)

C1 = Contratista(25832303, "Miguel","Herize","Merida")
print("Contratista: ",C1.nombre)