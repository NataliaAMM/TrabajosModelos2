class carta:
    def __init__(self, color, pinta, valor):
        self.color = color
        self.pinta = pinta
        self.valor = valor


lista = [carta("rojo","corazon","J"),carta("rojo","corazon",9),
         carta("negro","pica",3),carta("rojo","diamante",7),
         carta("rojo","corazon",2),carta("rojo","diamante","A"),
         carta("negro","trebol","K")]

print (reduce(lambda x,y: x+y, map(lambda x:x.valor, filter(
    lambda x: x.valor!="A" and x.valor!="J" and x.valor!="Q" and
    x.valor!="K", filter(lambda x: x.color=="rojo", lista)))))
