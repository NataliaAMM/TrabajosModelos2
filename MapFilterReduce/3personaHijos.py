class persona:
    def __init__(self, nombre, edad, estCivil, hijos):
        self.nombre = nombre
        self.edad = edad
        self.estCivil = estCivil
        self.hijos = hijos

personas = [persona("A",38,"CASADO",1),persona("B",42,"VIUDO",0),
            persona("C",55,"CASADO",3),persona("D",28,"SOLTERO",1),
            persona("E",15,"SOLTERO",0),persona("F",60,"VIUDO",2)]

print len(map(lambda x:x.nombre, filter(lambda x: x.edad>=40 and
                                        x.edad<=60 and x.hijos<=2, personas)))
