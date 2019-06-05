class persona:
    def __init__(self, nombre, genero, cargo, salario):
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.salario = salario

empleados = [persona("A","F","GERENTE",17000000),
             persona("B","M","VENDEDOR",1300000),
             persona("C","F","SECRETARIA",1120000),
             persona("D","F","VENDEDOR",1300000),
             persona("F","M","CONTADOR",3100000),
             persona("G","M","INGENIERO",3200000)]

print "Salario hombres: "+str(reduce(lambda x,y:x+y, map(
    lambda x:x.salario, filter(lambda x:x.genero=="M", empleados))))
print "Salario mujeres: "+str(reduce(lambda x,y:x+y, map(
    lambda x:x.salario, filter(lambda x:x.genero=="F", empleados))))
