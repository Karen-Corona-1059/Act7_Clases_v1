print("\nIntroduccion a clases")
class animal:
    edad=4
    raza="Doberman"
    comida="Chuletas"
    def come(self):
        print(f"el perro come: "+self.comida)    

print(animal)

print("\nCreando el objeto de la clase animal")
perro = animal()
print(f"Mi perro tiene: {perro.edad} años")
print(f"Y es un: {perro.raza}")
perro.come()




print("\n")