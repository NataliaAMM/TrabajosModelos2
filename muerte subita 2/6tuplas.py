class tupla:
    def __init__(self, valorx, valory):
        self.valorx = valorx
        self.valory = valory



print reduce(lambda x,y: x+y, map(lambda w:w.valorx,
                                  filter(lambda z: z.valorx==(z.valory*(z.valory+1))/2,
                                         [tupla(1,1), tupla(5,2), tupla(15,5), tupla(234,7), tupla(21,6)])))
